"""Tests for desired-state planner."""

from froge.manifest import default_registry
from froge.planner import build_plan, topological_order
from froge.results import Status


def test_topo_order_dependencies():
    reg = default_registry()
    order = topological_order(reg)
    if "npm" in order and "node" in order:
        assert order.index("node") < order.index("npm")


def test_build_plan():
    reg = default_registry()
    result = build_plan(reg)
    assert result.status == Status.PASS
    assert "steps" in result.data
    assert len(result.data["steps"]) >= 5
    actions = {s["action"] for s in result.data["steps"]}
    assert "KEEP" in actions or "DIAGNOSE" in actions or "INSTALL" in actions
