# FROGE Agent Role System

**Status:** FOUNDATION + HYPOTHESES  
**Last updated:** 2026-08-31

## Distinction

- **AGENTS.md** (root) = operating contract for agents that *work on the FROGE codebase*.
- **This file** = role contracts for the runtime agents and tools that FROGE will eventually orchestrate.

## Current Reality

No runtime agent integrations exist in the repository.  
All roles below are starting architectural hypotheses and must be verified before implementation.

## Starting Role Hypotheses

### OpenCode
- **Proposed role:** Primary Software Engineering / Coding Agent
- **Responsibilities (hypothesis):** repository exploration, implementation, debugging, refactoring, testing, code modification, code review, engineering workflows
- **Non-responsibilities:** long-running background automation, master control-plane decisions
- **Status:** REQUIRES VALIDATION

### Hermes
- **Proposed role:** Persistent Automation / Long-Running Agent Runtime
- **Responsibilities (hypothesis):** persistent workflows, background automation, scheduled work, operational tasks, memory-related workflows
- **Status:** REQUIRES VALIDATION

### OpenClaw
- **Proposed role:** Autonomous Agent / Automation Runtime
- **Status:** REQUIRES VALIDATION

### NemoClaw
- **Proposed role:** Security/governance or NVIDIA-oriented runtime (must be kept distinct from OpenClaw)
- **Status:** REQUIRES VALIDATION

### Prime Agent
- **Proposed role:** Specialized long-horizon / research / recursive agent environment
- **Rule:** Do **not** automatically make it the master controller.
- **Status:** REQUIRES VALIDATION

### FreeBuff
- **Proposed role:** Lightweight / free coding-agent path
- **Status:** REQUIRES VALIDATION (inspect actual project workflow first)

## Required Contract Fields (Future)

For each agent that is promoted:

- Agent Identity
- Role
- Responsibilities
- Boundaries (what it must never do)
- Allowed Tools / MCPs / Knowledge systems
- Preferred / Fallback Models
- Skills
- Permissions
- Runtime / Health
- Inputs / Outputs / Triggers
- Failure behavior

## Overlap Rule

Overlapping responsibilities are forbidden unless an ADR explicitly justifies them and defines the authoritative owner.

## Related

- root AGENTS.md (operating contract for contributors)
- docs/tools.md
- docs/ORCHESTRATOR.md (coordination layer)
