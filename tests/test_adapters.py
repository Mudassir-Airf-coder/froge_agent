"""Tests for adapter abstraction."""

from froge.adapters import GenericAdapter, get_adapter
from froge.manifest import ToolManifest, default_registry
from froge.results import Status
from froge.state import ComponentState


def test_get_adapter_returns_generic():
    tool = ToolManifest(id="x", name="X")
    a = get_adapter(tool)
    assert isinstance(a, GenericAdapter)


def test_generic_discover_missing():
    tool = ToolManifest(id="nope", name="Nope", executable="froge-no-such-bin-xyz")
    r = GenericAdapter().discover(tool)
    assert r.state == ComponentState.MISSING.value


def test_generic_apply_keep():
    reg = default_registry()
    tool = reg.get("python")
    assert tool is not None
    disc = GenericAdapter().discover(tool)
    state = ComponentState.from_string(disc.state or "UNKNOWN")
    r = GenericAdapter().apply(tool, state)
    assert r.status in (Status.SKIP, Status.PASS)
