from froge.providers import ProviderRegistry, ProviderInfo, default_provider_registry
from froge.results import Status


def test_empty_default_registry():
    reg = default_provider_registry()
    assert len(reg.list()) == 0
    r = reg.validate()
    assert r.status == Status.PASS


def test_register_requires_validation():
    reg = ProviderRegistry()
    reg.register_info(
        ProviderInfo(id="example", name="Example", validation_status="requires_validation")
    )
    assert reg.get("example") is not None
    r = reg.validate()
    assert "example" in r.data["requires_validation"]
