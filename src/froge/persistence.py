"""Persistent local state store — atomic JSON writes, no secrets."""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from froge.config import FrogeSettings, load_settings


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class StateStore:
    """Atomic JSON state store under data_dir/state.json."""

    def __init__(self, path: Optional[Path] = None, settings: Optional[FrogeSettings] = None):
        settings = settings or load_settings()
        settings.ensure_data_dir()
        self.path = path or (settings.data_dir / "state.json")
        self._data: dict[str, Any] = {"version": 1, "components": {}, "operations": []}
        self.load()

    def load(self) -> dict[str, Any]:
        if self.path.exists():
            try:
                self._data = json.loads(self.path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                self._data = {"version": 1, "components": {}, "operations": []}
        else:
            self._data = {"version": 1, "components": {}, "operations": []}
        return self._data

    def save(self) -> None:
        """Atomic write: write temp file then rename."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(self.path.parent), suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=2, default=str)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, self.path)
        except Exception:
            try:
                os.unlink(tmp)
            except OSError:
                pass
            raise

    def get_component(self, tool_id: str) -> dict[str, Any]:
        return dict(self._data.get("components", {}).get(tool_id, {}))

    def set_component(self, tool_id: str, **fields: Any) -> None:
        comps = self._data.setdefault("components", {})
        entry = comps.get(tool_id, {})
        entry.update(fields)
        entry["updated_at"] = _now()
        comps[tool_id] = entry
        self.save()

    def record_operation(
        self,
        operation: str,
        component: str,
        action: str,
        status: str,
        state_before: Optional[str] = None,
        state_after: Optional[str] = None,
        message: str = "",
        evidence: Optional[list] = None,
    ) -> None:
        ops = self._data.setdefault("operations", [])
        ops.append(
            {
                "timestamp": _now(),
                "operation": operation,
                "component": component,
                "action": action,
                "status": status,
                "state_before": state_before,
                "state_after": state_after,
                "message": message,
                "evidence_count": len(evidence or []),
            }
        )
        if len(ops) > 500:
            self._data["operations"] = ops[-500:]
        self.save()

    def record_verification(
        self, tool_id: str, status: str, state: str, levels: Optional[dict] = None
    ) -> None:
        self.set_component(
            tool_id,
            last_verification_status=status,
            last_verification_state=state,
            last_verification_at=_now(),
            last_verification_levels=levels or {},
        )

    def list_operations(self, limit: int = 50) -> list[dict[str, Any]]:
        ops = self._data.get("operations", [])
        return ops[-limit:]

    def summary(self) -> dict[str, Any]:
        comps = self._data.get("components", {})
        return {
            "path": str(self.path),
            "component_count": len(comps),
            "operation_count": len(self._data.get("operations", [])),
            "components": {
                k: {
                    "state": v.get("state"),
                    "version": v.get("version"),
                    "last_verification_status": v.get("last_verification_status"),
                }
                for k, v in comps.items()
            },
        }


def load_state(settings: Optional[FrogeSettings] = None) -> StateStore:
    return StateStore(settings=settings)
