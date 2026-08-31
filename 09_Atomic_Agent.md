# Atomic Agents

## Identity — Important Category Difference
Unlike every other tool in this research set, **Atomic Agents is a Python library/framework, not a standalone CLI agent or terminal tool.** It's meant to be imported into your own code to *build* agents — it does not itself run as a `command` you invoke to "do a coding task" the way Claude Code/Codex/Kimi/OpenCode do.

- Vendor: Open-source community project (maintained by Eigenwise / BrainBlend-AI; multiple GitHub forks exist — `Eigenwise/atomic-agents` is the canonical/maintained one, `eigenwise.github.io/atomic-agents` is the docs site)
- Current version referenced: 2.10.1 (docs site) / 2.6.0 (API reference snapshot)
- Language: Python (a separate unofficial Golang reimplementation exists: `bububa/atomic-agents`)
- PyPI package: `atomic-agents`
- Design philosophy: "Atomic Design" ideas applied to agent architecture — small, reusable, predictable components, explicit input/output schemas, full control over the flow (a deliberate contrast to "autonomous multi-agent swarm" frameworks that prioritize emergent behavior over predictability)

## Core Functionality
- Built on **Instructor** (structured output library) + **Pydantic** (schema validation/serialization)
- `AtomicAgent` class: foundation for building agents — handles chat interactions, history, system prompts, model responses
- All input/output schemas inherit from `BaseIOSchema` (which extends `pydantic.BaseModel`)
- **Atomic Forge**: a collection of pre-built tools you can plug into an Atomic Agent to extend functionality
- **Atomic Assembler CLI**: installed alongside the framework, used to download/manage Tools (and per docs, "soon also Agents and Pipelines")
- Monorepo structure with a documented `docs/` directory covering API reference and how-to guides

## Providers / Models
- Provider-agnostic via Instructor: OpenAI, Anthropic, Groq, Ollama (local models), Gemini, Cohere, and more
- **Omni Router compatibility:** `[INFERRED, likely YES]` — since it relies on Instructor's provider abstraction and already supports arbitrary OpenAI-compatible local servers (Ollama, LMStudio), a custom OpenAI-compatible client pointed at `localhost:20128/v1` should work through the same provider-client pattern, though not explicitly documented for Omni Router by name.

## Claude Code Integration (notable)
- Ships a dedicated Claude Code plugin: `/plugin marketplace add eigenwise/atomic-agents` then `/plugin install atomic-agents@eigenwise`
- This installs **six agent skills**: a framework guide (progressive-disclosure references), four creation workflows (`create-atomic-schema`, `create-atomic-agent`, `create-atomic-tool`, `create-atomic-context-provider`), and a new-app project scaffolder
- Also adds two Claude Code **subagents**: `atomic-explorer` and `atomic-reviewer`
- Documentation site publishes LLM-ready bundles (`llms-full.txt` = docs+source+examples) specifically so an AI assistant can be pointed at the full picture directly — also indexed on **Context7** for assistants using the Context7 MCP server `[OFFICIAL SOURCE: PyPI page, GitHub]`

## MCP
- Atomic Agents does **not appear to be an MCP client/server itself** — its MCP-adjacent presence is entirely through being *indexed* on Context7 (so other MCP-enabled agents can look up its docs) and through the Claude Code plugin packaging. This is a meaningfully different MCP relationship than OpenCode/Codex/Claude Code/Kimi, which connect *outward* to MCP servers — Atomic Agents is consumed *as documentation*, not as a live tool server. `[INFERRED from absence of any MCP-server/client documentation in sources retrieved]`

## Hermes / MCP Control Potential
- This tool is fundamentally different in kind from the other 13 — it's a **library Hermes' own code could import**, not an external process to spawn/control via CLI/PTY/MCP. If Hermes wants to use Atomic Agents, the integration point is "write Python that imports atomic_agents," not "shell out to an atomic-agents binary."
- READ_ONLY / CONTROLLED_WRITE / HIGH_RISK classifications don't map cleanly here since there's no running service to control — the risk surface is whatever the *agents you build with it* do, which depends entirely on the tools you wire into them via Atomic Forge.

## Windows Notes
- Standard Python venv install (`python -m venv venv`, `pip install -r requirements.txt`); docs explicitly show the Windows activation variant (`venv\Scripts\activate.bat`) alongside the Unix one — reasonably well Windows-tested for a community project.

## Evidence Sources
`[GITHUB]` github.com/Eigenwise/atomic-agents, github.com/bububa/atomic-agents (Go reimpl); `[OFFICIAL SOURCE]` eigenwise.github.io/atomic-agents, pypi.org/project/atomic-agents; `[COMMUNITY]` several near-duplicate personal forks found in search results (htcd-subham, segmond, mHz28, tonymaniaci) — these appear to be simple GitHub forks of the same upstream project rather than independent implementations, so treat `Eigenwise/atomic-agents` as the canonical source.
