# FROGE Roadmap

**Last updated:** 2026-08-31

## Stage 0 — Foundation (Documentation)

- [x] Repository created
- [x] Initial vision & architecture documents
- [x] Orchestrator contract
- [x] Agent operating contract
- [x] Full repository audit (CURRENT-STATE.md, GAPS.md)
- [x] Living documents introduced (flow.md, task.md, tracker.md)
- [x] Core architecture contracts drafted (bootstrap, tools, agents, health, recovery, security, testing, providers, skills, plugins)
- [x] Foundational ADRs (001–005)
- [ ] README fully aligned and remaining Phase-1 polish
- [ ] Documentation foundation declared complete (tracker green for Phase 0)

## Stage 1 — Core Control Plane (Future Implementation)

- [ ] Typed configuration
- [ ] Capability registry
- [ ] Provider registry
- [ ] Model registry
- [ ] Tool registry
- [ ] Session manager
- [ ] Policy engine

## Stage 2 — MCP Control Plane (Deferred)

- [ ] MCP server architecture
- [ ] MCP client/transport layer
- [ ] Tool discovery, health, permissions, lifecycle

**Note:** Explicitly out of scope until ADR-004 is revisited.

## Stage 3 — Orchestration

- [ ] Intent resolver, planner, router, execution engine, result validator

## Stage 4 — Context, Memory & Knowledge

- [ ] Active session context
- [ ] Persistent operational memory
- [ ] Retrieval & evidence tracking
- [ ] Knowledge-graph integration (future)

## Stage 5 — Self-Healing

- [ ] Error taxonomy (see recovery.md)
- [ ] Provider/model health scoring
- [ ] Verified fallback, retry, cooldown
- [ ] Same-session recovery (mechanism TBD)
- [ ] Recovery-memory learning

## Stage 6 — Verification

- [ ] Unit, contract, integration, E2E, failure-injection, regression suites

## Stage 7 — Operational Release

- [ ] Bootstrap/install flow (implementation of bootstrap.md)
- [ ] Diagnostics CLI
- [ ] Observability
- [ ] Secure local configuration
- [ ] Release documentation

## Source of Truth for Day-to-Day Progress

Use `docs/tracker.md` and `docs/task.md`. This roadmap is the high-level view.
