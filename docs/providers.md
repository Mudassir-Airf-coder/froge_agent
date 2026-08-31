# FROGE Provider & Model Architecture

**Status:** FOUNDATION IMPLEMENTED (interfaces only)  
**Last updated:** 2026-09-01

## Separation of Concerns

```
Agent → Provider → Model
```

Bootstrap/install engine remains decoupled from providers.

## Implemented

- `src/froge/providers.py`
  - `ModelInfo`, `ProviderInfo` models
  - `Provider` protocol
  - `ProviderRegistry` (in-memory)
  - `default_provider_registry()` — empty by design

## Not implemented

- Concrete providers
- Authentication
- Model discovery against live APIs
- Failover / cooldowns
- Omni Router MCP

## Explicit Restriction

Omni Router MCP, Ollama, vLLM, and any concrete provider backends remain **out of scope** until verified.

## Related

- docs/recovery.md
- docs/health.md
- ADR-004 (MCP deferred)
