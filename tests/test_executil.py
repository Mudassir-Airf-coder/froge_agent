from froge.executil import run_command
from froge.results import Status


def test_run_python_version():
    r = run_command(["python3", "--version"])
    assert r.status == Status.PASS
    assert r.data["exit_code"] == 0


def test_run_missing_command():
    r = run_command(["froge-no-such-binary-xyz"])
    assert r.status == Status.FAIL
    assert r.data.get("error_kind") == "COMMAND_NOT_FOUND"


def test_empty_command():
    r = run_command([])
    assert r.status == Status.FAIL
