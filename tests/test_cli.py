"""CLI smoke tests."""

from froge.cli import main


def test_version():
    assert main(["version"]) == 0


def test_status():
    assert main(["status"]) == 0


def test_doctor():
    assert main(["doctor"]) == 0


def test_plan():
    assert main(["plan"]) == 0


def test_bootstrap_dry_run():
    assert main(["bootstrap", "--dry-run"]) == 0
