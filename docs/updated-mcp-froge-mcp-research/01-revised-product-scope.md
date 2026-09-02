# 01 — Revised Product Scope

## Objective

Create a modular MCP ecosystem in which each researched tool is represented by its own dedicated MCP, then package and manage those MCPs as one FROGE MCP system for Hermes.

## Product layers

### Layer 1 — Tool

The real worker/runtime: OpenCode, Codex, Claude Code, Pi Agent, OpenClaw, NemoClaw, DeepSeek Harness, Atomic Agents, Freebuff/Codebuff, Prime Agent, Strix, or another explicitly supported tool.

### Layer 2 — Tool-specific MCP

One MCP per supported tool. It translates Hermes-facing MCP requests into the underlying tool's verified interface: CLI, API, RPC, SDK, extension mechanism, or another supported integration surface.

### Layer 3 — FROGE MCP System

The system that installs, configures, starts, stops, health-checks, authenticates, and manages the collection of individual MCPs.

### Layer 4 — Hermes

Hermes is the master. It interprets the user's intent, chooses the appropriate MCP, plans the work, decides when to retry/switch/ask for approval, and consumes the MCP results.

## In scope

- Separate MCP implementation for each selected tool.
- Independent build and test cycle for every MCP.
- Real Hermes-to-MCP connection testing.
- Real MCP-to-underlying-tool control testing.
- Dedicated skill file for every MCP.
- A common way to discover installed/available MCPs.
- One FROGE installation that packages/manages the MCP collection.
- One system startup command.
- Secure runtime token/authentication.
- MCP process lifecycle management.
- Health/status/error reporting.
- Idempotent setup and startup.
- Evidence-backed release gates.

## Out of scope

- Replacing Hermes as master.
- Building one giant MCP containing every tool implementation.
- Inventing integration interfaces when research does not prove them.
- Removing the security model of the underlying tools.
- Treating a successful process launch as proof of tool control.

## Acceptance criteria

The final system is accepted only when all required MCPs can be independently demonstrated to:

1. Start successfully.
2. Expose the documented capabilities.
3. Authenticate correctly.
4. Connect to Hermes.
5. Receive a valid task from Hermes.
6. Control the underlying tool through its verified interface.
7. Return useful status/result/error information.
8. Respect configured permissions and execution boundaries.
9. Be stopped/restarted by the FROGE lifecycle layer.
10. Be represented by an accurate skill file.

Then the combined FROGE system must demonstrate that multiple MCPs can coexist, start together, authenticate correctly, and remain individually addressable by Hermes.

## Evidence states

- `RESEARCHED` — supported by repository/research evidence.
- `IMPLEMENTED` — code exists.
- `VERIFIED` — real test evidence proves the behavior.
- `BLOCKED` — required dependency or access is unavailable.
- `UNSUPPORTED` — the underlying tool does not expose a safe/verified integration path.

Never promote `RESEARCHED` directly to `VERIFIED`.
