"""Central configuration system.

Defaults + schema + environment overrides + validation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class FrogeSettings(BaseSettings):
    """FROGE system configuration.

    Environment variables are prefixed with FROGE_.
    Example: FROGE_LOG_LEVEL=DEBUG
    """

    model_config = SettingsConfigDict(
        env_prefix="FROGE_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    log_level: str = Field(default="INFO", description="Logging level")
    data_dir: Path = Field(
        default_factory=lambda: Path.home() / ".froge",
        description="Base directory for FROGE state and data",
    )
    manifest_path: Optional[Path] = Field(
        default=None,
        description="Path to tool manifest YAML/JSON. None = built-in defaults.",
    )
    dry_run: bool = Field(default=False, description="If true, plan but do not mutate")
    max_retries: int = Field(default=3, ge=0, le=20)
    command_timeout_seconds: int = Field(default=120, ge=5, le=3600)
    allow_destructive: bool = Field(
        default=False,
        description="Must be true to permit destructive operations",
    )

    def ensure_data_dir(self) -> Path:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        return self.data_dir


def load_settings(**overrides: Any) -> FrogeSettings:
    """Load settings with optional programmatic overrides."""
    return FrogeSettings(**overrides)
