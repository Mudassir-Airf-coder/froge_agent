"""Tests for persistent state store."""

from froge.config import load_settings
from froge.persistence import StateStore


def test_atomic_save_and_load(tmp_path):
    path = tmp_path / "state.json"
    store = StateStore(path=path, settings=load_settings(data_dir=tmp_path))
    store.set_component("python", state="INSTALLED", version="3.12")
    assert path.exists()
    store2 = StateStore(path=path, settings=load_settings(data_dir=tmp_path))
    c = store2.get_component("python")
    assert c["state"] == "INSTALLED"
    assert c["version"] == "3.12"


def test_record_operation(tmp_path):
    path = tmp_path / "state.json"
    store = StateStore(path=path, settings=load_settings(data_dir=tmp_path))
    store.record_operation("bootstrap", "git", "KEEP", "SKIP", "INSTALLED", "INSTALLED", "ok")
    ops = store.list_operations()
    assert len(ops) == 1
    assert ops[0]["component"] == "git"


def test_record_verification(tmp_path):
    path = tmp_path / "state.json"
    store = StateStore(path=path, settings=load_settings(data_dir=tmp_path))
    store.record_verification("python", "PASS", "INSTALLED", {"L1_existence": "PASS"})
    c = store.get_component("python")
    assert c["last_verification_status"] == "PASS"


def test_corrupt_state_recovers(tmp_path):
    path = tmp_path / "state.json"
    path.write_text("{not valid json", encoding="utf-8")
    store = StateStore(path=path, settings=load_settings(data_dir=tmp_path))
    assert store.summary()["component_count"] == 0
