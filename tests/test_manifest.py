"""Tests for tool manifest and registry."""

from froge.manifest import ToolManifest, ToolRegistry, default_registry
from froge.results import Status
from froge.state import ComponentState


def test_manifest_validation():
    t = ToolManifest(id="demo", name="Demo Tool")
    assert t.id == "demo"
    assert t.enabled is True
    assert t.status == ComponentState.UNKNOWN


def test_id_normalization():
    t = ToolManifest(id="My Tool", name="X")
    assert t.id == "my-tool"


def test_registry_register_get_list():
    reg = ToolRegistry()
    t = ToolManifest(id="python", name="Python", required=True)
    reg.register(t)
    assert len(reg) == 1
    assert reg.get("python") is t
    assert reg.list()[0].id == "python"


def test_registry_enable_disable():
    reg = ToolRegistry()
    reg.register(ToolManifest(id="x", name="X"))
    assert reg.disable("x") is True
    assert reg.get("x").enabled is False
    assert reg.enable("x") is True


def test_default_registry_has_conceptual_tools():
    reg = default_registry()
    assert len(reg) >= 8
    assert reg.get("python") is not None
    assert reg.get("opencode") is not None
    assert "REQUIRES VALIDATION" in (reg.get("opencode").notes or "")


def test_registry_validate_pass():
    reg = default_registry()
    result = reg.validate()
    assert result.status == Status.PASS
