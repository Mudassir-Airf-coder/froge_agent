# Claude Code

## Identity
- Vendor: Anthropic
- Category: Agentic CLI ("general computer automation" tool, not purely coding) — also available as VS Code/JetBrains extensions, standalone desktop app (macOS/Windows), web app at claude.ai/code, iOS, plus an embeddable Claude Agent SDK (TypeScript/Python), GitHub Action, and GitHub App `[COMMUNITY, well-corroborated across multiple 2026 guides]`
- Requires a Claude Pro/Max or Team/Enterprise subscription (or API billing)
- The CLI is described as the **reference surface** — every other channel (VS Code, JetBrains, desktop, web) mirrors a subset of its tools `[COMMUNITY]`

## Core Systems (five pillars per multiple independent guides)
1. **Configuration hierarchy** (settings.json, CLAUDE.md project memory files)
2. **Permissions** — tool/path/URL allow-deny rules
3. **Hooks** — automated actions at lifecycle events
4. **MCP** — external tool/server connections
5. **Subagents** — isolated-context delegated workers

## Hooks (deep)
- Event-driven automation: hook types include `command` (bash), `prompt` (LLM), `http` (webhook), `mcp_tool` (MCP tool invocation, v2.1.118+), and `agent` (subagent-based verification) `[GITHUB: luongnv89/claude-howto]`
- Config shape:
 ```json
 { "hooks": { "EventName": [ { "matcher": "ToolPattern", "hooks": [ { "type": "command", "command": "...", "timeout": 60 } ] } ] } }
 ```
- Known lifecycle events referenced: PreToolUse, PostToolUse (runs before/after every tool execution), plus session-level events
- Matchers do **exact** matching as of a recent version fix (v2.1.195+) — hyphenated tool names no longer accidentally substring-match

## Subagents
- A subagent = a separate Claude session launched via the **Task tool**, with its own context window — used for context isolation and parallelism
- Built-in subagents: **Explore** (file discovery), **Plan** (codebase research), **General-purpose** (complex multi-step tasks)
- "Agent teams" (2026 terminology): splitting larger work across specialized subagents (planning, implementation, test repair, security review, docs, migration, browser QA, release notes)
- Custom subagents can be created with their own system prompt, model, and permission set (deny-by-default: "anything you don't select is denied")

## MCP (deep)
- MCP connects Claude Code to external services: issue trackers, databases, monitoring, browser automation, design tools, docs, internal APIs — Anthropic's own docs frame usage around concrete tasks (implementing from JIRA issues, checking monitoring, etc.)
- Third-party wrapper example found: **Shannon MCP Server** — a Python-implemented MCP server that gives *programmatic control over Claude Code itself* (session management, hooks, checkpoints, analytics) — this is directly relevant as a template for a future Hermes-controls-Claude-Code MCP design: 7 MCP tools, 3 MCP resources, binary discovery/version-checking, checkpoint (git-like) system `[GITHUB: krzemienski/shannon-mcp]`

## Skills / Plugins
- **Skills**: domain-expertise packages Claude applies automatically or on manual trigger (`disable-model-invocation: true` for manual-only; `context: fork` to run a skill in a subagent)
- **Plugins**: versioned bundles that can ship skills + subagents + slash commands + hooks + output styles + MCP server definitions together as one installable unit — the canonical way to share reusable Claude Code extensions across a team or public marketplace, installed with one `/plugin` command

## Other Notable Features
- **Worktree isolation** for parallel agent runs (referenced in "April 2026 update" notes: deferred tool loading, worktree isolation, agent teams)
- **statusLine**: customizable status bar (model in use, cwd, context usage) via `settings.json`, can run an external script
- Backgrounded shell commands: `run_in_background` flag on the Bash tool lets long-running commands run without blocking the conversation; Claude gets notified on completion and can poll output

## Model Tiering
- Opus for complex reasoning, Sonnet for general work, Haiku for fast/cheap exploration — subagent work can be routed to cheaper models while reserving Opus for architectural reasoning

## Hermes / MCP Control Potential
- READ_ONLY: session/checkpoint inspection, hook config read, `/mcp` status
- CONTROLLED_WRITE: subagent dispatch for bounded work, hook-triggered lint/format/security checks, MCP tool calls scoped by permission allow-lists
- HIGH_RISK: unrestricted Bash tool access, any hook of type `command` with unreviewed shell content, plugin installs from untrusted marketplaces
- The Shannon MCP precedent shows this is a well-trodden path — a Hermes-facing Claude Code MCP is very buildable, following that project's tool/resource split as a reference architecture.

## Windows Notes
`[UNKNOWN]` — CLI is cross-platform, desktop app ships for Windows; no PowerShell-specific caveats surfaced in this documentation pass (would need local verification, which was explicitly out of scope this round).

## Evidence Sources
`[COMMUNITY, well cross-corroborated]` alexop.dev, hidekazu-konishi.com, jitendrazaa.com, blakecrosley.com, developersdigest.tech, luongnv89/claude-howto (GitHub); `[GITHUB]` krzemienski/shannon-mcp specification doc. No official Anthropic docs page was directly fetched in this pass — recommend a follow-up direct fetch of docs.claude.com/claude-code for primary-source confirmation of exact current hook/MCP schema.
