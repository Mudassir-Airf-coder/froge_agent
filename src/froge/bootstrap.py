"""Bootstrap orchestrator — discover → plan → execute → verify → report."""

from __future__ import annotations

from typing import Optional

from froge.config import FrogeSettings, load_settings
from froge.health import verify_tool
from froge.installer import apply_desired_action
from froge.manifest import ToolRegistry, default_registry
from froge.planner import build_plan
from froge.results import OperationResult, Status
from froge.state import ComponentState


def run_bootstrap(
    registry: Optional[ToolRegistry] = None,
    settings: Optional[FrogeSettings] = None,
    tool_ids: Optional[list[str]] = None,
    verify: bool = True,
) -> OperationResult:
    """Execute full bootstrap cycle with evidence."""
    settings = settings or load_settings()
    registry = registry or default_registry()

    plan_result = build_plan(registry, settings, tool_ids)
    steps = plan_result.data.get("steps", [])
    order = plan_result.data.get("order", [])

    execution_results: list[dict] = []
    overall = Status.PASS
    errors: list[str] = []

    for step in steps:
        tid = step["tool_id"]
        tool = registry.get(tid)
        if tool is None:
            continue
        state = ComponentState.from_string(step["current_state"])
        action_result = apply_desired_action(tool, state, settings)
        entry = {
            "tool_id": tid,
            "planned_action": step["action"],
            "result_status": action_result.status.value,
            "result_state": action_result.state,
            "message": action_result.message,
        }

        if verify and action_result.status in (Status.PASS, Status.SKIP):
            if tool.executable:
                v = verify_tool(tool)
                entry["verify_status"] = v.status.value
                entry["verify_state"] = v.state
                entry["verify_levels"] = v.data.get("levels", {})
                if v.status == Status.FAIL:
                    overall = Status.FAIL
                    errors.append(f"{tid}: verification failed")
            else:
                entry["verify_status"] = "SKIP"
                entry["verify_state"] = "UNKNOWN"

        if action_result.status == Status.FAIL:
            overall = Status.FAIL
            errors.extend(action_result.errors or [action_result.message])

        execution_results.append(entry)

    keep = sum(1 for e in execution_results if e["planned_action"] == "KEEP")
    installed = sum(1 for e in execution_results if e["planned_action"] == "INSTALL")
    skipped_unknown = sum(
        1 for e in execution_results if "REQUIRES VALIDATION" in (e.get("message") or "")
    )

    report = OperationResult(
        operation="bootstrap.run",
        status=overall,
        message=(
            f"Bootstrap complete: tools={len(execution_results)} "
            f"keep={keep} install_attempted={installed} "
            f"requires_validation={skipped_unknown} dry_run={settings.dry_run}"
        ),
        data={
            "plan": steps,
            "order": order,
            "execution": execution_results,
            "dry_run": settings.dry_run,
            "summary": {
                "total": len(execution_results),
                "keep": keep,
                "install_attempted": installed,
                "requires_validation": skipped_unknown,
            },
        },
        errors=errors,
    )
    report.evidence.extend(plan_result.evidence)
    return report
