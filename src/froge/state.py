"""Component lifecycle state model.

Aligned with docs/health.md and docs/bootstrap.md.
"""

from __future__ import annotations

from enum import Enum


class ComponentState(str, Enum):
    """Canonical lifecycle states for any FROGE-managed component."""

    UNKNOWN = "UNKNOWN"
    DISCOVERING = "DISCOVERING"
    MISSING = "MISSING"
    INSTALLED = "INSTALLED"
    OUTDATED = "OUTDATED"
    CONFIGURING = "CONFIGURING"
    CONFIGURED = "CONFIGURED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    BROKEN = "BROKEN"
    REPAIRING = "REPAIRING"
    FAILED = "FAILED"
    STOPPED = "STOPPED"

    @classmethod
    def from_string(cls, value: str) -> "ComponentState":
        try:
            return cls(value.upper())
        except ValueError:
            return cls.UNKNOWN


def desired_action(state: ComponentState) -> str:
    """Return the canonical action for a detected state (bootstrap.md)."""
    if state in (
        ComponentState.HEALTHY,
        ComponentState.RUNNING,
        ComponentState.CONFIGURED,
        ComponentState.INSTALLED,
    ):
        return "KEEP"
    mapping = {
        ComponentState.MISSING: "INSTALL",
        ComponentState.OUTDATED: "UPDATE",
        ComponentState.BROKEN: "REPAIR",
        ComponentState.UNKNOWN: "DIAGNOSE",
        ComponentState.FAILED: "REPAIR",
        ComponentState.DEGRADED: "REPAIR",
        ComponentState.STOPPED: "START",
        ComponentState.DISCOVERING: "DIAGNOSE",
        ComponentState.CONFIGURING: "VERIFY",
        ComponentState.STARTING: "VERIFY",
        ComponentState.REPAIRING: "VERIFY",
    }
    return mapping.get(state, "DIAGNOSE")
