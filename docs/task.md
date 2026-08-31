# FROGE Agent — Task System

**Last updated:** 2026-08-31
**Purpose:** Executable work breakdown derived from repository audit and gap analysis.
**Rule:** Every implementation task must reference this document. Status is maintained in `docs/tracker.md`.

## Status Legend

- ✅ COMPLETED
- 🟡 IN PROGRESS / PENDING
- ⬜ NOT STARTED
- ❌ FAILED / BLOCKED
- 🚫 OUT OF SCOPE (current phase)

## PHASE 0 — Repository Audit & Documentation Foundation

| ID | Title | Description | Dependencies | Status | Acceptance Criteria | Evidence Required |
|----|-------|-------------|--------------|--------|---------------------|-------------------|
| T-0-001 | Complete repository audit | Inspect every file, classify state, produce CURRENT-STATE.md and GAPS.md | None | ✅ COMPLETED | All existing files read; classification accurate; gaps recorded | CURRENT-STATE.md, GAPS.md present |
| T-0-002 | Establish living documentation set | Create flow.md, task.md, tracker.md and core architecture docs | T-0-001 | 🟡 IN PROGRESS | Documents exist, consistent, resume-capable | Files in docs/ + git commit |
| T-0-003 | Record foundational ADRs | ADR-001 to ADR-005 | T-0-001 | 🟡 PENDING | ADRs accepted and committed | docs/adr/ |
| T-0-004 | Update README to reflect reality | Remove aspirational folder claims; point to living docs | T-0-002 | ⬜ NOT STARTED | README matches actual structure + points to docs | README diff |

## PHASE 1 — Core Architecture Contracts (Documentation Only)

| ID | Title | Description | Dependencies | Status | Acceptance Criteria | Evidence Required |
|----|-------|-------------|--------------|--------|---------------------|-------------------|
| T-1-001 | Bootstrap specification | Full desired-state machine, detection, install/update/repair/verify | T-0-002 | ⬜ NOT STARTED | bootstrap.md complete with idempotency rules | docs/bootstrap.md |
| T-1-002 | Tool role definitions | Document each tool with Role / Responsibilities / Non-responsibilities / Health / etc. Mark unverified | T-0-002 | ⬜ NOT STARTED | tools.md exists; every tool has REQUIRES VALIDATION where appropriate | docs/tools.md |
| T-1-003 | Agent role contracts | Explicit contracts for runtime agents FROGE will orchestrate | T-1-002 | ⬜ NOT STARTED | agents.md with non-overlapping roles | docs/agents.md |
| T-1-004 | Provider & model architecture | Discovery, health, failover, cooldown, session continuity (mechanism TBD) | T-0-002 | ⬜ NOT STARTED | providers.md + models.md or combined | docs/providers.md |
| T-1-005 | Skills vs Plugins distinction | Clear definitions + lifecycle | T-0-002 | ⬜ NOT STARTED | skills.md + plugins.md | docs/skills.md, docs/plugins.md |
| T-1-006 | Health model | Formal vocabulary + ladder | T-0-002 | ⬜ NOT STARTED | health.md | docs/health.md |
| T-1-007 | Recovery model | Failure taxonomy + detect-classify-diagnose-repair-verify-record | T-0-002 | ⬜ NOT STARTED | recovery.md | docs/recovery.md |
| T-1-008 | Security principles | Secrets, least privilege, boundaries, audit, redaction | T-0-002 | ⬜ NOT STARTED | security.md | docs/security.md |
| T-1-009 | Testing philosophy | Layers, acceptance, evidence rule | T-0-002 | ⬜ NOT STARTED | testing.md | docs/testing.md |

## PHASE 2 — Deferred / Future (Explicitly Out of Scope Now)

| ID | Title | Status | Notes |
|----|-------|--------|-------|
| T-MCP-001 | MCP Control Plane implementation | 🚫 OUT OF SCOPE | Document boundary only |
| T-OMNI-001 | Omni Router MCP | 🚫 OUT OF SCOPE | Document future integration only |
| T-MEGA-001 | Mega MCP construction/redesign | 🚫 OUT OF SCOPE | Assume exists; interface TBD |
| T-UI-001 | Frontend / design.md | 🚫 OUT OF SCOPE | Explicitly deferred |

## PHASE 3+ — Implementation (After Documentation Foundation Accepted)

To be detailed only after Phase 0–1 documentation is validated and tracker shows foundation complete.  
Will follow: READ DOCS → READ TRACKER → SELECT NEXT TASK → IMPLEMENT → TEST → VERIFY → UPDATE DOCS/TASK/TRACKER → COMMIT.

## Task Rules

1. No task is COMPLETED without evidence.
2. Dependencies must be satisfied before starting.
3. Status changes must update tracker.md in the same commit when possible.
4. New architectural decisions require an ADR.
