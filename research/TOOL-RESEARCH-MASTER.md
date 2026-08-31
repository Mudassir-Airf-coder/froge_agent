# FROGE Universal Installation Research Matrix

**Purpose:** convert the existing research set into deterministic installation/verification policy without inventing procedures.

## 1. Installation-ready procedures found in research

| Tool | Research-backed install entry | Platform note | Verification requirement | Promotion state |
|---|---|---|---|---|
| Freebuff | `npm install -g freebuff` | Node/npm; Windows CLI expected by research | `freebuff --version` or the tool's actual version command must be validated locally | CANDIDATE — validate first |
| Codex | `npm install -g @openai/codex` then `codex login` | Windows supported | version + authenticated startup | CANDIDATE — validate first |
| OpenClaw | PowerShell installer `iwr -useb https://openclaw.ai/install.ps1 | iex` or npm route from research | Native Windows installer documented | version + gateway/CLI health; never expose gateway publicly | CANDIDATE — validate first |
| Pi Agent | `npm install -g --ignore-scripts @earendil-works/pi-coding-agent` or documented PowerShell installer | Native Windows installer documented | `pi --version` + non-interactive/RPC smoke test | CANDIDATE — validate first |
| Atomic Agents | `pip install atomic-agents` | Python library, not a standalone agent | Python import/package version | CANDIDATE — library only |
| DeepSeek Harness | `npx @deepseek-ai/dsh web` | Node/npx path documented | `dsh`/web startup + provider smoke test | CANDIDATE — validate first |
| Prime Agent | `curl .../install.sh \| sh` from research | **macOS/Linux only in research; not a native Windows target** | version + disposable workspace smoke test | BLOCKED on native Windows |
| NemoClaw | `nemoclaw onboard` after installing its documented prerequisites | Linux/DGX-focused research; Windows parity unknown | live endpoint validation is part of onboarding | BLOCKED until Windows support validated |

## 2. Tools with no sufficiently verified install procedure in the supplied research

- OpenCode — rich CLI/MCP documentation is present, but the supplied research file does not provide a concrete install command. Do not invent one.
- Hermes — personal/local project; evidence is `[STATED]`; no public installer. Do not invent one.
- Omni Router — architecture and npm-based distribution are described, but the supplied research does not provide a precise current package/install command. Do not invent one.
- Strix — installation and operational model are mostly `[UNKNOWN]`; do not install automatically.
- OpenCode, Hermes, Omni Router, Strix therefore remain `REQUIRES_VALIDATION` until a concrete current procedure is added.

## 3. Explicit exclusions

The universal install skill must NOT install:

- Ollama
- vLLM
- Any MCP server
- Omni Router MCP
- Mega MCP redesign
- Frontend/design system
- Skills/plugin catalog
- OHSC for now

These are scope decisions, not missing implementation.

## 4. Universal execution contract

For every candidate tool:

1. Discover whether it is already installed.
2. Record executable path and version.
3. Detect dependencies before mutation.
4. If already healthy, KEEP it.
5. If missing and the procedure is validated, install it.
6. Verify installation immediately.
7. Run the strongest available functional health check.
8. Persist evidence and state.
9. If any step is not sufficiently evidenced, stop that tool at `REQUIRES_VALIDATION` rather than guessing.
10. Never print or commit credentials.

## 5. Parallelism

Parallelize independent discovery/version checks. Serialize mutations that share npm/pip/package-manager state or have dependency relationships. A failed parent dependency blocks its dependents. Never run two competing installers for the same tool concurrently.

## 6. Safety and rollback

- Prefer user-level installation where supported.
- Do not require administrator privileges unless the verified procedure explicitly requires them.
- Do not use `shell=True` for arbitrary tool execution.
- Treat installer scripts as external mutation and require explicit authorization unless the caller has already granted unattended installation authority.
- Never claim HEALTHY from a version check alone; distinguish installed from functional health.
- Preserve an audit record of every mutation and verification result.

## 7. Evidence promotion rule

A tool becomes `AUTO_INSTALL_READY` only when FROGE has all of:

- official/primary source or repository reference,
- exact install procedure,
- supported platform confirmation,
- exact version/executable check,
- post-install verification,
- failure/repair behavior,
- evidence date,
- a passing local smoke test.

Until then, the skill may report the research candidate but must not invent or silently execute a procedure.
