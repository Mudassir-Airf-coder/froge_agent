# Architectural Decisions

## D001 — Hermes remains master

Hermes is the top-level orchestrator. FROGE is not a replacement orchestrator.

## D002 — FROGE is a communication/control bridge

FROGE provides stable MCP communication, capability discovery, routing to adapters, controlled execution, status and result normalization.

## D003 — Tool-specific behavior belongs behind adapters

The core must not contain product-specific command logic for every tool. Adapters isolate tool-specific interfaces and security policies.

## D004 — Research is not verification

`[UNKNOWN]` and `[INFERRED]` research claims must remain explicitly labeled until tested.

## D005 — No permanent runtime credential by default

The runtime token is treated as a credential for the active runtime/session. A long-lived permanent secret is not the default design.

## D006 — Security controls are preserved

FROGE must not bypass a worker's sandbox, permission, approval, or authentication model merely to make automation easier.

## D007 — OmniRoute remains separate

OmniRoute is a model/API routing layer. Its integration does not turn FROGE into a model router.

## D008 — Windows is the primary distribution target

Installation, PATH, clean-machine and lifecycle acceptance tests are required for the intended Windows-first release.

## D009 — No fake success

A failed, unsupported, unknown or unverified operation must be reported as such. The system must never convert uncertainty into a success claim.
