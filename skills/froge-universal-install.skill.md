# Skill: FROGE Universal Tool Installation & Verification

**Skill ID:** `froge-universal-install`  
**Version:** 1.0.0  
**Status:** ACTIVE  
**Last updated:** 2026-09-01  
**Executor:** `froge install-skill` / `src/froge/skill_install.py`

## Purpose

Deterministic, evidence-backed, **idempotent** procedure for a coding agent on a fresh Windows PC:

```
DISCOVER → CHECK → PLAN → INSTALL/UPDATE/REPAIR/KEEP → VERIFY → REPORT → PERSIST
```

Does **not** invent installation commands. Unverified tools remain `REQUIRES_VALIDATION`.

## Scope

**In scope:** Python, Git, Node, npm; FreeBuff, OpenCode, Hermes, OpenClaw, NemoClaw, Prime Agent; Omni Router, Nimble Clock; OHSC, Graphify (inventory only).

**Excluded:** Ollama, vLLM, MCP servers, Omni Router MCP, Mega MCP, skills/plugin catalog, frontend.

## Prerequisites

- FROGE package (`PYTHONPATH=src` or install)
- Commands: `froge doctor`, `froge plan`, `froge install-skill --dry-run`
- Prefer user-level installs; do not assume admin

## Environment

Primary: Windows 10/11 (PowerShell). Also usable for discovery on Linux/macOS.
Execution: argument arrays only (`shell=False` via `executil`).

## Inventory

### System (discovery verified)

| ID | Version command | Auto-install |
|----|-----------------|--------------|
| python | `python3 --version` / `python --version` | REQUIRES_VALIDATION if missing |
| git | `git --version` | REQUIRES_VALIDATION if missing |
| node | `node --version` | REQUIRES_VALIDATION if missing |
| npm | `npm --version` | depends on node |

### External (all REQUIRES_VALIDATION)

freebuff, opencode, hermes, openclaw, nemoclaw, prime-agent, omni-router, nimble-clock, ohsc, graphify

**Promotion rule:** fill research block (official source, install procedure, version command, verification, repair, evidence date) before adding concrete install_command.

## Decision tree

```
DISCOVER →
  UNKNOWN / no executable → REQUIRES_VALIDATION / DIAGNOSE
  MISSING + verified install_command → INSTALL → VERIFY
  MISSING + unknown → REQUIRES_VALIDATION (do not invent)
  OUTDATED + verified update → UPDATE → VERIFY
  BROKEN + verified repair → REPAIR → VERIFY
  INSTALLED/HEALTHY → KEEP → VERIFY (no reinstall)
```

Implemented by `desired_action` + installer + GenericAdapter.

## Pipeline

| Phase | Action |
|-------|--------|
| A Discovery | `froge doctor` / `discover_environment()` |
| B Preflight | dependencies, credentials name-check only |
| C Plan | `froge plan` — topo order + cycle detection |
| D Install | `froge install-skill --dry-run` then `--apply` if authorized |
| E Health | L1–L6 ladder; SKIP ≠ PASS; no L6 → not HEALTHY |
| F Final | re-discover, verify, report, persist state |

### Parallelization

- PARALLEL-SAFE: independent KEEP/VERIFY
- SEQUENTIAL: dependency parent before child; same package-manager mutations

## Credentials

- Check env var **names** only (`secret_env_present`)
- Never log/print/commit values (`redact()`)
- One canonical source per provider family when known

## Idempotency

First run: install missing verified tools; diagnose unvalidated.  
Second run: KEEP healthy; no unnecessary reinstall.  
State: `.froge/state.json` atomic writes.

## Failure classes

See `froge.errors.ErrorKind`. Critical dependency failure blocks dependents.

## Report format

```
FROGE INSTALLATION REPORT
Environment: ...
Tools: Tool | Action | Result | Verify | Message
Summary: KEEP / INSTALL / UPDATE / REPAIR / FAILED / REQUIRES_VALIDATION
Overall: PASS | PARTIAL | FAIL
```

## Agent execution recipe

```
1. Install/load FROGE
2. Read this skill
3. froge doctor
4. froge plan
5. froge install-skill --dry-run
6. Obtain authorization for mutation
7. froge install-skill --apply
8. froge verify && froge state
9. Do not invent commands for REQUIRES_VALIDATION tools
```

```python
from froge.skill_install import run_install_skill
result = run_install_skill(dry_run=True)
```

## Architecture mapping

| Concern | Module |
|---------|--------|
| Manifests | manifest.py |
| Discovery | discovery.py |
| Plan/cycles | planner.py |
| Install | installer.py + adapters/ |
| Health | health.py |
| Skill orchestration | skill_install.py + bootstrap.py |
| State | persistence.py |
| Secrets | security.py |
| CLI | install-skill |

## Related

docs/bootstrap.md, health.md, tools.md, security.md, CURRENT-STATE.md, tracker.md, ADR-002, ADR-004
