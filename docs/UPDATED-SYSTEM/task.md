# FROGE Updated Implementation Tasks

## Status legend

- ✅ COMPLETE — verified with evidence
- 🟡 IN PROGRESS — actively being implemented
- ⬜ PENDING — dependency ready, not started
- ❌ BLOCKED/FAILED — requires resolution
- 🚫 EXCLUDED — explicitly out of scope

## Phase A — Reconcile foundation

| ID | Task | Status |
|---|---|---|
| A-001 | Reconcile stale root docs with current implementation | ⬜ |
| A-002 | Verify fresh-clone install/test/CLI baseline | ⬜ |

## Phase B — Research-backed tool management

| ID | Task | Status |
|---|---|---|
| B-001 | Normalize research inventory and map each approved tool to manifest | ⬜ |
| B-002 | Implement verified adapters for approved tools, one by one | ⬜ |
| B-003 | Add functional health tests for each adapter | ⬜ |
| B-004 | Implement safe fresh-machine bootstrap path | ⬜ |

## Phase C — Automatic updates

| ID | Task | Status |
|---|---|---|
| C-001 | Version/update signal abstraction | ⬜ |
| C-002 | Research-backed update adapters | ⬜ |
| C-003 | Update planner + idempotent updater | ⬜ |
| C-004 | Post-update capability/health/regression verification | ⬜ |
| C-005 | Recovery/rollback path | ⬜ |

## Phase D — Agent coordination

| ID | Task | Status |
|---|---|---|
| D-001 | Agent registry and capability model | ⬜ |
| D-002 | Task/result envelopes and correlation IDs | ⬜ |
| D-003 | Hermes/coordinator delegation workflow | ⬜ |
| D-004 | Agent-to-agent MCP transport/control layer | ⬜ |
| D-005 | Communication integration tests and permission tests | ⬜ |

## Phase E — Skill system

| ID | Task | Status |
|---|---|---|
| E-001 | Skill registry/discovery model | ⬜ |
| E-002 | Existing-skill selection workflow | ⬜ |
| E-003 | Dedicated Skill Designer workflow | ⬜ |
| E-004 | Skill validation/publishing/versioning | ⬜ |
| E-005 | Integrate Tool Expert and Skill Expert with orchestration | ⬜ |

## Phase F — Continuous loop / harness

| ID | Task | Status |
|---|---|---|
| F-001 | Durable `.context.md` checkpoint protocol | ⬜ |
| F-002 | Continuous task loop with bounded retries | ⬜ |
| F-003 | Failure injection and recovery tests | ⬜ |
| F-004 | End-to-end build/verify/document/push loop | ⬜ |
| F-005 | Final hardening and release gate | ⬜ |

## Explicitly excluded

Ollama, vLLM, frontend/design.md, generic MCPs, Omni Router MCP, Mega MCP, and an uncontrolled large skill/plugin catalog.

## Rule

Tasks are completed only with evidence. The implementation agent must update this file, `tracker.md`, `.context.md` and relevant status documentation in the same logical change.
