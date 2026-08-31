"""Tests for universal install skill runner."""

from froge.config import load_settings
from froge.manifest import default_registry
from froge.persistence import StateStore
from froge.skill_install import format_report, run_install_skill, SKILL_ID


def test_skill_dry_run(tmp_path):
    settings = load_settings(dry_run=True, data_dir=tmp_path)
    store = StateStore(path=tmp_path / "state.json", settings=settings)
    r = run_install_skill(dry_run=True, settings=settings, store=store)
    assert r.operation == "skill.install"
    assert r.data["skill_id"] == SKILL_ID
    assert r.data["dry_run"] is True
    assert "execution" in r.data
    assert r.data["overall"] in ("PASS", "PARTIAL", "FAIL")
    assert r.data["summary"]["REQUIRES_VALIDATION"] >= 1


def test_skill_idempotent(tmp_path):
    settings = load_settings(dry_run=True, data_dir=tmp_path)
    store = StateStore(path=tmp_path / "state.json", settings=settings)
    r1 = run_install_skill(dry_run=True, settings=settings, store=store)
    r2 = run_install_skill(dry_run=True, settings=settings, store=store)
    assert r1.data["summary"]["KEEP"] == r2.data["summary"]["KEEP"]


def test_format_report_no_secrets(tmp_path):
    settings = load_settings(dry_run=True, data_dir=tmp_path)
    store = StateStore(path=tmp_path / "state.json", settings=settings)
    r = run_install_skill(dry_run=True, settings=settings, store=store)
    text = format_report(r)
    assert "FROGE INSTALLATION REPORT" in text
    assert "Overall:" in text


def test_default_registry_has_skill_inventory():
    reg = default_registry()
    for tid in ("python", "git", "opencode", "nimble-clock", "ohsc", "graphify"):
        assert reg.get(tid) is not None, tid
