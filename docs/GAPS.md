# FROGE Agent — Gap Analysis

**Last updated:** 2026-08-31

## Legend

- **MISSING** — Required for target architecture, does not exist
- **PARTIAL** — Some documentation or stub exists
- **INCONSISTENT** — Conflicts between documents or reality
- **UNVERIFIED** — Claimed or assumed but not confirmed against real tools
- **DUPLICATED** — Overlapping descriptions without clear ownership
- **BLOCKED** — Cannot proceed without external dependency or decision
- **DEFERRED** — Explicitly out of current phase

## Gaps

### 1. Bootstrap / Machine Preparation
- **Status:** MISSING
- **Why it matters:** First stage of the target lifecycle; without it FROGE cannot prepare a machine idempotently.
- **Current state:** Zero code or detailed specification.
- **Desired state:** Documented desired-state machine (MISSING → INSTALL, OUTDATED → UPDATE, BROKEN → REPAIR, CURRENT → VERIFY) with verification evidence.
- **Recommended task:** T-BOOT-001 (see task.md)
- **Priority:** High (foundation)
- **Dependencies:** None

### 2. Tool Ecosystem Definitions
- **Status:** MISSING / UNVERIFIED
- **Why it matters:** Every integrated tool must have explicit role, boundaries, health, and recovery.
- **Current state:** Conceptual names appear only in conversation history and this documentation phase; none present in repository.
- **Desired state:** `docs/tools.md` with verified roles for OpenCode, Hermes, OpenClaw, NemoClaw, Prime Agent, FreeBuff, Omni Router (and any others discovered).
- **Recommended task:** T-TOOL-001
- **Priority:** High
- **Dependencies:** Official documentation research (REQUIRES VALIDATION)

### 3. Agent Role Contracts
- **Status:** PARTIAL
- **Why it matters:** Prevents overlapping responsibilities and uncontrolled delegation.
- **Current state:** AGENTS.md defines operating rules for agents working *on* FROGE; no role contracts for the runtime agents FROGE will orchestrate.
- **Desired state:** Explicit Agent Identity / Role / Responsibilities / Boundaries / Allowed Tools / etc.
- **Recommended task:** T-AGENT-001
- **Priority:** High
- **Dependencies:** Tool definitions

### 4. Provider / Model Architecture
- **Status:** PARTIAL (high-level only)
- **Why it matters:** Provider abstraction and health/failover are core goals.
- **Current state:** Mentioned in architecture and orchestrator docs; no concrete contracts.
- **Desired state:** Documented discovery, health, classification, failover, cooldown, session-continuity (mechanism TBD).
- **Recommended task:** T-PROV-001
- **Priority:** Medium (after bootstrap & tools)
- **Dependencies:** None for documentation

### 5. MCP Control Plane Implementation
- **Status:** DEFERRED
- **Why it matters:** Planned integration boundary; not current-phase work.
- **Current state:** High-level document exists.
- **Desired state (future):** Full interface, health, permissions after verification of real Mega MCP / FROGE MCP.
- **Recommended task:** Marked OUT OF SCOPE for this phase
- **Priority:** Deferred
- **Dependencies:** External Mega MCP verification

### 6. Skills vs Plugins Distinction & Lifecycle
- **Status:** MISSING
- **Why it matters:** Skills = reusable operational knowledge; Plugins = executable capability. Must not be conflated.
- **Current state:** Skills mentioned abstractly; plugins absent.
- **Desired state:** Clear definitions + structure + lifecycle.
- **Recommended task:** T-SKILL-001
- **Priority:** Medium

### 7. Knowledge / Memory Stack
- **Status:** MISSING
- **Why it matters:** Persistent project knowledge and operational memory are required for context resume.
- **Current state:** Generic “Context & Memory” layer only.
- **Desired state:** Clear separation of concerns (human-readable notes, operational memory, graph, controlled operations).
- **Recommended task:** T-KNOW-001 (later phase)
- **Priority:** Later

### 8. Health Model
- **Status:** PARTIAL
- **Why it matters:** Installed ≠ Configured ≠ Running ≠ Healthy ≠ Functionally Verified.
- **Current state:** Principle stated; no formal definitions or tool-specific checks.
- **Desired state:** Formal health vocabulary + evidence requirements.
- **Recommended task:** T-HEALTH-001
- **Priority:** High

### 9. Recovery Model
- **Status:** PARTIAL
- **Why it matters:** Classified failures + verified recovery are core goals.
- **Current state:** High-level in orchestrator and architecture.
- **Desired state:** Failure taxonomy + detect → classify → diagnose → repair → verify → record.
- **Recommended task:** T-REC-001
- **Priority:** High

### 10. Testing & Evidence Harness
- **Status:** MISSING
- **Why it matters:** No claim of “complete” without evidence.
- **Current state:** Zero tests.
- **Desired state:** Layered test strategy + acceptance criteria per phase.
- **Recommended task:** T-TEST-001
- **Priority:** High (parallel with implementation phases)

### 11. Living Project Management Documents
- **Status:** MISSING (prior to this commit)
- **Why it matters:** Context resume requirement.
- **Current state:** Created in this phase (flow.md, task.md, tracker.md).
- **Desired state:** Continuously updated.
- **Recommended task:** Ongoing

### 12. ADRs
- **Status:** MISSING (prior to this phase)
- **Why it matters:** Architectural decisions must be recorded, not lost in chat.
- **Current state:** Several foundational ADRs introduced in this phase.
- **Desired state:** ADR process followed for future decisions.

### 13. Intended vs Actual Repository Structure
- **Status:** INCONSISTENT
- **Why it matters:** README describes folders that do not exist (mcp/, skills/, providers/, tests/, scripts/, config/).
- **Current state:** README is aspirational.
- **Desired state:** README reflects reality + points to living docs; structure grows with phases.
- **Recommended task:** Update README (this phase)

### 14. Secrets / Security Implementation
- **Status:** PARTIAL (policy only)
- **Why it matters:** Security must be designed before code that handles credentials.
- **Current state:** “Never commit secrets” stated; no concrete secret-store or redaction design.
- **Desired state:** Documented principles + future secure configuration approach.
- **Recommended task:** T-SEC-001

## Summary Counts (approximate)

- MISSING: majority of operational systems
- PARTIAL: architecture, orchestrator, MCP intent, health/recovery principles
- DEFERRED: all MCP implementation, Omni Router MCP, frontend/design
- UNVERIFIED: every external tool capability

This gap list is the primary input to `docs/task.md`.
