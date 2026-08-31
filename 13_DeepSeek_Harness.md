# DeepSeek Harness

## Identity — Important Disambiguation
Two things share this name; only one is official:
- **Official**: `deepseek-ai/deepseek-harness` on GitHub — DeepSeek AI's own open-sourced agent harness, CLI command `dsh`, released ~August 2026, MIT-licensed, currently in **developer preview** with explicit warning: "THERE WILL BE COMPATIBILITY-BREAKING CHANGES" `[OFFICIAL SOURCE: github.com/deepseek-ai/deepseek-harness]`
- **Unofficial/community**: a separate third-party project called `deepseek-harness` by a different GitHub user (HenryZ838978), described as a protocol-aware adapter/wrapper for DeepSeek V4-Pro/V4-Flash — **not the same project**, released May 2026, ships as Python library/CLI/MCP server/Anthropic Skill. Do not conflate these two when integrating.

## Core Architecture (official DeepSeek Harness)
- Built on **Cordis**, a "meta-framework for spatiotemporal composability" — described in an academic paper by researchers from Peking University and DeepSeek
- Design philosophy: **"Everything is a Plugin"** — model adapter, tool registry, and agent loop are all swappable plugins
- Two composability axes:
 - **Spatial**: mount/replace/extend any part (tools, memory, sub-agents, UI components) as plugins without breaking the rest
 - **Temporal**: behaviors/workflows composed across time — sequential steps, persistent state, replayable sessions

## Core Functionality
- Local **Web UI**, not CLI-only — `npx @deepseek-ai/dsh web` starts a local server on `http://127.0.0.1:3080` and opens it in the default browser
- Documentation: deepseek-harness.github.io/deepseek-harness/
- **Code Mode**: exposes tools through code-based execution, giving the agent more control over combining/running tool calls
- **Trajectory view**: step-by-step inspection of agent actions — model responses, tool calls, nested tool activity, timing, token usage
- **Session statistics**: turns, steps, model time, tool time, time-to-first-token, decoding time
- **Subagents**: main agent can delegate parts of a task to child agents
- **Community plugins**: third-party plugins add capabilities not in the base model (example given: a vision-support plugin called ModLens)
- **Four presets** referenced (exact names not fully retrieved in this pass, but "Standard mode gives developers the full coding agent" is confirmed) `[OFFICIAL SOURCE / TheNewStack]`
- **Creator mode**: lets the agent help build its own extensions — a self-improving/self-extending loop
- **Subagent delegation to OTHER coding agents**: ships with subagent providers that can delegate directly to **Anthropic's Claude Code and OpenAI's Codex** — resolving each product's binary from the host PATH, so the user supplies install+login. **Both ship switched off by default** `[OFFICIAL SOURCE / TheNewStack, high confidence — this is a very specific, checkable claim]`

## Providers / Models
- Provider catalog: Anthropic, OpenAI, AWS Bedrock, Microsoft Azure, Google's Gemini Enterprise Agent Platform (docs still internally call it "Vertex"), plus DeepSeek's own endpoint
- **Custom OpenAI-compatible gateways explicitly supported** for other inference providers — this is a first-class, explicitly documented feature, not inferred
- Can be pointed at local model servers such as **Ollama** or "any OpenAI-compatible endpoint on your network" `[OFFICIAL SOURCE, corroborated: howdoiuseai.com]`
- **Omni Router compatibility:** `[INFERRED, HIGH confidence]` — given the explicit "any OpenAI-compatible endpoint on your network" support, pointing DeepSeek Harness at `localhost:20128/v1` should work without any special-case handling. This is the strongest inferred compatibility of any tool in this research set, though still not confirmed by name.

## MCP / Hooks
`[UNKNOWN]` — no explicit MCP client/server documentation was surfaced in this pass beyond the general "everything is a plugin" architecture, which *could* subsume MCP as one plugin type, but this wasn't confirmed directly.

## Hermes / MCP Control Potential
- Because DeepSeek Harness can itself **delegate to Claude Code and Codex as subagents**, it is architecturally an *orchestrator* in its own right, similar in spirit to what Hermes aims to become. Two integration models are possible:
 1. Treat DeepSeek Harness as **one more worker** Hermes dispatches to (standard model)
 2. Treat DeepSeek Harness as a **peer orchestrator** that Hermes could delegate broad tasks to, letting DSH's own Claude-Code/Codex subagent providers handle the fan-out (reduces Hermes's own orchestration burden, but reduces Hermes's visibility/control over what actually ran)
- READ_ONLY: Trajectory view, session statistics
- CONTROLLED_WRITE: subagent dispatch (own or delegated to Claude Code/Codex), Code Mode tool execution
- HIGH_RISK: enabling the Claude-Code/Codex subagent providers (off by default for a reason — this creates a chain-of-trust across three separate tools at once) and running in developer preview with breaking-change risk

## Windows Notes
`[UNKNOWN]` — `npx` install path suggests cross-platform Node.js support, but no explicit Windows documentation surfaced.

## Evidence Sources
`[OFFICIAL SOURCE]` github.com/deepseek-ai/deepseek-harness (README, high confidence); `[COMMUNITY]` thenewstack.io (strong, detailed technical reporting), medium.com (Mehul Gupta), mindstudio.ai, datacamp.com, codepick.dev, howdoiuseai.com, deepseek-code.com — cross-corroborated on the Cordis/plugin architecture and Claude-Code/Codex subagent delegation across 3+ independent sources.
