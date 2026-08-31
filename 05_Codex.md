# Codex (OpenAI Codex CLI)

## Identity
- Vendor: OpenAI
- Category: AI coding agent — CLI, desktop app (Windows/macOS), VS Code extension, ChatGPT web integration
- Released: April 2025 as Codex CLI; actively updated through 2026 (GPT-5.3-Codex, GPT-5.3-Codex-Spark, GPT-5.4, GPT-5.6 referenced across sources) `[OFFICIAL SOURCE / GITHUB]`
- Install: `npm install -g @openai/codex`
- Auth: `codex login` opens browser OAuth; token saved at `~/.codex/auth.json`

## Core Functionality
- Reads/edits code, runs shell commands, plans and executes multi-step engineering tasks
- **Codex Security** (added March 2026): a dedicated application-security agent mode for finding/fixing vulnerabilities `[OFFICIAL SOURCE]`
- Sandbox/approval model: `sandbox_mode` = `read-only` | `workspace-write` | `danger-full-access`; `approval_policy` gates when Codex asks before acting

## Configuration
- Personal config: `~/.codex/config.toml`
- Project overrides: `.codex/config.toml` — **only loaded when the project is explicitly trusted** (security-relevant design choice)
- Key config fields observed: `model`, `model_provider`, `model_context_window`, `model_auto_compact_token_limit`, `model_reasoning_effort` (minimal/low/medium/high/xhigh), `model_reasoning_summary`, `model_verbosity`, `personality`, `review_model`, `service_tier`, `oss_provider` (lmstudio|ollama, used with `--oss` flag) `[COMMUNITY, cross-checked against official config.md structure]`

## CLI / Automation
- `codex mcp add/list/get/remove <name>` — full MCP server lifecycle management from the CLI
- `codex mcp-server` — Codex can run **as an MCP server itself**, separate from `codex mcp` (client management) `[OFFICIAL DOC]`
- Both CLI and VS Code extension share the same MCP configuration layer

## MCP (deep)
- **Transports:** stdio (local child process) and direct **Streamable HTTP** when the RMCP client is enabled `[OFFICIAL SOURCE: github.com/openai/codex/docs/config.md]`
- **Config format:** TOML, e.g.:
 ```toml
 [mcp_servers.tooluniverse]
 command = "uvx"
 args = ["--refresh", "tooluniverse"]
 [mcp_servers.tooluniverse.env]
 PYTHONIOENCODING = "utf-8"
 ```
- Remote/URL-based servers also supported: `[mcp_servers.openaiDeveloperDocs] url = "https://developers.openai.com/mcp"`
- **Plugin marketplace**: bundles auth + skills + MCP config as one installable unit (e.g. Linear, Vercel integrations ship this way) — simpler than manual MCP config for supported services
- **Cross-tool config note:** MCP server *packages* are portable across Codex/Claude Code/others, but the config *file format* differs — Codex uses TOML, Claude Code uses JSON. Manual translation required when porting configs between the two.

## Providers / Models
- Primary: OpenAI's own GPT-5.x/Codex model family
- `--oss` flag + `oss_provider` setting allows routing to **local model servers** (LM Studio or Ollama) instead of OpenAI's hosted models — this is the most direct built-in local-inference path among the researched tools
- **Omni Router compatibility:** `[INFERRED, likely YES]` — since Codex already supports custom `model_provider` entries and local OSS providers, adding a custom provider pointing at `http://localhost:20128/v1` should work using the same mechanism as Ollama/LM Studio, but this exact config was not found documented for Omni Router specifically.

## Authentication
- OAuth via `codex login` (ChatGPT Plus/Pro subscription) OR direct OpenAI API key
- Token storage: `~/.codex/auth.json`

## Hooks / Extensibility
`[UNKNOWN]` — no dedicated hooks system was surfaced in this pass distinct from MCP/plugins; Claude Code's hook system (PreToolUse/PostToolUse etc.) does not appear to have a documented Codex equivalent in the sources retrieved. Needs a follow-up check of official Codex docs' automation section if hook-level control is required.

## Hermes / MCP Control Potential
- READ_ONLY: `codex mcp list`, `codex mcp get <name>`
- CONTROLLED_WRITE: `codex mcp add/remove`, config.toml edits, running Codex in `workspace-write` sandbox mode with approval gating on
- HIGH_RISK: `sandbox_mode = "danger-full-access"` — should never be the default in any Hermes-driven automation; `codex mcp-server` mode exposes Codex's own capabilities to external callers and needs its own access control review before wiring into a master MCP.

## Windows Notes
- Desktop app available for Windows natively; CLI via npm works cross-platform. No Windows-specific blocker surfaced, but PowerShell path/escaping quirks for TOML config edits should be locally verified.

## Evidence Sources
`[OFFICIAL SOURCE]` developers.openai.com/codex, github.com/openai/codex/docs/config.md (via secondary citations); `[GITHUB]` openai/codex; `[COMMUNITY]` verdent.ai, inventivehq.com, blakecrosley.com, zitniklab.hms.harvard.edu (ToolUniverse docs, cross-checking Codex's MCP behavior).
