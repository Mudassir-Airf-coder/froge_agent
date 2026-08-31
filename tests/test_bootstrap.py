"""Tests for bootstrap orchestrator — idempotency and dry-run."""

from froge.bootstrap import run_bootstrap
from froge.config import load_settings
from froge.results import Status


def test_bootstrap_dry_run():
    settings = load_settings(dry_run=True)
    result = run_bootstrap(settings=settings)
    assert result.operation == "bootstrap.run"
    assert "execution" in result.data
    assert result.data["dry_run"] is True
    assert result.status in (Status.PASS, Status.FAIL)


def test_bootstrap_idempotent_second_run():
    settings = load_settings(dry_run=True)
    r1 = run_bootstrap(settings=settings)
    r2 = run_bootstrap(settings=settings)
    assert len(r1.data["execution"]) == len(r2.data["execution"])
    keeps1 = [e for e in r1.data["execution"] if e["planned_action"] == "KEEP"]
    keeps2 = [e for e in r2.data["execution"] if e["planned_action"] == "KEEP"]
    assert len(keeps1) == len(keeps2)
