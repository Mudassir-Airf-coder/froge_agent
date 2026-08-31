"""Tool manifest schema and registry — declarative source of truth for tools."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import yaml
from pydantic import BaseModel, Field, field_validator

from froge.results import OperationResult, Status
from froge.state import ComponentState


class HealthCheckSpec(BaseModel):
    kind: str = Field(..., description="version|executable|process|gateway|functional|custom")
    command: Optional[str] = None
    expected_exit_code: int = 0
    timeout_seconds: int = 30
    notes: str = ""


class ToolManifest(BaseModel):
    id: str = Field(..., min_length=1)
    name: str
    role: str = ""
    description: str = ""
    required: bool = False
    platform: list[str] = Field(default_factory=lambda: ["windows", "linux", "darwin"])
    version: Optional[str] = None
    source: Optional[str] = None
    installation_method: str = Field(
        default="unknown",
        description="pip|npm|winget|chocolatey|binary|script|manual|system|unknown",
    )
    dependencies: list[str] = Field(default_factory=list)
    executable: Optional[str] = None
    executable_aliases: list[str] = Field(default_factory=list)
    version_command: Optional[list[str]] = None
    command: Optional[str] = None
    install_command: Optional[list[str]] = None
    update_command: Optional[list[str]] = None
    configure_command: Optional[list[str]] = None
    start_command: Optional[list[str]] = None
    stop_command: Optional[list[str]] = None
    repair_command: Optional[list[str]] = None
    configuration: dict[str, Any] = Field(default_factory=dict)
    environment: dict[str, str] = Field(default_factory=dict)
    gateway: Optional[dict[str, Any]] = None
    health_checks: list[HealthCheckSpec] = Field(default_factory=list)
    functional_test: Optional[HealthCheckSpec] = None
    provider: Optional[str] = None
    mcp: Optional[str] = None
    known_errors: list[str] = Field(default_factory=list)
    recovery: Optional[str] = None
    permissions: list[str] = Field(default_factory=list)
    enabled: bool = True
    notes: str = ""
    validation_status: str = Field(
        default="unknown", description="verified|requires_validation|unknown"
    )
    status: ComponentState = ComponentState.UNKNOWN

    @field_validator("id")
    @classmethod
    def id_lower(cls, v: str) -> str:
        return v.strip().lower().replace(" ", "-")


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolManifest] = {}

    def register(self, tool: ToolManifest) -> None:
        self._tools[tool.id] = tool

    def unregister(self, tool_id: str) -> bool:
        return self._tools.pop(tool_id, None) is not None

    def get(self, tool_id: str) -> Optional[ToolManifest]:
        return self._tools.get(tool_id)

    def list(self, enabled_only: bool = False) -> list[ToolManifest]:
        tools = list(self._tools.values())
        if enabled_only:
            tools = [t for t in tools if t.enabled]
        return sorted(tools, key=lambda t: t.id)

    def enable(self, tool_id: str) -> bool:
        t = self.get(tool_id)
        if t is None:
            return False
        t.enabled = True
        return True

    def disable(self, tool_id: str) -> bool:
        t = self.get(tool_id)
        if t is None:
            return False
        t.enabled = False
        return True

    def validate(self) -> OperationResult:
        errors: list[str] = []
        for t in self._tools.values():
            if not t.id:
                errors.append(f"Tool missing id: {t.name}")
            if t.required and not t.executable and t.installation_method == "unknown":
                errors.append(
                    f"Required tool '{t.id}' has no executable and unknown install method"
                )
        status = Status.PASS if not errors else Status.FAIL
        return OperationResult(
            operation="registry.validate",
            status=status,
            message="Registry validation complete",
            errors=errors,
            data={"count": len(self._tools)},
        )

    def load_from_yaml(self, path: Path) -> OperationResult:
        try:
            raw = yaml.safe_load(path.read_text(encoding="utf-8"))
            if raw is None:
                items = []
            elif isinstance(raw, list):
                items = raw
            elif isinstance(raw, dict) and "tools" in raw:
                items = raw["tools"]
            else:
                return OperationResult(
                    operation="registry.load_yaml",
                    status=Status.FAIL,
                    message="YAML must be a list or contain a 'tools' key",
                    errors=["invalid structure"],
                )
            loaded = 0
            for item in items:
                self.register(ToolManifest.model_validate(item))
                loaded += 1
            return OperationResult(
                operation="registry.load_yaml",
                status=Status.PASS,
                message=f"Loaded {loaded} tool(s) from {path}",
                data={"loaded": loaded, "path": str(path)},
            )
        except Exception as exc:
            return OperationResult(
                operation="registry.load_yaml",
                status=Status.ERROR,
                message=str(exc),
                errors=[str(exc)],
            )

    def clear(self) -> None:
        self._tools.clear()

    def __len__(self) -> int:
        return len(self._tools)


def default_registry() -> ToolRegistry:
    """Pre-seeded registry. External agents remain REQUIRES VALIDATION."""
    reg = ToolRegistry()
    tools = [
        ToolManifest(
            id="python", name="Python", role="runtime", required=True,
            executable="python3", version_command=["python3", "--version"],
            installation_method="system", validation_status="verified",
            health_checks=[HealthCheckSpec(kind="version", command="python3 --version")],
            notes="Core runtime prerequisite",
        ),
        ToolManifest(
            id="git", name="Git", role="vcs", required=True,
            executable="git", version_command=["git", "--version"],
            installation_method="system", validation_status="verified",
            health_checks=[HealthCheckSpec(kind="version", command="git --version")],
        ),
        ToolManifest(
            id="node", name="Node.js", role="runtime", required=False,
            executable="node", version_command=["node", "--version"],
            installation_method="system", validation_status="verified",
            health_checks=[HealthCheckSpec(kind="version", command="node --version")],
        ),
        ToolManifest(
            id="npm", name="npm", role="package-manager", required=False,
            executable="npm", version_command=["npm", "--version"],
            installation_method="system", dependencies=["node"], validation_status="verified",
            health_checks=[HealthCheckSpec(kind="version", command="npm --version")],
        ),
        ToolManifest(
            id="opencode", name="OpenCode",
            role="Primary Software Engineering / Coding Agent",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION — no install command assumed",
        ),
        ToolManifest(
            id="hermes", name="Hermes",
            role="Persistent Automation / Long-Running Agent Runtime",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION",
        ),
        ToolManifest(
            id="openclaw", name="OpenClaw",
            role="Autonomous Agent / Automation Runtime",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION",
        ),
        ToolManifest(
            id="nemoclaw", name="NemoClaw",
            role="NVIDIA-oriented Agent/Runtime Integration",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION",
        ),
        ToolManifest(
            id="prime-agent", name="Prime Agent",
            role="Specialized Development/Agent Runtime",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION",
        ),
        ToolManifest(
            id="freebuff", name="FreeBuff / CodeBuff",
            role="Lightweight coding environment workflow",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION — inspect actual project before integration",
        ),
        ToolManifest(
            id="omni-router", name="Omni Router",
            role="Provider / Model Routing Layer",
            installation_method="unknown", validation_status="requires_validation",
            notes="REQUIRES VALIDATION — do not invent MCP",
        ),
    ]
    for t in tools:
        reg.register(t)
    return reg
