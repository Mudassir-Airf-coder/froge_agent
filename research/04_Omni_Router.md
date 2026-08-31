# Omni Router (OmniRoute)

## Identity
- Project name in public sources: **OmniRoute** (this is almost certainly what "Omni Router" in the master prompt refers to)
- Category: Self-hosted, open-source, MIT-licensed **local AI gateway** — a single OpenAI-compatible endpoint that fronts many providers
- License: MIT; installs via `npm install -g` (global npm package), Docker, pnpm, AUR, Nix
- Community traction: 20K–30K+ GitHub stars range through mid/late 2026, rapidly growing `[COMMUNITY, multiple corroborating sources]`

## Core Functionality
- Runs a **local server on port 20128 by default**, exposing an OpenAI-compatible API at `http://localhost:20128/v1` `[OFFICIAL SOURCE: omniroute.online, corroborated by 4+ independent write-ups]`
- Aggregates **~230–340 providers** (figures vary by article date — the project is moving fast): major labs (OpenAI, Anthropic, Google Gemini, xAI Grok, DeepSeek, Mistral, Qwen, Meta Llama, Groq, NVIDIA) plus a long tail of smaller/free-tier hosts (90+ with free tiers, 40+ "free forever")
- **`auto` model**: send `"model": "auto"` and OmniRoute picks a provider itself, with automatic fallback on quota/failure
- Reliability features: circuit breakers, exponential backoff, per-key/per-connection cooldowns
- **Compression pipeline**: multiple engines (referenced as RTK, Caveman, LLMLingua-2 in different sources) can shrink prompts before sending upstream, claimed 15–95% token savings
- **Routing strategies**: reported counts range 17–19 across sources (priority, round-robin, cost-optimized, auto-scoring, fusion, strict-random, etc.) — exact current count should be verified against the live docs since the project updates frequently
- Web dashboard for provider/credential management and usage visualization
- Notion & Obsidian integration exposed **as MCP tools** — i.e., OmniRoute itself can expose your notes/vault as context to any connected model `[OFFICIAL SOURCE: omniroute.online]`

## MCP (deep)
- OmniRoute acts as **both an MCP client and an MCP server**:
 - As MCP client: aggregates other gateways (Bifrost, "9Router", CLIProxy) as managed sidecars
 - As MCP server: exposes itself at `http://localhost:20128/api/mcp/stream` — example shown: `claude mcp add omniroute --type http --url http://localhost:20128/api/mcp/stream` yielding ~95-105 tools available to the connecting agent `[OFFICIAL SOURCE]`
- This means OmniRoute is a genuine **control surface** in its own right — Hermes (or any MCP client) could connect to OmniRoute's MCP endpoint and get a large bundle of tools (Notion, Obsidian, sidecar gateways) in one hop, not just LLM routing.

## Security Features
- Prompt-injection guard on every route
- Opt-in PII redaction
- Safety content-filter normalization
`[OFFICIAL SOURCE, unverified independently]`

## Authentication
- Provider API keys entered via the dashboard; a free-tier provider is enough to make a first call without any paid key
- OmniRoute's own MCP endpoint auth model: `[UNKNOWN]` — not detailed in sources retrieved; verify before exposing beyond localhost

## Integration Ecosystem
- Explicitly documented integration targets: Claude Code, Cursor, Copilot, and "16+ agents" generally, via the OpenAI-compatible base URL swap
- VS Code extension "OmniCopilot" surfaces OmniRoute models directly in the native model picker

## Hermes / MCP Control Potential
- READ_ONLY: dashboard status, provider list, usage stats
- CONTROLLED_WRITE: adding/removing provider credentials, changing routing strategy, toggling compression
- HIGH_RISK: none inherent to OmniRoute itself, but by design it becomes the **single point of failure/control** for every tool routed through it — a compromised OmniRoute instance affects everything behind it. This makes OmniRoute a natural **first integration target** for Hermes's master MCP (control the router, and you gain leverage over every tool that points at it), but also the highest-value security target to lock down (bind to localhost only, per its own docs' security guidance).

## Windows Notes
`[UNKNOWN]` — npm/Docker-based install should work on Windows; no explicit Windows caveat surfaced.

## Evidence Sources
`[OFFICIAL SOURCE]` omniroute.online; `[COMMUNITY]` medium.com (Fazal), provenlabs.ai, pinggy.io, ai-tldr.dev, explainx.ai — cross-corroborated across 6 independent sources on the localhost:20128 endpoint and multi-provider claim, so this is reasonably solid despite being entirely community-documented (no single canonical GitHub README was directly retrieved in this pass — recommend a follow-up direct fetch of the GitHub repo for exact current version/config schema).
