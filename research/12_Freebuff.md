# Freebuff

## Identity
- Vendor: Codebuff / Freebuff, Inc. — Freebuff is the **free, ad-supported tier** of a broader platform called **Codebuff**
- Codebuff itself was originally launched under the name **"Manicode"** in 2024, then renamed to Codebuff after a trademark dispute `[COMMUNITY: ai.miraheze.org]` — this directly explains "ManiCode" in your original 20-tool list; **ManiCode = Codebuff's original 2024 name**, now fully superseded. (Per your instruction, ManiCode itself was removed from active research scope, but this lineage is worth recording since Freebuff remains in scope and is its direct descendant.)
- Founders: James Grugett and Brandon Chen (San Francisco); Y Combinator Fall 2024 batch; Grugett also co-founded Manifold Markets
- License: Codebuff core is Apache 2.0, open-source
- Freebuff launched March 2026

## Core Functionality
- Multi-agent architecture — four specialized agents divide labor rather than one monolithic model:
 - **File Picker Agent** — scans codebase (~2 seconds per one source), maps architecture, finds relevant files
 - **Planner Agent** — breaks the task into an ordered plan
 - (Execution and Review agents implied by "coordinate to handle file selection, planning, code editing, and review" — exact 4th/5th agent names varied slightly across sources, treat the 4-agent count as approximate `[COMMUNITY, self-reported by vendor via multiple secondary write-ups]`)
- Model-agnostic via OpenRouter — not locked to a single provider
- Built-in web research and browser automation capabilities
- CLI: `npm install -g freebuff`; supports file mentions (`@filename`), agent mentions (`@AgentName`), bash mode, chat history, knowledge files
- Multi-surface: CLI, Desktop (beta, macOS/Windows/Linux, parallel workspaces), Web (prompt-to-deployed-app builder), Cloud (GitHub-integrated dev environments)

## Free/Ad Model (notable, unique among this tool set)
- **No subscription, no API key, no credit card required** for core functionality
- Funded via **text-based advertisements displayed in the terminal** — this is architecturally unusual and worth flagging explicitly for any Hermes integration: a Freebuff-wrapping MCP tool would need to handle/strip or account for ad content in CLI output, which no other tool in this research set requires
- Uses free/open-weight models: DeepSeek V4 Pro/Flash, MiniMax M3, GPT 5.6 Luna (free sessions as of a specific date), Gemini 3.1 Flash Lite referenced across sources (model lineup changes frequently — treat any specific model name here as a snapshot, not current)
- Vendor claims of "no training on your data," no codebase storage, and "5-10x faster than Claude Code" are **self-reported marketing claims**, not independently verified benchmarks — flag as `[COMMUNITY, vendor-originated, unverified]`

## Providers / Models
- **Omni Router compatibility:** `[UNKNOWN]` — Freebuff already routes through OpenRouter-style model selection internally; whether it accepts a *fully custom* endpoint like Omni Router's localhost gateway wasn't confirmed in sources retrieved. Given it's already provider-agnostic, this is plausible but unconfirmed.

## MCP / Hooks / Automation
`[UNKNOWN]` — no MCP client/server documentation surfaced for Freebuff/Codebuff in this research pass. This is a **documentation gap**, not evidence of absence — worth a direct follow-up fetch of the Codebuff GitHub repo/docs if MCP integration with Freebuff specifically is needed.

## Hermes / MCP Control Potential
- READ_ONLY: session/chat history inspection
- CONTROLLED_WRITE: CLI-driven file edits via the multi-agent pipeline, `@AgentName` targeted dispatch
- HIGH_RISK: bash mode (raw shell execution), the ad-supported model's dependency on an external ad-serving system that Hermes has no control over — if uptime/reliability matters, note that Freebuff's business model introduces a dependency (ad servers, free-tier model availability) that paid/self-hosted tools in this set don't have.

## Windows Notes
- Desktop app explicitly supports Windows (beta); CLI via npm should be cross-platform. No PowerShell-specific caveats surfaced.

## Evidence Sources
`[COMMUNITY]` ai.miraheze.org (Codebuff/Manicode lineage — treat as reasonably reliable given specific, checkable claims like the YC batch and trademark-dispute rename), stork.ai, everydev.ai, ailistify.com, bizrescuepro.com, saascity.io — no official Codebuff/Freebuff primary-source docs page was directly fetched in this pass; all findings here are secondary-source and should be verified against the actual GitHub repo before being treated as authoritative for an MCP design.
