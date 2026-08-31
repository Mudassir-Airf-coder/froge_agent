"""Tests for OperationResult and Evidence."""

from froge.results import Evidence, OperationResult, Status


def test_result_success():
    r = OperationResult(operation="test", status=Status.PASS, message="ok")
    assert r.is_success()
    r.add_evidence("command_output", summary="python --version", stdout="Python 3.12")
    assert len(r.evidence) == 1
    assert r.to_report_line().startswith("test: PASS")


def test_result_fail():
    r = OperationResult(operation="test", status=Status.FAIL, errors=["boom"])
    assert not r.is_success()
