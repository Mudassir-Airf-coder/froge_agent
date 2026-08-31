"""Installation engine — manifest-driven, idempotent, dry-run aware."""

from __future__ import annotations

from typing import Optional

from froge.config import FrogeSettings, load_settings
from froge.discovery import discover_executable
from froge.errors import ErrorKind
from froge.executil import run_command
from froge.manifest import ToolManifest
from froge.results import OperationResult, Status
from froge.state import ComponentState, desired_action


def discover_tool(tool: ToolManifest) -> OperationResult:
    if not tool.executable:
        return OperationResult(
            operation="install.discover",
            status=Status.SKIP,
            component=tool.id,
            state=ComponentState.UNKNOWN.value,
            message=f"{tool.id}: no executable (REQUIRES VALIDATION)",
            data={"error_kind": ErrorKind.REQUIRES_VALIDATION.value},
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
        "discovery", summary=f"{tool.id}={item.state.value}", version=item.version, path=item.path
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
            data={"error_kind": ErrorKind.REQUIRES_VALIDATION.value},
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
    exec_result = run_command(
        tool.install_command,
        timeout=settings.command_timeout_seconds,
        operation="install.install",
        component=tool.id,
    )
    if exec_result.status == Status.PASS:
        disc2 = discover_tool(tool)
        exec_result.state = disc2.state
        exec_result.evidence.extend(disc2.evidence)
        exec_result.message = f"{tool.id}: install OK → {disc2.state}"
    else:
        exec_result.state = ComponentState.FAILED.value
        if not exec_result.errors:
            exec_result.errors.append("INSTALL_FAILED")
    return exec_result


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
    return run_command(
        tool.update_command,
        timeout=settings.command_timeout_seconds,
        operation="install.update",
        component=tool.id,
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
                data={"planned_command": tool.repair_command},
            )
        return run_command(
            tool.repair_command,
            timeout=settings.command_timeout_seconds,
            operation="install.repair",
            component=tool.id,
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
            return run_command(tool.start_command, operation="install.start", component=tool.id)
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
