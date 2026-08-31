# Skill: FROGE Universal Tool Installation & Verification

**Skill ID:** `froge-universal-install`
**Version:** 2.0.0
**Status:** ACTIVE
**Last updated:** 2026-09-01
**Executor:** `froge install-skill` / `src/froge/skill_install.py`

## Mission

Turn a fresh Windows machine into the declared FROGE tool environment through one deterministic, evidence-backed workflow:

```text
DISCOVER → PREFLIGHT → PLAN → INSTALL/UPDATE/REPAIR/KEEP → VERIFY → FUNCTIONAL CHECK → REPORT → PERSIST
```

The skill is idempotent: an already healthy tool is kept, not reinstalled.

## Non-negotiable rules

1. Never invent an install command.
2. Never convert `[UNKNOWN]` or `[INFERRED]` research into a verified fact.
3. Never claim `HEALTHY` from a version check alone.
4. Never print, store, or commit secret values.
5. Use FROGE's safe execution layer; do not introduce arbitrary `shell=True` execution.
6. Discover first; mutate second.
7. Verify immediately after every mutation.
8. Dependency failures block dependent tools.
9. Parallelize only independent discovery/verification; serialize shared package-manager mutations.
10. Persist evidence, state, and audit information after the run.
11. Prefer user-level installation where the verified procedure supports it.
12. Unverified tools end as `REQUIRES_VALIDATION`, `FAILED`, or `DIAGNOSE` — never a fake PASS.

## Primary target

- Windows 10/11, primarily PowerShell.
- Cross-platform behavior is used only when the research explicitly supports it.
- FROGE is the control plane; concrete tool knowledge comes from the research archive.

## Research source of truth

Read before promoting any tool to an executable adapter:

- `research/README.md`
- `research/TOOL-RESEARCH-MASTER.md`
- Individual research files at repository root: `01_Hermes.md`, `02_OpenCode.md`, `04_Omni_Router.md`, `05_Codex.md`, `06_Claude_Code.md`, `08_Prime_Agent.md`, `09_Atomic_Agent.md`, `10_OpenClaw.md`, `12_Freebuff.md`, `13_DeepSeek_Harness.md`, `15_NemoClaw.md`, `Pi_Agent.md`, `Strix.md`.

## Scope

### System prerequisites

- Python
- Git
- Node.js
- npm

### Candidate ecosystem

- Freebuff / Codebuff
- OpenCode
- Hermes
- Codex
- Claude Code
- Prime Agent
- Atomic Agents
- OpenClaw
- DeepSeek Harness
- NemoClaw
- Omni Router
- Pi Agent
- Strix
- Nimble Clock when a current verified procedure is supplied

### Explicit exclusions

- Ollama
- vLLM
- MCP servers
- Omni Router MCP
- Mega MCP
- Frontend / `design.md`
- Skills/plugin catalog
- OHSC for the current installation cycle

These are intentional scope exclusions, not TODOs to silently implement.

## Research-backed candidate procedures

The supplied research contains concrete candidate procedures for some tools and only architectural information for others. Preserve that distinction.

### Freebuff

Research documents:

```text
npm install -g freebuff
```

Validate the executable/version and perform a minimal safe startup check before promotion to automatic installation.

### Codex

Research documents:

```text
npm install -g @openai/codex
codex login
```

Authentication is a separate credential step; never capture or print tokens.

### OpenClaw

Research documents a native Windows PowerShell installer and an npm route. Treat installer execution as an external mutation and validate the current official procedure before promotion to an unattended adapter.

### Pi Agent

Research documents:

