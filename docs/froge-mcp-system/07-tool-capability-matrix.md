# 07 — Tool Capability Matrix

This is a planning matrix, not a claim that every integration already works.

| Tool | Type | Research signal | FROGE integration approach | Current status |
|---|---|---|---|---|
| Hermes | master agent | MCP consumption `[UNKNOWN]` | MCP client + FROGE skill | DESIGN |
| OpenCode | coding agent | CLI, headless, server, ACP documented | CLI/server/ACP adapter | RESEARCHED |
| OmniRoute | AI gateway + MCP surface | localhost OpenAI API + MCP documented; auth details `[UNKNOWN]` | dedicated gateway adapter | RESEARCHED |
| Codex | coding agent | CLI + MCP client/server + sandbox/approval | CLI/MCP adapter | RESEARCHED |
| Claude Code | agentic CLI | CLI, MCP, hooks, subagents | CLI/MCP adapter | RESEARCHED |
| Prime Agent | coding/research harness | Windows installer not found; no native MCP documented | isolated process/WSL path only after verification | HIGH-RISK / UNKNOWN |
| Atomic Agents | Python framework | library, not standalone worker CLI | Python SDK/library adapter | RESEARCHED |
| OpenClaw | personal AI assistant/gateway | gateway documented; MCP surface `[UNKNOWN]` | gateway/API adapter after direct verification | RESEARCHED |
| Freebuff/Codebuff | coding agent | CLI documented; MCP/custom endpoint `[UNKNOWN]` | CLI adapter after direct verification | RESEARCHED |
| DeepSeek Harness | agent harness | plugin architecture + Codex/Claude delegation | CLI/plugin adapter after direct verification | RESEARCHED |
| NemoClaw | OpenClaw plugin + sandbox | OpenAI-compatible inference path strongly documented | sandbox/runtime adapter | RESEARCHED |
| Pi Agent | coding harness | RPC/SDK documented; native MCP intentionally absent | RPC/SDK adapter or extension | RESEARCHED |
| Strix | security tool | operational details `[UNKNOWN]` | no adapter until evidence exists | UNKNOWN |

## Verification rule

`RESEARCHED` means only that the research archive contains information worth investigating. It does not mean FROGE can currently control the tool.

Each row becomes `VERIFIED` only after a real test against a concrete version and interface.

## Priority

1. Hermes connection to FROGE.
2. OpenCode / Pi / Codex / Claude Code — strongest direct worker-control candidates.
3. OmniRoute — separate routing/control integration.
4. NemoClaw/OpenClaw — security/runtime integration after direct interface verification.
5. DeepSeek Harness / Freebuff / Prime Agent / Atomic Agents / Strix — based on concrete requirements and verification results.
