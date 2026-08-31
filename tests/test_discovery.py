"""Tests for environment discovery."""

from froge.discovery import discover_executable, discover_environment
from froge.results import Status
from froge.state import ComponentState


def test_discover_python():
    item = discover_executable("python3", ["--version"])
    assert item.state in (ComponentState.INSTALLED, ComponentState.BROKEN)
    if item.state == ComponentState.INSTALLED:
        assert item.path is not None
        assert item.version is not None


def test_discover_missing():
    item = discover_executable("froge-nonexistent-binary-xyz", ["--version"])
    assert item.state == ComponentState.MISSING
    assert item.path is None


def test_discover_environment():
    result = discover_environment()
    assert result.operation == "discovery.environment"
    assert "items" in result.data
    assert len(result.data["items"]) >= 5
    assert len(result.evidence) >= 5
