"""Tests for health verification ladder."""

from froge.health import verify_tool
from froge.manifest import ToolManifest, HealthCheckSpec
from froge.results import Status
from froge.state import ComponentState


def test_verify_python_exists():
    tool = ToolManifest(
        id="python3",
        name="Python3",
        executable="python3",
        version_command=["python3", "--version"],
        health_checks=[HealthCheckSpec(kind="version", command="python3 --version")],
    )
    result = verify_tool(tool)
    assert result.status == Status.PASS
    assert result.state in (ComponentState.INSTALLED.value, ComponentState.HEALTHY.value)
    assert "L1_existence" in result.data["levels"]
    assert result.data["levels"]["L1_existence"] == "PASS"


def test_verify_missing_tool():
    tool = ToolManifest(
        id="nope",
        name="Nope",
        executable="froge-definitely-missing-xyz",
    )
    result = verify_tool(tool)
    assert result.status == Status.FAIL
    assert result.state == ComponentState.MISSING.value


def test_verify_unknown_no_exe():
    tool = ToolManifest(id="opencode", name="OpenCode", installation_method="unknown")
    result = verify_tool(tool)
    assert result.data["levels"]["L1_existence"] == "SKIP"
