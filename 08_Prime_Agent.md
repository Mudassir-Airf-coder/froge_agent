# Prime Agent

## Identity
- Vendor: Prime Intellect (company raised $130M July 2026 at $1B valuation; backers include Radical Ventures, NVIDIA Ventures, Intel Capital)
- Category: Self-improving, open-source coding/research harness — released August 5–6, 2026, MIT-licensed
- Repo: github.com/PrimeIntellect-ai/prime-agent
- Install: `curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh` — installs on **macOS or Linux only** (no native Windows install script found) `[OFFICIAL SOURCE + AI Wiki]`
- Runtime: verified SHA-256 checksum on install; prepares a Python runtime for the agent

## Core Architecture — Two Key Abstractions
1. **Recursive Language Model (RLM)**: treats context as a variable and subagent delegation as **function calls inside a persistent Python REPL** (IPython kernel) rather than the usual fixed tool-schema + context-compaction pattern most agents use
2. **Continual Harness**: manages system state across four areas — prompt, sub-agents, skills, memory — stored as durable local files. Triggered updates via `/refine` convert successful execution trajectories into small, evidence-backed harness improvements over time (i.e., the agent literally rewrites its own instructions/skills based on what worked)

## Core Functionality
- Persistent IPython REPL: context window contents exist as **live Python variables**, not just text history
- Subagents are standard function calls — launched programmatically, return immediately on admission, deliver results **asynchronously** without blocking the main execution
- Messaging restricted to immediate parent/child/sibling agents only (prevents cross-session chatter)
- Inactive subagents auto-drop from memory after **30 minutes idle**
- "Background Daemon and Agents View" — default TUI view; IPython actions are condensed by default but can be expanded
- Long-task support: automatic compaction, persistent goals, heartbeats, schedules, autonomous mode, retained subagents that preserve progress across turns/terminal sessions
- `/resume [id|path]` slash command, or bare `prime-agent --resume`, reopens the agents view / resumes a specific session

## Providers / Models
- Model-agnostic: authenticate with a subscription (ChatGPT Plus/Pro via Codex, Claude Pro/Max, GitHub Copilot) **or** direct API keys from Anthropic, OpenAI, Google, DeepSeek, xAI, Mistral, Groq, Cerebras, OpenRouter, Hugging Face, MiniMax, Kimi For Coding, or Prime Intellect's own **Prime Inference** service `[OFFICIAL SOURCE, per AI Wiki summary of repo docs]`
- OpenAI has reportedly endorsed Codex-subscription use under a "Codex for OSS" program; Anthropic subscription use via third-party harnesses like this is billed as extra usage, not counted against plan limits
- **Omni Router compatibility:** `[UNKNOWN]` — no explicit custom-endpoint/OpenAI-compatible-gateway config was surfaced in sources; given the breadth of already-supported providers, adding a generic OpenAI-compatible endpoint is plausible but unconfirmed.

## Security Warning (explicit, from the project's own docs)
- Prime Agent **executes model-generated Python and project commands with the user's own permissions**
- The project's own isolation measures are explicitly stated to be **"not a security sandbox"**
- Official recommendation: use disposable clones or external sandboxes for untrusted work `[OFFICIAL SOURCE — direct from repo docs, high confidence]`
- This is the single most important safety flag among all 14 tools researched here — Prime Agent should be treated as HIGH_RISK by default for any Hermes integration, and never given a shared/production working directory without an external sandbox layer.

## Benchmarks (self-reported)
- 95.5% on ARC-AGI-3 with Opus 5, reportedly above the stated human-expert baseline of 95.4% `[OFFICIAL SOURCE / MarkTechPost, self-reported by Prime Intellect — treat as a vendor claim, not independently audited]`

## Known Limitations (community-reported)
- Some developers report code bloat in generated files
- Heavy use of the self-improvement loop (`/refine`) can get expensive at current model pricing

## MCP / Hooks / Plugins
`[UNKNOWN]` — no MCP-specific documentation was surfaced for Prime Agent in this pass. Given its Python-REPL-first design (function calls instead of tool schemas), it may not follow the standard MCP client pattern used by OpenCode/Codex/Claude Code — this needs direct verification against the GitHub repo docs before assuming MCP compatibility.

## Hermes / MCP Control Potential
- READ_ONLY: `/resume` session listing, agents view inspection
- CONTROLLED_WRITE: subagent dispatch as function calls (bounded, since messaging is restricted to parent/child/sibling)
- HIGH_RISK: **everything else** — the tool's own docs flag full local-permission code execution with no built-in sandbox. Any Hermes wiring must add its own sandbox layer (disposable clone/worktree/container) before delegating real tasks to Prime Agent.

## Windows Notes
- **No native Windows install path found** (macOS/Linux only via the install script). If Windows use is required, WSL2 is the likely path, though this is `[INFERRED]`, not confirmed in the sources retrieved.

## Evidence Sources
`[OFFICIAL SOURCE]` github.com/PrimeIntellect-ai/prime-agent (README + releases), primeintellect.ai/blog/prime-agent; `[COMMUNITY]` dev.to (terminalchai), opensourceforu.com, marktechpost.com, byteiota.com, aiwiki.ai — strong cross-corroboration on architecture and the explicit "not a security sandbox" warning across independent sources.
