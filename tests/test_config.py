"""Tests for configuration system."""

from froge.config import FrogeSettings, load_settings


def test_defaults():
    s = load_settings()
    assert s.log_level == "INFO"
    assert s.dry_run is False
    assert s.max_retries == 3
    assert s.allow_destructive is False


def test_env_override(monkeypatch):
    monkeypatch.setenv("FROGE_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("FROGE_DRY_RUN", "true")
    s = load_settings()
    assert s.log_level == "DEBUG"
    assert s.dry_run is True


def test_programmatic_override():
    s = load_settings(log_level="WARNING", dry_run=True)
    assert s.log_level == "WARNING"
    assert s.dry_run is True
