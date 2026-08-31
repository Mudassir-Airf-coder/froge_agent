# FROGE Bootstrap — Specification (Target Architecture)

**Status:** DOCUMENTED ONLY (no implementation)  
**Last updated:** 2026-08-31

## Purpose

Prepare a developer machine so that the rest of the FROGE control plane can operate.  
Bootstrap is the first stage of the target lifecycle.

## Desired-State Machine

```
DETECT
  ↓
CLASSIFY as one of:
  MISSING | OUTDATED | CURRENT | BROKEN | UNKNOWN
  ↓
ACT:
  MISSING  → INSTALL  → VERIFY
  OUTDATED → UPDATE   → VERIFY
  CURRENT  → VERIFY   → KEEP
  BROKEN   → REPAIR   → VERIFY
  UNKNOWN  → DIAGNOSE → re-classify
```

## Idempotency Requirement

- First run on a clean machine: installs and verifies.
- Subsequent runs on a healthy machine: detect CURRENT, produce verification evidence, make no destructive changes.
- Never blindly reinstall or upgrade everything.

## High-Level Responsibilities (Target)

1. System detection (OS, architecture, Windows-first focus)
2. Prerequisite / dependency detection (Python, Node, Git, Docker, PowerShell, package managers, etc.)
3. Version detection and compatibility matrix (TBD)
4. Desired-state calculation
5. Ordered install / update / repair with concurrency controls and locks
6. Verification that produces evidence
7. Recording of results for the knowledge layer

## Explicit Non-Goals (Current Phase)

- Actual installation code
- Multi-terminal orchestration implementation
- Concrete dependency list (requires research + verification)

## Health Ladder Applied to Bootstrap Itself

Bootstrap is not “done” when commands finish.  
It is done when verification evidence shows the environment meets the desired state.

## Open Questions / TBDs

- Exact dependency set and version constraints → REQUIRES VALIDATION
- Windows vs WSL2 requirements → REQUIRES VALIDATION
- Concrete concurrency / lock / port-conflict model → TBD
- Evidence format → TBD (to be defined with health.md)

## Related Documents

- docs/flow.md
- docs/health.md (to be written)
- docs/GAPS.md (Bootstrap gap)
