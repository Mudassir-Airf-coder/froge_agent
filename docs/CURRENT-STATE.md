# FROGE Agent — Current Repository State

**Last updated:** 2026-08-31

## Implemented & Verified (local evidence)

| Component | Status | Evidence |
|-----------|--------|----------|
| Packaging (`pyproject.toml`) | COMPLETE | present |
| Config (`FrogeSettings`, env override) | COMPLETE | 3 tests |
| State model (`ComponentState`, `desired_action`) | COMPLETE | 3 tests |
| Results (`OperationResult`, `Evidence`) | COMPLETE | 2 tests |
| Manifest + Registry | COMPLETE | 6 tests |
| Environment discovery | COMPLETE | 3 tests + `froge doctor` |
| Health verification ladder (L1–L6) | COMPLETE | 3 tests |
| Installation engine (discover/install/update/repair/apply) | COMPLETE | used by bootstrap |
| Desired-state planner | COMPLETE | 2 tests |
| Bootstrap orchestrator | COMPLETE | 2 tests + CLI |
| CLI: status, tools, doctor, plan, bootstrap | COMPLETE | 5 tests |
| Unit tests | **29 passed** | `pytest tests/ -v` |

### Functional CLI evidence

```
froge status     → Registry PASS, 11 tools
froge plan       → system tools KEEP; external DIAGNOSE (REQUIRES VALIDATION)
froge bootstrap --dry-run → PASS; keep=4; install_attempted=0; requires_validation=7
```

## Idempotency

Second dry-run bootstrap produces identical KEEP set for system tools.

## Not yet complete

- Concrete install adapters for external tools (OpenCode, Hermes, etc.) — **REQUIRES VALIDATION** (no invented commands)
- Real gateway/service health for tools that expose them
- Provider abstraction / failover (foundation only)
- Agent registry runtime
- Windows-specific package managers (winget/choco) adapters

## Explicitly deferred

- MCP servers / Omni Router MCP / Mega MCP redesign
- Skills catalog / plugins
- Frontend / design.md
- Ollama / vLLM
