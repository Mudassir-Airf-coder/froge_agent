# Updated MCP / FROGE MCP Research

## Status
Research-driven architecture proposal. This document set supersedes the **implementation direction** of the earlier unified FROGE MCP plan, but the earlier documentation under `docs/froge-mcp-system/` is intentionally preserved as historical/reference material and must not be deleted.

## Core idea

The system will **not** try to build one giant MCP that directly contains every tool integration.

Instead:

```text
USER
  |
  v
HERMES (MASTER / ORCHESTRATOR)
  |
  | MCP connections
  +-------------------+-------------------+-------------------+---- ...
  |                   |                   |
  v                   v                   v
OpenCode MCP       Codex MCP        Claude Code MCP       ...
  |                   |                   |
  v                   v                   v
OpenCode           Codex           Claude Code          Other tools

All MCPs are then packaged/managed together by:

FROGE MCP SYSTEM
  |
  +-- installs / configures / starts / stops / health-checks MCPs
  +-- provides shared lifecycle and runtime authentication
  +-- exposes the MCP endpoints to Hermes
  +-- keeps each tool's integration isolated behind its own MCP
```

### The key separation

- **Hermes** remains the master/orchestrator and decision maker.
- **Each supported tool gets its own dedicated MCP**.
- **Each MCP is independently generated, implemented, tested, and verified with Hermes** before being included in the combined system.
- **Each MCP gets its own skill file** explaining capabilities, connection details, authentication expectations, commands/tools, limitations, and safe usage.
- **FROGE MCP is the distribution/lifecycle/control layer around the collection of MCPs**, not a replacement for the individual MCPs.
- The final user experience is one installation, one system startup command, one Hermes connection point/workflow, while internally the individual MCPs remain separate components.

## Research basis

This architecture is based on the existing research under `research/` covering Hermes, OpenCode, Omni Router, Codex, Claude Code, Prime Agent, Atomic Agents, OpenClaw, Freebuff/Codebuff, DeepSeek Harness, NemoClaw, Pi Agent, and Strix.

Research evidence must remain separate from implementation verification. A researched integration is not considered working until the corresponding MCP is actually connected to Hermes and its required control paths are tested.

## Required end state

A user should be able to:

1. Install the FROGE MCP system with a single GitHub-hosted installer command.
2. Run a simple FROGE command to initialize/start the system.
3. Have the required individual MCPs discovered/configured and started.
4. Have runtime authentication/token handling generated securely.
5. Have Hermes connect to the FROGE-managed MCP environment.
6. Have Hermes read the skill information for every available MCP.
7. Have Hermes discover which MCP exposes which tool capabilities.
8. Have Hermes dispatch work to the correct MCP.
9. Have the individual MCP invoke/control its underlying tool using that tool's native supported interface.
10. Receive normalized status, result, error, and lifecycle information back through the MCP path.

## Non-goals

This design does **not** mean:

- one MCP becomes an unrestricted shell executor;
- FROGE becomes the AI master;
- FROGE replaces Hermes planning/reasoning;
- every external tool is forced into one identical internal implementation;
- unsupported tool interfaces are guessed;
- research claims are treated as verification;
- all MCPs must expose identical capabilities when their underlying tools differ.

## Document map

- `01-revised-product-scope.md` — revised product goal, boundaries, and acceptance criteria.
- `02-system-architecture.md` — complete multi-MCP architecture and responsibilities.
- `03-individual-mcp-spec.md` — standard contract for each tool-specific MCP.
- `04-mcp-skill-file-spec.md` — required skill file for every MCP.
- `05-hermes-mcp-integration.md` — how Hermes discovers, connects to, and controls the MCP collection.
- `06-froge-system-lifecycle.md` — installation, startup, runtime token, orchestration of MCP processes, shutdown, restart, and health.
- `07-tool-by-tool-build-plan.md` — implementation order for the researched tools.
- `08-verification-matrix.md` — evidence required before each MCP is marked verified.
- `09-one-line-installer-spec.md` — final distribution and installer requirements.
- `10-implementation-phases.md` — phased implementation plan from individual MCPs to the combined FROGE system.
- `DECISIONS.md` — architectural decisions and constraints.

## Golden rule

**Build and verify the individual MCPs first. Combine them only after their independent Hermes connection/control paths are proven.**
