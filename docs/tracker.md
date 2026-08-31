# FROGE Agent — Live Tracker

**Last updated:** 2026-08-31

## Snapshot

| Item | Value |
|------|-------|
| Status | Bootstrap engine + persistence + adapters COMPLETE |
| Tests | **44 passed** |
| CLI | status, tools, doctor, plan, bootstrap, state, verify (+ --json) |
| Idempotency | verified |
| Persistence | `.froge/state.json` atomic writes |

## Board

- 🟢 Foundation
- 🟢 Discovery
- 🟢 Manifest + registry
- 🟢 Installation engine
- 🟢 Health ladder
- 🟢 Planner + cycle detection
- 🟢 Bootstrap orchestrator
- 🟢 Persistent state store
- 🟢 Adapter abstraction
- 🟢 CLI state / verify / --json
- 🟢 E2E fake-tool tests
- ⬜ Concrete external tool adapters (REQUIRES VALIDATION)
- ⬜ Windows winget/choco adapters (when verified)
- ⬜ Provider/failover foundation expansion
- 🚫 MCP / skills / plugins / frontend / Ollama / vLLM

## Evidence

- pytest: 44 passed
- froge status/plan/bootstrap/state/verify: PASS
- No invented external install commands
