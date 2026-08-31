# FROGE Implementation Plan

**Created:** 2026-08-31  
**Status:** Active  
**Based on:** Full repository + documentation inspection at commit 97d1538…

## 1. Inspection Summary

### What Exists
- Complete documentation foundation (CURRENT-STATE, GAPS, flow, task, tracker, bootstrap, tools, agents, providers, health, recovery, security, testing, ADRs 001–005).
- High-level architecture and orchestrator contracts.
- Python package stub: `src/froge/__init__.py` (`__version__ = "0.1.0"`).

### What Does Not Exist
- Any package manifest (`pyproject.toml`, `requirements.txt`, etc.).
- Configuration system.
- Logging / observability.
- State model / lifecycle enums.
- Tool manifest schema or data.
- Discovery, install, update, repair, health, or functional-test engines.
- Any tests.
- CLI / entry points.
- Agent registry implementation.
- Provider / model abstraction code.
- Session management.
- Error classification / failover code.
- Knowledge integration code.

### Architecture Consistency Check
- No contradictions found between living documents.
- ADR-004 (MCP deferred) and ADR-005 (frontend deferred) remain binding.
- Skills / plugins ecosystem remains deferred.
- All external tool capabilities remain marked REQUIRES VALIDATION.
- Bootstrap desired-state machine and health ladder are the authoritative contracts for the first implementation target.

## 2. Implementation Gap Analysis (vs Target Bootstrap + Install Orchestrator)

| Capability | Doc Status | Code Status | Gap Priority |
|------------|------------|-------------|--------------|
| Project packaging & config foundation | Documented | Missing | P0 |
| Logging + structured results | Documented | Missing | P0 |
| Component state model / lifecycle | Documented (health.md, bootstrap.md) | Missing | P0 |
| Tool manifest schema + registry | Documented conceptually | Missing | P0 |
| Environment / dependency discovery | Documented | Missing | P1 |
| Installation abstraction layer | Documented | Missing | P1 |
| Health / functional verification engine | Documented | Missing | P1 |
| Idempotent bootstrap orchestrator | Documented | Missing | P1 |
| CodeBuff / FreeBuff workflow | Hypothesis only | Missing | P2 (after engine) |
| Provider abstraction + Omni Router integration | Documented boundary | Missing | P2 |
| Agent registry | Documented | Missing | P2 |
| Failover / session continuity | Documented | Missing | P3 |
| Knowledge (OHSC/Obsidian/Graphify) | Deferred / high-level | Missing | Later |
| Skills / Plugins catalog | Explicitly deferred | N/A | Deferred |
| New MCP servers | Explicitly deferred (ADR-004) | N/A | Deferred |

## 3. Dependency Graph (Implementation Order)

```
PHASE I-1  Project Foundation
           ├── packaging (pyproject.toml)
           ├── configuration system
           ├── logging + structured result types
           ├── component state model / enums
           └── tool manifest schema + empty registry
                 ↓
PHASE I-2  Environment Discovery
           └── detect OS, runtimes, paths, versions
                 ↓
PHASE I-3  Dependency / Prerequisite Management
                 ↓
PHASE I-4  Tool Installation Engine (discover/install/update/configure/start/stop/repair)
                 ↓
PHASE I-5  Verification / Health / Functional-Test Engine
                 ↓
PHASE I-6  Bootstrap Orchestrator (desired-state machine)
                 ↓
PHASE I-7  First concrete tool workflow (CodeBuff / FreeBuff — after research)
                 ↓
PHASE I-8+ Provider, Agent Registry, Session, Failover, etc.
```

No phase may start until its dependencies are complete and verified.

## 4. Immediate Next Task (First Dependency-Safe Work)

**I-1-001 — Project Foundation**

Create the minimal, testable core that every later component depends on:

1. Proper Python packaging (`pyproject.toml`, package layout).
2. Central configuration system (schema, defaults, env support, validation).
3. Structured logging + result / evidence types.
4. Component lifecycle state model (enums matching health.md / bootstrap.md).
5. Tool manifest schema (Pydantic or equivalent) + in-memory / file-backed registry.
6. Minimal unit tests for the above.
7. Update documentation, task.md, tracker.md.

Acceptance criteria for I-1-001 will be written into task.md before any code is committed.

## 5. Explicit Non-Goals for Current Cycle

- No skill catalog
- No plugin ecosystem
- No new MCP servers
- No Omni Router MCP
- No Mega MCP redesign
- No frontend / design.md
- No claim that any external tool is “working” without functional verification evidence
- No hard-coded installation logic scattered outside the installation engine

## 6. Definition of Done (Reminder)

A task is COMPLETE only when:

CODE + TESTS PASS + FUNCTIONAL BEHAVIOR VERIFIED + DOCUMENTATION UPDATED + TASK UPDATED + TRACKER UPDATED + NO KNOWN REGRESSION

For installation-related work:

INSTALLED + CONFIGURED + STARTED + HEALTHY + FUNCTIONALLY VERIFIED + INTEGRATED
