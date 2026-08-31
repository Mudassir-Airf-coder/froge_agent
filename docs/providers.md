# FROGE Provider & Model Architecture

**Status:** DOCUMENTED ONLY (high-level)  
**Last updated:** 2026-08-31

## Separation of Concerns

```
Agent
  ↓
Provider
  ↓
Model
```

The orchestrator must not hard-code provider-specific behavior. Providers and models belong behind adapters / a registry.

## Target Capabilities

- Provider discovery
- Authentication (secure)
- Model discovery (including free-model discovery where applicable)
- Provider health
- Model health (listing ≠ usable)
- Failure classification
- Failover to verified alternative
- Cooldowns
- Model-health memory (successful recovery choices remembered)
- Same-session continuity (mechanism **TBD**)

## Current Reality

Only high-level mentions exist in architecture and orchestrator documents. No registry, no adapters, no health implementation.

## Explicit Restriction

Omni Router MCP and any concrete provider implementation are **out of scope** for the current documentation-foundation phase. Only the architectural boundary is recorded here.

## Related

- docs/recovery.md
- docs/health.md
- ORCHESTRATOR.md
