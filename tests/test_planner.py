"""Tests for desired-state planner including cycle detection."""

from froge.manifest import ToolManifest, ToolRegistry, default_registry
from froge.planner import build_plan, detect_cycles, topological_order
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


def test_detect_cycle():
    reg = ToolRegistry()
    reg.register(ToolManifest(id="a", name="A", dependencies=["b"]))
    reg.register(ToolManifest(id="b", name="B", dependencies=["a"]))
    cycles = detect_cycles(reg)
    assert len(cycles) >= 1


def test_build_plan_fails_on_cycle():
    reg = ToolRegistry()
    reg.register(ToolManifest(id="a", name="A", dependencies=["b"]))
    reg.register(ToolManifest(id="b", name="B", dependencies=["a"]))
    result = build_plan(reg)
    assert result.status == Status.FAIL
    assert result.data.get("cycles")
