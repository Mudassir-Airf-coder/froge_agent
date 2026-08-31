"""Desired-state planner — deterministic plan generation + cycle detection."""

from __future__ import annotations

from typing import Optional

from froge.config import FrogeSettings, load_settings
from froge.installer import discover_tool
from froge.manifest import ToolRegistry
from froge.results import OperationResult, Status
from froge.state import ComponentState, desired_action


class PlanStep:
    def __init__(self, tool_id: str, action: str, state: str, reason: str = ""):
        self.tool_id = tool_id
        self.action = action
        self.state = state
        self.reason = reason

    def to_dict(self) -> dict:
        return {
            "tool_id": self.tool_id,
            "action": self.action,
            "current_state": self.state,
            "reason": self.reason,
        }


def detect_cycles(registry: ToolRegistry, tool_ids: Optional[list[str]] = None) -> list[list[str]]:
    """Return list of dependency cycles."""
    tools = {t.id: t for t in registry.list(enabled_only=True)}
    if tool_ids:
        tools = {k: v for k, v in tools.items() if k in tool_ids}

    WHITE, GRAY, BLACK = 0, 1, 2
    color = {tid: WHITE for tid in tools}
    cycles: list[list[str]] = []
    path: list[str] = []

    def dfs(tid: str) -> None:
        color[tid] = GRAY
        path.append(tid)
        t = tools.get(tid)
        if t:
            for dep in t.dependencies:
                if dep not in tools:
                    continue
                if color[dep] == GRAY:
                    idx = path.index(dep)
                    cycles.append(path[idx:] + [dep])
                elif color[dep] == WHITE:
                    dfs(dep)
        path.pop()
        color[tid] = BLACK

    for tid in tools:
        if color[tid] == WHITE:
            dfs(tid)
    return cycles


def topological_order(registry: ToolRegistry, tool_ids: Optional[list[str]] = None) -> list[str]:
    """Dependency-aware ordering. Raises ValueError on cycle."""
    cycles = detect_cycles(registry, tool_ids)
    if cycles:
        raise ValueError(f"Dependency cycle(s) detected: {cycles}")

    tools = {t.id: t for t in registry.list(enabled_only=True)}
    if tool_ids:
        tools = {k: v for k, v in tools.items() if k in tool_ids}

    visited: set[str] = set()
    order: list[str] = []

    def visit(tid: str) -> None:
        if tid in visited:
            return
        visited.add(tid)
        t = tools.get(tid)
        if t:
            for dep in t.dependencies:
                if dep in tools:
                    visit(dep)
        if tid in tools:
            order.append(tid)

    for tid in sorted(tools.keys()):
        visit(tid)
    return order


def build_plan(
    registry: ToolRegistry,
    settings: Optional[FrogeSettings] = None,
    tool_ids: Optional[list[str]] = None,
) -> OperationResult:
    settings = settings or load_settings()
    cycles = detect_cycles(registry, tool_ids)
    if cycles:
        return OperationResult(
            operation="planner.build",
            status=Status.FAIL,
            message=f"Dependency cycle(s) detected: {cycles}",
            errors=[f"cycle: {' -> '.join(c)}" for c in cycles],
            data={"cycles": cycles},
        )

    order = topological_order(registry, tool_ids)
    steps: list[dict] = []
    results_evidence = []

    for tid in order:
        tool = registry.get(tid)
        if tool is None:
            continue
        disc = discover_tool(tool)
        state = ComponentState.from_string(disc.state or "UNKNOWN")
        action = desired_action(state)
        step = PlanStep(tid, action, state.value, reason=disc.message)
        steps.append(step.to_dict())
        results_evidence.extend(disc.evidence)

    mutating = [s for s in steps if s["action"] not in ("KEEP", "DIAGNOSE")]
    return OperationResult(
        operation="planner.build",
        status=Status.PASS,
        message=f"Plan: {len(steps)} tools, {len(mutating)} mutating actions, dry_run={settings.dry_run}",
        data={
            "steps": steps,
            "order": order,
            "mutating_count": len(mutating),
            "dry_run": settings.dry_run,
            "cycles": [],
        },
        evidence=results_evidence,
    )
