"""CLI smoke tests."""

from froge.cli import main


def test_version():
    assert main(["version"]) == 0


def test_status():
    assert main(["status"]) == 0


def test_doctor():
    assert main(["doctor"]) == 0
