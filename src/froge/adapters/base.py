"""Base tool adapter interface.

Adapters implement tool-specific discover/install/update/configure/start/stop/repair.
Unverified external tools return REQUIRES_VALIDATION without inventing commands.
"""

from __future__ import annotations

from typing import Optional, Protocol

from froge.config import FrogeSettings
from froge.installer import (
    apply_desired_action,
    discover_tool,
    install_tool,
    repair_tool,
    update_tool,
)
from froge.manifest import ToolManifest
from froge.results import OperationResult
from froge.state import ComponentState


class ToolAdapter(Protocol):
    def discover(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult: ...
    def install(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult: ...
    def update(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult: ...
    def repair(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult: ...
    def apply(self, tool: ToolManifest, state: ComponentState, settings: Optional[FrogeSettings] = None) -> OperationResult: ...


class GenericAdapter:
    """Default adapter driven entirely by ToolManifest fields."""

    def discover(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
        return discover_tool(tool)

    def install(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
        return install_tool(tool, settings)

    def update(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
        return update_tool(tool, settings)

    def repair(self, tool: ToolManifest, settings: Optional[FrogeSettings] = None) -> OperationResult:
        return repair_tool(tool, settings)

    def apply(
        self, tool: ToolManifest, state: ComponentState, settings: Optional[FrogeSettings] = None
    ) -> OperationResult:
        return apply_desired_action(tool, state, settings)


_DEFAULT = GenericAdapter()


def get_adapter(tool: ToolManifest) -> GenericAdapter:
    """Resolve adapter for a tool. Currently always GenericAdapter.

    Future: register per-tool adapters when installation is verified.
    """
    return _DEFAULT
