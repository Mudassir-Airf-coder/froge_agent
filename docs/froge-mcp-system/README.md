# FROGE MCP System Specification

This documentation defines the target product and implementation contract for FROGE MCP: a reusable MCP communication/control layer that allows Hermes to connect to, discover, authenticate with, and dispatch work to a controlled ecosystem of external tools and agent runtimes.

## Source of truth

The research archive under `research/` is the evidence base. Claims marked `[UNKNOWN]` or `[INFERRED]` in research are not treated as implemented facts. A tool becomes an executable integration only after installation, version, connection, functional task, result capture, and failure behavior are verified.

## Product goal

FROGE MCP must let Hermes remain the master orchestrator while FROGE provides a stable MCP communication and control surface for supported tools.

```text
USER
  ↓
HERMES (master/orchestrator)
  ↓ MCP
FROGE MCP (communication + control bridge)
  ↓ adapters / controlled execution
SUPPORTED TOOLS
  ↓
real task/result
```

FROGE is not a second master agent, model router, marketplace, planner, or autonomous product orchestrator.

## Target outcome

A user installs FROGE with one supported command, starts it, receives a runtime endpoint and authentication token, connects Hermes, and then Hermes can use FROGE capabilities to work with verified tool adapters.

The system must be evidence-first: no adapter, capability, or compatibility claim is promoted from research to `VERIFIED` without a real test.

## Documents

- `01-product-scope.md` — goals, non-goals, acceptance criteria.
- `02-architecture.md` — system boundaries and component responsibilities.
- `03-tool-integration-spec.md` — adapter contract and capability model.
- `04-hermes-integration.md` — Hermes connection, skill, session and dispatch model.
- `05-installer-and-lifecycle.md` — one-line install, start, update, reinstall and lifecycle requirements.
- `06-security-model.md` — authentication, authorization, process and filesystem controls.
- `07-tool-capability-matrix.md` — current research-derived integration status.
- `08-api-and-protocol-contract.md` — FROGE MCP control-plane contract.
- `09-verification-and-release.md` — test gates and release criteria.
- `10-implementation-phases.md` — implementation sequence from current state to target state.
- `DECISIONS.md` — architectural decisions that must not be silently changed.

## Current state

The existing FROGE MCP core has been reported as locally functional with CLI, authentication, user-scoped configuration, package build, and 50/50 tests passing. Remote installer, clean-machine installation, idempotency, and real external-tool integrations remain verification work rather than assumed capabilities.

## Important distinction

`FROGE MCP core complete` does not mean `FROGE ecosystem integration complete`.

The target product is complete only when the core, adapter framework, Hermes connection, installer, and required real tool integrations have all passed their respective evidence gates.
