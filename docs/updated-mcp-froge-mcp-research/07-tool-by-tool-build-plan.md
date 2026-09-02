# 07 — Tool-by-Tool Build Plan

## Principle

Do not build all MCPs at once. Build one MCP, verify it end-to-end with Hermes, freeze its skill/evidence, then move to the next MCP.

## Research set

The current research set contains:

- Hermes — master/orchestrator, not a worker MCP.
- OpenCode
- Omni Router
- Codex
- Claude Code
- Prime Agent
- Atomic Agents
- OpenClaw
- Freebuff/Codebuff
- DeepSeek Harness
- NemoClaw
- Pi Agent
- Strix

The exact MCP inclusion set must be decided from the research evidence and the user's final selected tool list. Tools with no verified integration surface must be marked `BLOCKED` or `UNSUPPORTED`, not forced into implementation.

## Recommended build sequence

### Track A — first worker MCPs

1. OpenCode MCP
2. Pi Agent MCP
3. Codex MCP
4. Claude Code MCP

These are useful early candidates because the research contains concrete integration surfaces that can be tested.

### Track B — runtime/router integrations

5. Omni Router MCP
6. OpenClaw MCP
7. NemoClaw MCP
8. DeepSeek Harness MCP

Build these only against their documented/verified interfaces.

### Track C — remaining ecosystem tools

9. Atomic Agents MCP
10. Freebuff/Codebuff MCP
11. Prime Agent MCP
12. Strix MCP

The research for some of these may be incomplete. A blocked/unsupported result is a valid engineering outcome.

## Per-tool workflow

For every MCP:

```text
READ RESEARCH
   -> IDENTIFY REAL INTERFACE
   -> DESIGN MCP
   -> IMPLEMENT
   -> WRITE SKILL
   -> LOCAL UNIT TESTS
   -> REAL TOOL TEST
   -> HERMES CONNECT TEST
   -> REAL TASK CONTROL TEST
   -> FAILURE/PERMISSION TEST
   -> DOCUMENT EVIDENCE
   -> MARK VERIFIED/BLOCKED/UNSUPPORTED
```

Only after a tool reaches a stable verified state should it be added to the combined FROGE runtime.
