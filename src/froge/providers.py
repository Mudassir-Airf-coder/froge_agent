"""Provider abstraction foundation — interfaces only, no MCP, no invented providers."""

from __future__ import annotations

from typing import Optional, Protocol

from pydantic import BaseModel, Field

from froge.results import OperationResult, Status


class ModelInfo(BaseModel):
    id: str
    name: str = ""
    provider_id: str = ""
    capabilities: list[str] = Field(default_factory=list)
    available: bool = False
    notes: str = ""


class ProviderInfo(BaseModel):
    id: str
    name: str
    kind: str = Field(default="unknown", description="api|local|router|unknown")
    models: list[ModelInfo] = Field(default_factory=list)
    healthy: bool = False
    validation_status: str = Field(
        default="requires_validation",
        description="verified|requires_validation|unknown",
    )
    notes: str = ""


class Provider(Protocol):
    @property
    def id(self) -> str: ...

    def discover_models(self) -> OperationResult: ...

    def health(self) -> OperationResult: ...


class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, ProviderInfo] = {}

    def register_info(self, info: ProviderInfo) -> None:
        self._providers[info.id] = info

    def get(self, provider_id: str) -> Optional[ProviderInfo]:
        return self._providers.get(provider_id)

    def list(self) -> list[ProviderInfo]:
        return sorted(self._providers.values(), key=lambda p: p.id)

    def validate(self) -> OperationResult:
        errors = []
        for p in self._providers.values():
            if p.validation_status == "requires_validation":
                errors.append(f"{p.id}: REQUIRES_VALIDATION")
        return OperationResult(
            operation="providers.validate",
            status=Status.PASS,
            message=(
                f"{len(self._providers)} provider(s) registered, "
                f"{sum(1 for p in self._providers.values() if p.validation_status == 'verified')} verified"
            ),
            data={
                "count": len(self._providers),
                "requires_validation": [
                    p.id for p in self._providers.values() if p.validation_status != "verified"
                ],
            },
            errors=errors,
        )


def default_provider_registry() -> ProviderRegistry:
    """Empty by design — concrete providers added only after verification."""
    return ProviderRegistry()
