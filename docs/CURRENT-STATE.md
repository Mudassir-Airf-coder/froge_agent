# FROGE Agent — Current Repository State

**Last audited:** 2026-08-31 (implementation in progress)
**Branch:** main

## Implemented (verified locally)

- `pyproject.toml` + package layout under `src/froge/`
- `ComponentState` lifecycle model (aligned with health.md / bootstrap.md)
- `OperationResult` + `Evidence` contracts
- `FrogeSettings` (defaults, env override, validation)
- `ToolManifest` schema + `ToolRegistry` with conceptual tools (REQUIRES VALIDATION for external agents)
- Environment discovery (`discover_environment`, `discover_executable`)
- CLI: `froge status | tools | doctor | version`
- 20 unit tests — all passing in sandbox

## Evidence

```
pytest tests/ -v  → 20 passed
froge status       → Registry PASS, 10 tools
froge doctor       → Discovery PASS
```

## Not yet implemented

- Installation engine
- Health / functional verification engine  
- Bootstrap orchestrator
- Provider abstraction / failover
- Agent registry runtime
- External tool adapters (all REQUIRES VALIDATION)

## Deferred (ADR)

- MCP servers, Omni Router MCP, Mega MCP redesign
- Skills catalog / plugins
- Frontend / design.md
