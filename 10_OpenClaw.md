# OpenClaw

## Identity
- Vendor: OpenClaw Foundation (non-profit); creator Peter Steinberger (Austrian agentic engineer)
- Category: Self-hosted, open-source **personal AI assistant**, primarily messaging-first (not a coding-agent CLI in the same category as Claude Code/Codex — closer in spirit to Hermes's own design goal)
- Name history: Warelay (Nov 2025) → Clawdis (Dec 2025) → Clawdbot (Jan 2, 2026) → Moltbot (Jan 27, 2026) → **OpenClaw** (Jan 30, 2026) `[GITHUB / Wikipedia]`
- License: MIT
- Written in: TypeScript + Swift
- Scale: 247K–346K+ GitHub stars through 2026 (rapid growth, viral due to the associated "Moltbook" social network for AI agents)
- Repo: github.com/openclaw/openclaw

## Core Functionality
- Runs locally on the user's own hardware; connects to **50+ integrations**
- Access channels: WhatsApp, Telegram, Discord, Signal, iMessage, GitHub (as a native channel), and 12+ other messaging platforms — architecturally very similar in spirit to Hermes's WhatsApp-bridge design
- Everything routes through **one Gateway** that connects models, tools, messaging channels, and optional companion apps for a single operator
- Personality/behavior defined via a **`SOUL.md`** file per agent (community template packs exist with 100+ personality templates)
- **ClawHub**: skill marketplace — "only install skills from verified publishers, review SKILL.md before installing" (official security guidance)
- Companion products: **ClawdTalk** (phone calling/SMS via Telnyx), **clawr.ing** (bot gets a real phone number and can call you)

## Installation
- macOS/Linux/WSL2: `curl -fsSL https://openclaw.ai/install.sh | bash`
- **Windows PowerShell**: `iwr -useb https://openclaw.ai/install.ps1 | iex` — native Windows installer exists `[OFFICIAL SOURCE: github.com/openclaw/openclaw]`
- Also installable via `npm install -g openclaw@latest --allow-scripts=openclaw` (Node.js 22.22.3+/24.15+/25.9+)
- Notably: Microsoft has shown OpenClaw running **natively on Windows inside Microsoft Execution Containers** ("the Windows node and gateway run contained, so your system stays secure" — quote attributed to Windows EVP Pavan Davuluri at a Build keynote) — this is a strong signal for safe Windows sandboxing if OpenClaw is ever integrated `[OFFICIAL SOURCE quote, vendor-published]`
- Repository is a **pnpm workspace** — plain `npm install` at the repo root is explicitly unsupported; must use `pnpm install && pnpm build && pnpm ui:build`

## Security Posture (explicit, from official docs)
- "Tools run on the host for the main session unless you configure sandboxing" — sandboxing is opt-in, not default
- Official guidance explicitly points to a security guide, an "exposure runbook," and a sandboxing guide **before connecting other users or exposing the Gateway remotely**
- Community best-practices list (from an awesome-openclaw-agents repo): bind to localhost only, use SSH tunneling for remote access, **never expose port 18789 to the internet**, store keys in `.env` (gitignored), rotate keys, only install ClawHub-verified skills, set strict rules in SOUL.md, limit filesystem access, disable shell commands for untrusted inputs, use HEARTBEAT.md with scope limits and budget caps, enable logging for all actions `[COMMUNITY, but directly mirrors official OpenClaw security-doc structure]`

## Providers / Models
- Model-agnostic — a companion "one interface, every AI model" Swift SDK exists in the openclaw GitHub org for provider interfacing
- Users have reported signing in with a ChatGPT subscription directly ("you can sign in to openclaw with your chatgpt account now")
- **Omni Router compatibility:** `[UNKNOWN]` — no explicit custom-gateway config documented in sources retrieved, though the provider-agnostic design makes it architecturally plausible.

## MCP / Automation
`[UNKNOWN]` — no explicit MCP client/server documentation was surfaced in this pass for OpenClaw specifically (note: do not confuse with "awesome-hermes-agent," a **different, unrelated** project referenced as OpenClaw's "most common upgrade path" via a `hermes claw migrate` command — this is a naming coincidence with your own Hermes project, not the same thing, and should be flagged clearly to avoid future confusion in your ecosystem docs).

## Hermes / MCP Control Potential
- OpenClaw is architecturally the closest public analog to Hermes itself (self-hosted, messaging-gateway-first, skill-based). It is **not obviously a tool Hermes would "control" like a coding CLI** — it's more of a peer/competitor architecture, or a reference design to borrow patterns from (e.g. SOUL.md-style behavior definition, the "one Gateway" pattern, the never-expose-port-18789 security posture).
- If integration is desired, treat it as a **separate agent process** to bridge via its own channel APIs (Telegram/Discord/GitHub) rather than assuming CLI/MCP control until confirmed.

## Evidence Sources
`[GITHUB]` github.com/openclaw/openclaw (official repo, high confidence), github.com/SamurAIGPT/awesome-openclaw, github.com/mergisi/awesome-openclaw-agents; `[OFFICIAL SOURCE]` openclaw.ai; `[COMMUNITY]` openclawguide.org. The Wikipedia-style naming-history table is treated as `[COMMUNITY]` despite its structured format since it wasn't a primary vendor source.
