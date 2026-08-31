# FROGE Tool Research Archive

This directory is the consolidated research index for tools considered by the FROGE installation/verification skill.

## Source documents currently present at repository root

- `01_Hermes.md` — personal/local Hermes architecture; evidence is `[STATED]` and not independently verified.
- `02_OpenCode.md` — OpenCode CLI/TUI, headless mode, providers, MCP, auth, plugins.
- `04_Omni_Router.md` — OmniRoute local OpenAI-compatible gateway and routing behavior.
- `05_Codex.md` — OpenAI Codex CLI, auth, sandbox/approval, MCP and providers.
- `06_Claude_Code.md` — Claude Code CLI, hooks, permissions, subagents, skills/plugins, MCP.
- `08_Prime_Agent.md` — Prime Agent harness; Windows limitation and explicit non-sandbox warning.
- `09_Atomic_Agent.md` — Atomic Agents Python framework/library; not a standalone CLI agent.
- `10_OpenClaw.md` — OpenClaw gateway, Windows install path, security/sandboxing notes.
- `12_Freebuff.md` — Freebuff/Codebuff research; npm CLI and multi-agent behavior.
- `13_DeepSeek_Harness.md` — DeepSeek Harness (`dsh`), plugin architecture, Web UI, subagents and provider support.
- `15_NemoClaw.md` — NVIDIA NemoClaw/OpenShell sandbox and inference endpoint onboarding.
- `Pi_Agent.md` — Pi coding-agent harness, Windows installer, npm package, RPC/skills/extensions.
- `Strix.md` — Strix security research; most operational details remain UNKNOWN and therefore it is not an install target yet.

## Evidence rule

These source files are research, not proof that a procedure works on the current machine. FROGE may promote a procedure to an executable adapter only after the procedure, version check, functional verification, and failure behavior are validated. Claims marked `[UNKNOWN]` or `[INFERRED]` must never be silently converted into facts.

## Current installation policy

- Windows is the primary target.
- FROGE itself remains the orchestrator and evidence collector.
- Installers must be idempotent and must verify after mutation.
- Do not install Ollama or vLLM as part of the universal installation skill.
- Do not implement MCP servers, Omni Router MCP, Mega MCP, frontend/design work, or a skills/plugins catalog in this installation scope.
- OHSC remains pending/deferred until explicitly promoted.
- Secrets are checked by environment-variable name only and are never printed.
