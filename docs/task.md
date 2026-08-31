# FROGE Agent — Task System

**Last updated:** 2026-08-31
**Purpose:** Executable work breakdown. Status is maintained in `docs/tracker.md`.

## Status Legend

- ✅ COMPLETED
- 🟡 IN PROGRESS / PENDING
- ⬜ NOT STARTED
- ❌ FAILED / BLOCKED
- 🚫 OUT OF SCOPE (current phase)

## PHASE 0 — Repository Audit & Documentation Foundation

| ID | Title | Status |
|----|-------|--------|
| T-0-001 | Complete repository audit | ✅ COMPLETED |
| T-0-002 | Establish living documentation set | ✅ COMPLETED |
| T-0-003 | Record foundational ADRs | ✅ COMPLETED |
| T-0-004 | Update README to reflect reality | ✅ COMPLETED |

## PHASE 1 — Core Architecture Contracts (Documentation)

| ID | Title | Status |
|----|-------|--------|
| T-1-001 … T-1-009 | Bootstrap, tools, agents, providers, skills/plugins, health, recovery, security, testing | ✅ COMPLETED (first drafts) |

## PHASE 2 — Deferred (Binding ADRs)

| ID | Title | Status |
|----|-------|--------|
| T-MCP-001 | MCP Control Plane implementation | 🚫 OUT OF SCOPE (ADR-004) |
| T-OMNI-001 | Omni Router MCP | 🚫 OUT OF SCOPE |
| T-MEGA-001 | Mega MCP construction/redesign | 🚫 OUT OF SCOPE |
| T-UI-001 | Frontend / design.md | 🚫 OUT OF SCOPE (ADR-005) |
| T-SKILL-CAT | Large skill / plugin catalog | 🚫 OUT OF SCOPE (deferred) |

## PHASE I — Implementation (Active)

See also `docs/IMPLEMENTATION-PLAN.md`.

### I-1 Project Foundation

| ID | Title | Description | Dependencies | Status | Acceptance Criteria | Evidence Required |
|----|-------|-------------|--------------|--------|---------------------|-------------------|
| I-1-001 | Project packaging & core foundation | pyproject.toml, package layout, config system, logging, result types, lifecycle state model, tool manifest schema + registry, minimal unit tests | Phase 0–1 complete | 🟡 IN PROGRESS | (1) `pyproject.toml` valid, package importable (2) config loads with defaults + env override (3) structured Result/Evidence types exist (4) ComponentState enum matches health/bootstrap vocabulary (5) ToolManifest schema validates (6) unit tests pass (7) docs/task/tracker updated | test output + import check + files on main |
| I-1-002 | CLI skeleton / entry point | Minimal `froge` CLI that can report version and run `froge status` (placeholder) | I-1-001 | ⬜ NOT STARTED | CLI invokes, version matches, exits cleanly | CLI output |

### I-2 Environment Discovery

| ID | Title | Status |
|----|-------|--------|
| I-2-001 | OS / runtime / path / version discovery | ⬜ NOT STARTED |

### I-3 Dependency Management

| ID | Title | Status |
|----|-------|--------|
| I-3-001 | Prerequisite graph + desired-state calculation | ⬜ NOT STARTED |

### I-4 Tool Installation Engine

| ID | Title | Status |
|----|-------|--------|
| I-4-001 | Installation abstraction (discover/install/update/configure/start/stop/repair) | ⬜ NOT STARTED |

### I-5 Verification / Health Engine

| ID | Title | Status |
|----|-------|--------|
| I-5-001 | Health ladder + functional test runner | ⬜ NOT STARTED |

### I-6 Bootstrap Orchestrator

| ID | Title | Status |
|----|-------|--------|
| I-6-001 | Desired-state bootstrap orchestrator (idempotent) | ⬜ NOT STARTED |

### I-7 First Tool Workflow (after research)

| ID | Title | Status |
|----|-------|--------|
| I-7-001 | CodeBuff / FreeBuff installation workflow (manifest-driven) | ⬜ NOT STARTED (blocked on research + I-4/I-5/I-6) |

### Later Implementation Phases (not yet expanded)

- Provider / Omni Router integration
- Agent registry
- Session management
- Failover + session continuity
- Knowledge integration (OHSC / Obsidian / Graphify)
- Full E2E + failure injection
- Hardening

## Task Rules

1. No task is COMPLETED without evidence.
2. Dependencies must be satisfied before starting.
3. Status changes must update tracker.md in the same commit when possible.
4. New architectural decisions require an ADR.
5. Skills catalog, plugins, new MCPs, frontend remain out of scope.
