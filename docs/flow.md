# FROGE Agent — Execution Flow

**Last updated:** 2026-08-31
**Status:** Target architecture documented; current implementation flow is essentially “documentation only”.

## 1. Distinction Rule

- **Current Implementation Flow** = what the repository can actually do today.
- **Target Architecture Flow** = the intended end-state lifecycle.

Never mix the two without explicit labels.

## 2. Current Implementation Flow (Reality)

```
Clone repository
   ↓
Read README + docs/
   ↓
Understand vision, architecture contracts, agent operating rules
   ↓
(No executable bootstrap, tools, agents, providers, or runtime yet)
```

Evidence: only documentation files + package stub exist.

## 3. Target Architecture Flow (Intended Lifecycle)

```
USER / OPERATOR
   ↓
FROGE ENTRY POINT
   ↓
BOOTSTRAP / ENVIRONMENT CHECK
   ├── System Detection
   ├── Prerequisite Detection
   ├── Tool Detection
   ├── Version Detection
   ├── Compatibility Check
   └── Desired State Calculation
   ↓
INSTALL / UPDATE / REPAIR (idempotent)
   ↓
VERIFICATION (evidence required)
   ↓
AI TOOL SETUP
   ↓
AGENT ROLE LOADING & CONFIGURATION
   ↓
PROVIDER CONFIGURATION
   ↓
MODEL DISCOVERY & SELECTION
   ↓
SKILLS / PLUGINS INSTALLATION
   ↓
KNOWLEDGE / MEMORY INITIALIZATION
   ↓
PROJECT DISCOVERY & CONTEXT
   ↓
TASK EXECUTION (via Orchestrator)
   ├── Planning
   ├── Capability Discovery
   ├── Routing
   ├── Execution (permissioned)
   └── Validation + Evidence
   ↓
HEALTH MONITORING (continuous)
   ↓
FAILURE DETECTION
   ↓
CLASSIFY → DIAGNOSE → REPAIR / FAILOVER → VERIFY → RECORD
   ↓
SESSION KNOWLEDGE UPDATE
   ↓
PROJECT KNOWLEDGE UPDATE
   ↓
FINAL STATUS + EVIDENCE
```

## 4. Bootstrap Desired-State Machine (Target)

| Detected State | Action |
|----------------|--------|
| MISSING | INSTALL → VERIFY |
| OUTDATED | UPDATE → VERIFY |
| CURRENT | VERIFY → KEEP |
| BROKEN | REPAIR → VERIFY |
| UNKNOWN | DIAGNOSE → re-classify |

Idempotency requirement: re-running bootstrap on a healthy system must detect CURRENT and produce verification evidence without destructive reinstallation.

## 5. Orchestrator Pipeline (from existing ORCHESTRATOR.md — preserved)

```
Task Intake
   ↓
Context / Session
   ↓
Planning
   ↓
Capability Discovery
   ↓
Routing
   ↓
Execution
   ↓
Validation
   ├── PASS → Result + Evidence
   └── FAIL → Error Classification → Recovery → Re-validate
```

## 6. Health Check Ladder (Target — every important tool)

1. Discoverable / Installed?
2. Correct version?
3. Executable available?
4. Configuration valid?
5. Gateway / service running? (if applicable)
6. API / endpoint responding?
7. Authentication valid?
8. Functional test successful?

**Installed ≠ Configured ≠ Running ≠ Healthy ≠ Functionally Verified**

## 7. Out-of-Scope in Current Phase

- Any MCP server or client implementation
- Omni Router MCP
- Mega MCP construction or redesign
- Frontend / UI / design.md
- Actual tool installation code

These appear only as future integration boundaries in documentation.

## 8. Resume Contract

Any future agent must be able to read this file + `docs/tracker.md` + `docs/task.md` + `docs/CURRENT-STATE.md` and know exactly where the project stands without conversation history.
