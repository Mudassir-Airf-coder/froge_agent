# Hermes AI

`[STATED]` = from Mudassir's own prior descriptions (not externally verifiable; Hermes is a personal project, not a public product).

## Identity
- Vendor: Mudassir (personal build)
- Category: WhatsApp-connected autonomous agent; operational layer of the wider "Jarvis" ecosystem (Jarvis = the locally-run multi-agent AI OS Mudassir is building)
- Access surfaces: WhatsApp bridge (Baileys, E.164 phone format, gateway on port 3000) and terminal

## Core Functionality
- Skills system: can write/push code, generate documents, manage multi-step workflows
- Scope boundary: writes and logically reviews code but does **not execute** it — Mudassir tests locally and feeds back logs/errors for fixes. This is an important control boundary for any future MCP wrapper: a Hermes-control-MCP should not silently grant execution rights beyond this design intent.
- LangChain Learning Pipeline: numbered project repos under the `MudassirBuilder-collab` GitHub org, stored locally at `D:\gen\`; each project folder has `main.py`, `streamlit_main.py`, `requirements.txt`
- Uzair document automation skill: generates Traffic Awareness Program `.docx` files with dynamic place/date formatting, using character-count spacing instead of tab stops; stored at `D:\Uzair bhai\`
- Hermes Intelligence System: background cron-based API-key failover — detects provider/key failures and issues **direct commands** (not suggestions) specifying which key to use next, following a fixed priority chain. Zero-hallucination-tolerance design goal.

## MCP / Control Surface
`[UNKNOWN]` — no evidence Hermes currently exposes or consumes MCP. Given the master-prompt's stated goal (Hermes as top-level orchestrator issuing MCP calls to control OpenCode/Codex/Claude Code/etc.), Hermes today looks like the **controller**, not a controllable MCP server itself. Building an MCP interface *for* Hermes (so other systems could invoke it) is future work, not something in place now.

## Automation / Integration Notes
- Since Hermes never executes code itself, any Hermes→tool control chain (e.g., Hermes telling Claude Code or OpenCode to actually run something) needs its own execution boundary defined — this is a design decision, not yet documented anywhere as implemented.
- The failover system's "direct commands, not suggestions" pattern is worth reusing as a control philosophy if Hermes becomes the master orchestrator over the other 14 tools: deterministic dispatch instructions rather than advisory ones.

## Evidence
`[STATED]` throughout — sourced from Mudassir's own memory file, not independently verified (Hermes is not a public/discoverable product).
