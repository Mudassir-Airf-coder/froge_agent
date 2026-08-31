"""Installation failure, repair, and KEEP paths using safe fakes."""

from froge.config import load_settings
from froge.installer import apply_desired_action, install_tool, repair_tool
from froge.manifest import ToolManifest
from froge.results import Status
from froge.state import ComponentState


def test_install_requires_validation():
    tool = ToolManifest(
        id="ghost",
        name="Ghost",
        installation_method="unknown",
        validation_status="requires_validation",
    )
    r = install_tool(tool, load_settings(dry_run=False))
    assert r.status == Status.SKIP
    assert "REQUIRES VALIDATION" in r.message


def test_install_dry_run_with_command():
    tool = ToolManifest(
        id="fake",
        name="Fake",
        executable="python3",
        install_command=["echo", "install-fake"],
        installation_method="script",
        validation_status="verified",
    )
    r = install_tool(tool, load_settings(dry_run=True))
    assert r.status == Status.SKIP


def test_repair_dry_run():
    tool = ToolManifest(
        id="fake",
        name="Fake",
        repair_command=["echo", "repair"],
        installation_method="script",
    )
    r = repair_tool(tool, load_settings(dry_run=True))
    assert r.status == Status.SKIP
    assert "dry_run" in r.message


def test_apply_keep():
    tool = ToolManifest(id="x", name="X", executable="python3")
    r = apply_desired_action(tool, ComponentState.INSTALLED)
    assert r.status == Status.SKIP
    assert "KEEP" in r.message


def test_apply_repair():
    tool = ToolManifest(
        id="x",
        name="X",
        repair_command=["echo", "ok"],
        installation_method="script",
    )
    r = apply_desired_action(tool, ComponentState.BROKEN, load_settings(dry_run=True))
    assert r.status == Status.SKIP
