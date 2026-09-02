# 10 — Implementation Phases

## Phase 1 — Freeze and verify FROGE core

Preserve the working MCP core. Confirm tests, auth, sessions, config paths, CLI and package build. Do not redesign the protocol without evidence.

## Phase 2 — Adapter framework

Implement a stable adapter interface, registry, capability metadata, health/version checks, policy hooks, correlation tracking and normalized results.

## Phase 3 — Hermes connection

Implement the real Hermes MCP-client connection, runtime-token handling, handshake/verification state and FROGE skill delivery/configuration. Hermes MCP consumption is currently a research gap and must be verified against the actual Hermes implementation.

## Phase 4 — First worker integrations

Implement and verify the strongest direct-control candidates one at a time: OpenCode, Pi, Codex and Claude Code. Each adapter must use the tool's documented interface and preserve its security controls.

## Phase 5 — Router/runtime integrations

Integrate OmniRoute and, where required, NemoClaw/OpenClaw using their real APIs/CLI/MCP surfaces. Keep routing responsibilities separate from FROGE orchestration/control.

## Phase 6 — Additional ecosystem integrations

Investigate and implement DeepSeek Harness, Freebuff/Codebuff, Prime Agent, Atomic Agents and Strix only where requirements justify them. Respect their different categories: library, peer orchestrator, security layer, or high-risk runtime are not interchangeable with coding CLIs.

## Phase 7 — Distribution

Finalize the real GitHub one-line installer, package publishing/install behavior, PATH handling, user-scoped data, upgrade/reinstall behavior and clean-machine installation.

## Phase 8 — End-to-end certification

Run the full chain:

```text
fresh machine
  → install
  → start FROGE
  → obtain runtime credential
  → connect Hermes
  → discover capabilities
  → select adapter
  → execute real task
  → capture result
  → stop/restart
```

Only after required integrations and evidence gates pass should the target release be called complete.
