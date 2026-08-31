"""End-to-end bootstrap with a fake local tool (no external AI installs)."""

from froge.bootstrap import run_bootstrap
from froge.config import load_settings
from froge.manifest import ToolManifest, ToolRegistry, HealthCheckSpec
from froge.persistence import StateStore
from froge.results import Status


def _fake_registry(python_path: str = "python3") -> ToolRegistry:
    reg = ToolRegistry()
    reg.register(
        ToolManifest(
            id="fake-cli",
            name="Fake CLI",
            role="test",
            executable=python_path,
            version_command=[python_path, "--version"],
            installation_method="system",
            validation_status="verified",
            health_checks=[HealthCheckSpec(kind="version", command=f"{python_path} --version")],
        )
    )
    return reg


def test_e2e_bootstrap_keep_idempotent(tmp_path):
    settings = load_settings(dry_run=True, data_dir=tmp_path)
    store = StateStore(path=tmp_path / "state.json", settings=settings)
    reg = _fake_registry()
    r1 = run_bootstrap(registry=reg, settings=settings, store=store, verify=True)
    assert r1.status == Status.PASS
    r2 = run_bootstrap(registry=reg, settings=settings, store=store, verify=True)
    assert r2.status == Status.PASS
    assert r2.data["execution"][0]["planned_action"] == "KEEP"


def test_e2e_missing_tool_diagnoses(tmp_path):
    settings = load_settings(dry_run=True, data_dir=tmp_path)
    store = StateStore(path=tmp_path / "state.json", settings=settings)
    reg = ToolRegistry()
    reg.register(
        ToolManifest(
            id="ghost",
            name="Ghost",
            executable="froge-ghost-bin-xyz-999",
            installation_method="unknown",
            validation_status="requires_validation",
        )
    )
    r = run_bootstrap(registry=reg, settings=settings, store=store, verify=True)
    assert r.data["execution"][0]["planned_action"] in ("INSTALL", "DIAGNOSE")


def test_e2e_requires_validation_not_healthy(tmp_path):
    settings = load_settings(dry_run=True, data_dir=tmp_path)
    store = StateStore(path=tmp_path / "state.json", settings=settings)
    reg = ToolRegistry()
    reg.register(
        ToolManifest(
            id="opencode-fake",
            name="OpenCode Fake",
            installation_method="unknown",
            validation_status="requires_validation",
            notes="REQUIRES VALIDATION",
        )
    )
    r = run_bootstrap(registry=reg, settings=settings, store=store)
    msg = r.data["execution"][0]["message"]
    assert "REQUIRES VALIDATION" in msg or r.data["execution"][0]["planned_action"] == "DIAGNOSE"
