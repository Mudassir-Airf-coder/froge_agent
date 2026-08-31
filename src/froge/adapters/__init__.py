"""Tool adapter package — tool-specific behavior lives here, not in the core engine."""

from froge.adapters.base import ToolAdapter, GenericAdapter, get_adapter

__all__ = ["ToolAdapter", "GenericAdapter", "get_adapter"]
