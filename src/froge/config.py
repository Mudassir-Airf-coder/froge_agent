"""Central configuration system.

Defaults + environment overrides + validation.
Uses plain pydantic BaseModel (no pydantic-settings dependency).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field


class FrogeSettings(BaseModel):
    """FROGE system configuration.

    Environment variables are prefixed with FROGE_.
    Example: FROGE_LOG_LEVEL=DEBUG
    """

    log_level: str = Field(default="INFO", description="Logging level")
    data_dir: Path = Field(
        default_factory=lambda: Path.home() / ".froge",
        description="Base directory for FROGE state and data",
    )
    manifest_path: Optional[Path] = Field(
        default=None,
        description="Path to tool manifest YAML/JSON. None = built-in defaults.",
    )
    dry_run: bool = Field(default=False, description="If true, plan but do not mutate")
    max_retries: int = Field(default=3, ge=0, le=20)
    command_timeout_seconds: int = Field(default=120, ge=5, le=3600)
    allow_destructive: bool = Field(
        default=False,
        description="Must be true to permit destructive operations",
    )

    def ensure_data_dir(self) -> Path:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        return self.data_dir


def _env_bool(key: str, default: bool) -> bool:
    val = os.environ.get(key)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")


def _env_int(key: str, default: int) -> int:
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return int(val)
    except ValueError:
        return default


def load_settings(**overrides: Any) -> FrogeSettings:
    """Load settings from environment (FROGE_*) with optional programmatic overrides."""
    data: dict[str, Any] = {
        "log_level": os.environ.get("FROGE_LOG_LEVEL", "INFO"),
        "dry_run": _env_bool("FROGE_DRY_RUN", False),
        "max_retries": _env_int("FROGE_MAX_RETRIES", 3),
        "command_timeout_seconds": _env_int("FROGE_COMMAND_TIMEOUT_SECONDS", 120),
        "allow_destructive": _env_bool("FROGE_ALLOW_DESTRUCTIVE", False),
    }
    data_dir = os.environ.get("FROGE_DATA_DIR")
    if data_dir:
        data["data_dir"] = Path(data_dir)
    manifest = os.environ.get("FROGE_MANIFEST_PATH")
    if manifest:
        data["manifest_path"] = Path(manifest)
    data.update(overrides)
    return FrogeSettings(**data)