```text
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

and a native PowerShell installer. Validate current release/version behavior before promotion.

### Atomic Agents

Research documents a Python package install. This is a library/framework, not a standalone coding-agent executable. Verify package import/version rather than expecting a worker CLI.

### DeepSeek Harness

Research documents:

```text
npx @deepseek-ai/dsh web
```

Treat this as a runtime/startup procedure, not proof of permanent installation. Validate current package and executable semantics before creating a persistent adapter.

### Prime Agent

Research documents a shell installer for macOS/Linux and does not establish native Windows support. Do **not** auto-install Prime Agent on the Windows target through this skill.

### NemoClaw

Research documents `nemoclaw onboard` and scripted provider configuration, but Windows support is not established. Do not promote it to an unattended Windows installer until platform support is directly validated.

### Research-only / blocked until procedure validation

- OpenCode
- Hermes
- Omni Router
- Strix
- Nimble Clock
- Claude Code

Their research is valuable for architecture and verification design, but the supplied research set does not provide enough current, platform-specific installation evidence to justify inventing a command.

## Execution algorithm

### Phase 0 — Load policy

1. Read the master research matrix.
2. Read current FROGE config/manifest.
3. Load the explicit excluded-tool set.
4. Determine whether mutation authorization is available.

### Phase A — Discovery

Run:

```text
froge doctor
froge status --json
```

For each target capture executable/path, version, platform, dependencies, lifecycle state, and prior FROGE evidence.

### Phase B — Preflight

Validate platform compatibility, dependencies, current install procedure, expected executable/version command, credential names, and functional-test availability. If any mandatory fact is missing, mark `REQUIRES_VALIDATION`.

### Phase C — Plan

Use FROGE's desired-state planner:

```text
froge plan
```

Expected actions:

- `KEEP` — already healthy/acceptable
- `INSTALL` — missing + verified procedure
- `UPDATE` — outdated + verified update procedure
- `REPAIR` — broken + verified repair procedure
- `DIAGNOSE` / `REQUIRES_VALIDATION` — insufficient evidence

Never turn `DIAGNOSE` into an invented install action.

### Phase D — Mutation

Preview first:

```text
froge install-skill --dry-run
```

Apply only when mutation authorization is present:

```text
froge install-skill --apply
```

Use adapters rather than scattered hard-coded installer logic. Every adapter must expose evidence for install, update, repair, and verify.

### Phase E — Verification

After each installation/update/repair:

1. Re-discover executable.
2. Check version.
3. Check dependencies.
4. Run the strongest available functional test.
5. Classify output without leaking secrets.
6. Map the result to lifecycle state.

Health ladder:

```text
L1 executable/path
L2 version
L3 dependencies
L4 configuration
L5 startup/connectivity
L6 functional behavior
```

`SKIP` is not `PASS`. Missing L6 means `INSTALLED`, not automatically `HEALTHY`.

### Phase F — Persistence/report

Run:

```text
froge verify
froge state
```

Persist action, result, evidence, version, timestamps, error classification, repairability, and final lifecycle state.

## Credential handling

Credentials are never part of research text, logs, reports, commits, or source code.

Allowed: check environment-variable **names** only. Forbidden: printing keys/tokens, committing `.env` secrets, or copying authentication files into the repository.

When login is required, report `AUTH_REQUIRED` and name the required credential/action without exposing the secret.

## Parallel execution

### Safe in parallel

- discovery of unrelated tools
- version checks
- read-only health checks
- independent report generation

### Sequential

- Node/npm mutation chains
- Python package mutations sharing one environment
- parent dependency before dependent tool
- install → verify for the same tool
- repair → verify for the same tool

## Idempotency contract

First run:

```text
missing + validated → INSTALL
present + healthy → KEEP
unknown/unvalidated → REQUIRES_VALIDATION
```

Repeated run:

```text
healthy → KEEP
no unnecessary reinstall
```

State lives in `.froge/state.json` with atomic persistence and audit history.

## Failure handling

Classify failures using `froge.errors.ErrorKind`. Preserve evidence, identify transient/dependency/auth/platform/procedure/unrecoverable failure, attempt repair only when a verified repair procedure exists, and otherwise stop that tool at `FAILED` or `REQUIRES_VALIDATION`. Continue independent tools where dependency safety permits.

## AUTO_INSTALL_READY gate

A tool may move from research candidate to automatic adapter only after all are present:

- primary/official source or repository reference;
- exact current install procedure;
- Windows support confirmation for the Windows target;
- executable/path check;
- version check;
- post-install verification;
- functional smoke test where available;
- repair/update behavior;
- evidence date;
- passing local validation.

## Final report

Every run produces:

```text
FROGE UNIVERSAL INSTALLATION REPORT
Environment: <platform/runtime>
Tool | Desired Action | Actual Action | Version | Verification | Final State | Evidence
Summary: KEEP=<n> INSTALL=<n> UPDATE=<n> REPAIR=<n> FAILED=<n> REQUIRES_VALIDATION=<n>
Overall: PASS | PARTIAL | FAIL
```

## Agent recipe

```text
1. Load FROGE.
2. Read this skill + research/TOOL-RESEARCH-MASTER.md.
3. froge doctor
4. froge status --json
5. froge plan
6. froge install-skill --dry-run
7. Apply only authorized, evidence-backed mutations.
8. Verify every changed tool.
9. froge verify
10. froge state
11. Persist/update documentation and evidence.
12. Never invent a missing procedure.
```

## Architecture mapping

| Concern | FROGE module |
|---|---|
| Manifest | `manifest.py` |
| Discovery | `discovery.py` |
| Plan/cycles | `planner.py` |
| Install/update/repair | `installer.py` + adapters |
| Health | `health.py` |
| Skill orchestration | `skill_install.py` + `bootstrap.py` |
| Persistence | `persistence.py` |
| Security/redaction | `security.py` |
| CLI | `cli.py` |
| Research | `research/` |

## Completion rule

The skill is complete only when the run is reproducible from repository state, every mutation has evidence, every installed tool has a verification result, and no excluded or unvalidated tool was silently installed.
