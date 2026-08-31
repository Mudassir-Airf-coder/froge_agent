# OpenCode

## Identity
- Vendor: opencode.ai (formerly built by the SST/Anomaly team)
- Category: Open-source terminal-first AI coding agent (TUI + CLI), with optional desktop/IDE/web surfaces
- License: Open source; large community (100K+ GitHub stars range as of 2026)
- Scale claim per official site: 195K+ stars, 950+ contributors, 16M+ monthly developers `[OFFICIAL SOURCE: opencode.ai]`

## Core Functionality
- Interactive TUI built for terminal-first agentic coding
- Non-interactive/headless mode: `opencode -p "prompt"` prints response to stdout and exits; supports `-f json` for structured output and `-q` to suppress the spinner for scripting `[GITHUB]`
- Session management: save/resume conversations; SQLite-backed persistent storage `[GITHUB]`
- Tool integration: can execute shell commands, search files, modify code
- LSP (Language Server Protocol) integration for code intelligence
- Agents: specialized sub-assistants configurable via `opencode agent create` (interactive or fully flagged with `--path --description --mode --permissions`); agents are saved as markdown files with frontmatter, either globally or per-project `[OFFICIAL DOC: opencode.ai/docs/agents]`
- `opencode import` can import a session from a file or a shared URL

## CLI / Automation
- `opencode serve`: starts a headless HTTP server with an OpenAPI spec exposed at `/doc`; official JS/TS SDK `@opencode-ai/sdk` available for programmatic control `[OFFICIAL DOC]`
- `opencode web`: HTTP server + browser-based web UI; `OPENCODE_SERVER_PASSWORD` env var enables HTTP basic auth
- `opencode acp`: starts an **ACP (Agent Client Protocol) server** communicating over stdin/stdout using newline-delimited JSON — this is a strong candidate for Hermes-style external control, since ACP is explicitly designed for another program to drive the agent
- `opencode attach`: attach a TUI to an already-running backend server started via `serve`/`web` — supports remote-backend usage
- Database tools + a "print db path" debug command exist for troubleshooting
- `opencode upgrade` (to latest or specific version), `opencode uninstall` (removes all related files)
- Global flags exist across the CLI; scripting-suitable due to JSON output mode and quiet mode

## Authentication
- `opencode auth login` stores credentials at `~/.local/share/opencode/auth.json` `[OFFICIAL SOURCE]`

## Providers / Models
- Multi-provider: OpenAI, Anthropic, Google Gemini, AWS Bedrock, Groq, Azure OpenAI, OpenRouter, and 75+ providers total per official docs claims `[OFFICIAL DOC]`
- Model selection via `opencode models`
- **Omni Router compatibility:** Since OpenCode supports arbitrary OpenAI-compatible providers and custom endpoints via config, pointing it at `http://localhost:20128/v1` is architecturally plausible but **not explicitly documented** — `[INFERRED]`, not `[OFFICIAL DOC]`. Would need to be added as a custom provider entry in `opencode.json`.

## MCP (deep)
- **Config file locations:** Global `~/.config/opencode/opencode.json`; project-level `opencode.json` or `opencode.jsonc` in repo root. Files are **merged**, not overridden wholesale — project settings take precedence for conflicting keys only `[OFFICIAL DOC / COMMUNITY]`
- **Transports supported:**
 - `local`/`stdio` — server runs as local child process; OpenCode's array-style command format: `"command": ["docker", "run", ...]` (note: different from Cursor/Zed's split command+args style) `[OFFICIAL DOC/GITHUB]`
 - `remote` — HTTP/SSE remote MCP servers, e.g. `{"type": "remote", "url": "https://mcp.example.com/mcp"}`
- **Auth:** supports OAuth flow for remote MCP servers (e.g. Sentry) — triggered via `opencode mcp auth <server>`, opens a browser for OAuth
- **CLI subcommands:** list configured MCP servers + connection/auth status; test HTTP connectivity; walk through OAuth discovery
- **Lifecycle:** "When AI calls an MCP tool, OpenCode creates a new client connection, executes the tool, and returns results" — connections appear to be created per-call rather than held persistently `[OFFICIAL DOC]`
- **Environment key naming gotcha:** OpenCode uses `environment` (not `env`) for MCP server env vars — a common cross-tool config error source

## MCP Control Potential (for a future Hermes-controlling-OpenCode MCP)
- READ_ONLY: `opencode mcp list`/status checks, `opencode models`, session read/import
- CONTROLLED_WRITE: `opencode run "<prompt>"` non-interactive execution (auto-approves permissions in that mode — **note the risk**: "-p" mode auto-approves ALL permissions for the session, so wrapping this in an MCP tool without an additional approval gate is a real HIGH_RISK surface)
- HIGH_RISK: raw shell/tool execution granted to OpenCode agents; any MCP tool that starts an `opencode run` with unrestricted permissions

## Plugins
- Plugin files placed in `.opencode/plugins/` (project) or `~/.config/opencode/plugins/` (global); can also be loaded from npm via the `plugin` config array `[OFFICIAL DOC]`
- Plugins can add custom tools, hooks, and integrations

## Windows Notes
`[UNKNOWN]` — no Windows-specific caveats surfaced in this research pass; OpenCode is a Go-based CLI application (per one GitHub source) which generally cross-compiles cleanly, but this should be locally verified rather than assumed.

## Limitations / Open Questions
- Exact skill-system mechanics beyond agents were not deeply covered in the sources retrieved — needs a follow-up documentation pass if skills (distinct from agents) matter to your design.
- Omni Router native support is unverified.

## Evidence Sources
`[OFFICIAL DOC]` opencode.ai/docs (config, cli, mcp-servers, agents pages); `[GITHUB]` github.com/opencode-ai/opencode, github.com/sst; `[COMMUNITY]` dev.to, developersdigest.tech, diyai.io write-ups (cross-checked against official docs where possible).
