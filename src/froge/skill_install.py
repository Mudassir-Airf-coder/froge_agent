"""FROGE Universal Install Skill runner.

Implements the operational pipeline described in:
  skills/froge-universal-install.skill.md

Reuses discovery, planner, bootstrap, health, persistence — no parallel framework.
"""

from __future__ import annotations

from typing import Any, Optional

from froge.bootstrap import run_bootstrap
from froge.config import FrogeSettings, load_settings
from froge.discovery import discover_environment
from froge.manifest import ToolRegistry, default_registry
from froge.persistence import StateStore, load_state
from froge.planner import build_plan
from froge.results import OperationResult, Status
from froge.security import redact


SKILL_ID = "froge-universal-install"
SKILL_VERSION = "1.0.0"


def _env_snapshot(discovery: OperationResult) -> dict[str, Any]:
    items = {i["id"]: i for i in discovery.data.get("items", [])}
    return {
        "python": items.get("python") or items.get("python3"),
        "git": items.get("git"),
        "node": items.get("node"),
        "npm": items.get("npm"),
        "raw_items": discovery.data.get("items", []),
    }


def run_install_skill(
    *,
    dry_run: bool = True,
    registry: Optional[ToolRegistry] = None,
    settings: Optional[FrogeSettings] = None,
    store: Optional[StateStore] = None,
    verify: bool = True,
) -> OperationResult:
    """Execute the universal install skill pipeline.

    Always safe in dry_run=True (default). Mutation only when dry_run=False.
    """
    settings = settings or load_settings(dry_run=dry_run)
    settings = load_settings(
        dry_run=dry_run,
        data_dir=settings.data_dir,
        log_level=settings.log_level,
    )
    registry = registry or default_registry()
    store = store or load_state(settings)

    discovery = discover_environment()
    env = _env_snapshot(discovery)

    plan = build_plan(registry, settings)
    if plan.status == Status.FAIL:
        return OperationResult(
            operation="skill.install",
            status=Status.FAIL,
            message=redact(f"Plan failed: {plan.message}"),
            errors=plan.errors,
            data={
                "skill_id": SKILL_ID,
                "skill_version": SKILL_VERSION,
                "phase": "plan",
                "environment": env,
                "plan": plan.data,
            },
            evidence=plan.evidence,
        )

    boot = run_bootstrap(
        registry=registry,
        settings=settings,
        verify=verify,
        store=store,
    )

    execution = boot.data.get("execution", [])
    summary = {
        "KEEP": sum(1 for e in execution if e.get("planned_action") == "KEEP"),
        "INSTALL": sum(1 for e in execution if e.get("planned_action") == "INSTALL"),
        "UPDATE": sum(1 for e in execution if e.get("planned_action") == "UPDATE"),
        "REPAIR": sum(1 for e in execution if e.get("planned_action") == "REPAIR"),
        "DIAGNOSE": sum(1 for e in execution if e.get("planned_action") == "DIAGNOSE"),
        "FAILED": sum(1 for e in execution if e.get("result_status") == "FAIL"),
        "REQUIRES_VALIDATION": sum(
            1 for e in execution if "REQUIRES VALIDATION" in (e.get("message") or "")
        ),
    }

    if boot.status == Status.FAIL or summary["FAILED"] > 0:
        overall = "FAIL"
        status = Status.FAIL
    elif summary["REQUIRES_VALIDATION"] > 0 or (summary["INSTALL"] > 0 and dry_run):
        overall = "PARTIAL"
        status = Status.PASS
    else:
        overall = "PASS"
        status = Status.PASS

    return OperationResult(
        operation="skill.install",
        status=status,
        message=redact(
            f"[{SKILL_ID} v{SKILL_VERSION}] overall={overall} "
            f"dry_run={dry_run} keep={summary['KEEP']} "
            f"requires_validation={summary['REQUIRES_VALIDATION']} "
            f"failed={summary['FAILED']}"
        ),
        data={
            "skill_id": SKILL_ID,
            "skill_version": SKILL_VERSION,
            "overall": overall,
            "dry_run": dry_run,
            "environment": env,
            "plan": plan.data.get("steps", []),
            "order": plan.data.get("order", []),
            "execution": execution,
            "summary": summary,
            "state_path": boot.data.get("state_path"),
        },
        errors=boot.errors,
        evidence=list(discovery.evidence) + list(plan.evidence) + list(boot.evidence),
    )


def format_report(result: OperationResult) -> str:
    """Human-readable installation report."""
    lines = [
        "FROGE INSTALLATION REPORT",
        f"Skill: {result.data.get('skill_id')} v{result.data.get('skill_version')}",
        f"Overall: {result.data.get('overall')}  dry_run={result.data.get('dry_run')}",
        f"Status: {result.status.value}",
        "",
        "Environment:",
    ]
    env = result.data.get("environment") or {}
    for key in ("python", "git", "node", "npm"):
        item = env.get(key) or {}
        if isinstance(item, dict):
            lines.append(
                f"  {key}: state={item.get('state')} version={item.get('version')} path={item.get('path')}"
            )
        else:
            lines.append(f"  {key}: (not reported)")
    lines.append("")
    lines.append("Tools:")
    lines.append(f"  {'Tool':16} {'Action':10} {'Result':8} {'Verify':12} Message")
    for e in result.data.get("execution") or []:
        lines.append(
            f"  {e.get('tool_id','?'):16} {e.get('planned_action','?'):10} "
            f"{e.get('result_status','?'):8} "
            f"{str(e.get('verify_status','-'))+'/'+str(e.get('verify_state','-')):12} "
            f"{redact(e.get('message') or '')}"
        )
    lines.append("")
    s = result.data.get("summary") or {}
    lines.append(
        f"Summary: KEEP={s.get('KEEP',0)} INSTALL={s.get('INSTALL',0)} "
        f"UPDATE={s.get('UPDATE',0)} REPAIR={s.get('REPAIR',0)} "
        f"FAILED={s.get('FAILED',0)} REQUIRES_VALIDATION={s.get('REQUIRES_VALIDATION',0)}"
    )
    if result.errors:
        lines.append("Errors:")
        for err in result.errors:
            lines.append(f"  - {redact(err)}")
    return "\n".join(lines)
