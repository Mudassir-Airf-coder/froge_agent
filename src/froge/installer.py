"""Installation engine — manifest-driven, idempotent, dry-run aware."""

from __future__ import annotations

import subprocess
from typing import Optional

from froge.config import FrogeSettings, load_settings
from froge.discovery import discover_executable
from froge.manifest import ToolManifest
from froge.results import OperationResult, Status
from froge.state import ComponentState, desired_action


def _run(cmd: list[str], timeout: int = 120) -> tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except FileNotFoundError:
        return 127, "", "not found"
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"
    except Exception as exc:
        return 1, "", str(exc)


def discover_tool(tool: ToolManifest) -> OperationResult:
    if not tool.executable:
        return OperationResult(
            operation="install.discover",
            status=Status.SKIP,
            component=tool.id,
            state=ComponentState.UNKNOWN.value,
            message=f"{tool.id}: no executable (REQUIRES VALIDATION)",
        )
    vargs = (
        tool.version_command[1:]
        if tool.version_command and len(tool.version_command) > 1
        else ["--version"]
    )
    item = discover_executable(tool.executable, vargs)
    result = OperationResult(
        operation="install.discover",
        status=Status.PASS,
        component=tool.id,
        state=item.state.value,
        message=f"{tool.id}: {item.state.value}",
        data={"version": item.version, "path": item.path},
    )
    result.add_evidence(
        "discovery",
        summary=f"{tool.id}={item.state.value}",
        version=item.version,
        path=item.path,
    )
    return result


def install_tool(tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
    settings = settings or load_settings()
    disc = discover_tool(tool)
    if disc.state in (
        ComponentState.INSTALLED.value,
        ComponentState.HEALTHY.value,
        ComponentState.CONFIGURED.value,
    ):
        return OperationResult(
            operation="install.install",
            status=Status.SKIP,
            component=tool.id,
            state=disc.state,
            message=f"{tool.id}: already present — KEEP",
            evidence=disc.evidence,
        )
    if tool.installation_method == "unknown" or not tool.install_command:
        return OperationResult(
            operation="install.install",
            status=Status.SKIP,
            component=tool.id,
            state=ComponentState.UNKNOWN.value,
            message=f"{tool.id}: installation_method=unknown or no install_command (REQUIRES VALIDATION)",
        )
    if settings.dry_run:
        return OperationResult(
            operation="install.install",
            status=Status.SKIP,
            component=tool.id,
            state=ComponentState.MISSING.value,
            message=f"{tool.id}: dry_run — would run {tool.install_command}",
            data={"planned_command": tool.install_command},
        )
    code, out, err = _run(tool.install_command, timeout=settings.command_timeout_seconds)
    result = OperationResult(
        operation="install.install",
        component=tool.id,
        status=Status.PASS if code == 0 else Status.FAIL,
        message=f"{tool.id}: install exit={code}",
        data={"stdout": out[:500], "stderr": err[:500]},
    )
    result.add_evidence(
        "install_command",
        summary=" ".join(tool.install_command),
        exit_code=code,
        stdout=out[:300],
    )
    if code == 0:
        disc2 = discover_tool(tool)
        result.state = disc2.state
        result.evidence.extend(disc2.evidence)
    else:
        result.state = ComponentState.FAILED.value
        result.errors.append(err or f"exit {code}")
    return result


def update_tool(tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
    settings = settings or load_settings()
    if not tool.update_command:
        return OperationResult(
            operation="install.update",
            status=Status.SKIP,
            component=tool.id,
            message=f"{tool.id}: no update_command defined",
        )
    if settings.dry_run:
        return OperationResult(
            operation="install.update",
            status=Status.SKIP,
            component=tool.id,
            message=f"{tool.id}: dry_run — would run {tool.update_command}",
            data={"planned_command": tool.update_command},
        )
    code, out, err = _run(tool.update_command, timeout=settings.command_timeout_seconds)
    return OperationResult(
        operation="install.update",
        component=tool.id,
        status=Status.PASS if code == 0 else Status.FAIL,
        message=f"{tool.id}: update exit={code}",
        data={"stdout": out[:500], "stderr": err[:500]},
    )


def repair_tool(tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
    settings = settings or load_settings()
    if tool.repair_command:
        if settings.dry_run:
            return OperationResult(
                operation="install.repair",
                status=Status.SKIP,
                component=tool.id,
                message=f"{tool.id}: dry_run — would repair",
            )
        code, out, err = _run(tool.repair_command, timeout=settings.command_timeout_seconds)
        return OperationResult(
            operation="install.repair",
            component=tool.id,
            status=Status.PASS if code == 0 else Status.FAIL,
            message=f"{tool.id}: repair exit={code}",
        )
    return install_tool(tool, settings)


def apply_desired_action(
    tool: ToolManifest, state: ComponentState, settings: Optional[FrogeSettings] = None
) -> OperationResult:
    action = desired_action(state)
    if action == "KEEP":
        return OperationResult(
            operation="install.apply",
            status=Status.SKIP,
            component=tool.id,
            state=state.value,
            message=f"{tool.id}: KEEP",
        )
    if action == "INSTALL":
        return install_tool(tool, settings)
    if action == "UPDATE":
        return update_tool(tool, settings)
    if action == "REPAIR":
        return repair_tool(tool, settings)
    if action == "DIAGNOSE":
        return discover_tool(tool)
    if action == "START":
        settings = settings or load_settings()
        if tool.start_command and not settings.dry_run:
            code, out, err = _run(tool.start_command)
            return OperationResult(
                operation="install.start",
                component=tool.id,
                status=Status.PASS if code == 0 else Status.FAIL,
                message=f"{tool.id}: start exit={code}",
            )
        return OperationResult(
            operation="install.start",
            status=Status.SKIP,
            component=tool.id,
            message=f"{tool.id}: no start_command or dry_run",
        )
    return OperationResult(
        operation="install.apply",
        status=Status.SKIP,
        component=tool.id,
        message=f"{tool.id}: unhandled action {action}",
    )
