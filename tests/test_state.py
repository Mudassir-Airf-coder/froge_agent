"""Tests for component state model."""

from froge.state import ComponentState, desired_action


def test_states_exist():
    assert ComponentState.MISSING.value == "MISSING"
    assert ComponentState.HEALTHY.value == "HEALTHY"
    assert ComponentState.BROKEN.value == "BROKEN"


def test_from_string():
    assert ComponentState.from_string("healthy") == ComponentState.HEALTHY
    assert ComponentState.from_string("bogus") == ComponentState.UNKNOWN


def test_desired_action():
    assert desired_action(ComponentState.MISSING) == "INSTALL"
    assert desired_action(ComponentState.OUTDATED) == "UPDATE"
    assert desired_action(ComponentState.BROKEN) == "REPAIR"
    assert desired_action(ComponentState.HEALTHY) == "KEEP"
    assert desired_action(ComponentState.UNKNOWN) == "DIAGNOSE"
