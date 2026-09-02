# 10 — Implementation Phases

## Phase 0 — Freeze the revised design

- Keep the previous `docs/froge-mcp-system/` documentation intact.
- Treat this folder as the new direction for the multi-MCP architecture.
- Confirm the exact selected MCP list from the research.

## Phase 1 — Build the first individual MCP

Choose one tool with a clear, testable integration surface.

Deliver:

- MCP package/project;
- tool discovery;
- capability tools;
- authentication;
- lifecycle;
- skill file;
- tests;
- Hermes connection test;
- real execution evidence.

## Phase 2 — Repeat independently

Build the next MCP without coupling its internal implementation to the previous MCP. Repeat the same verification gate.

## Phase 3 — MCP collection

Create the common FROGE runtime configuration that knows which independently verified MCPs are installed/enabled.

## Phase 4 — FROGE lifecycle

Implement:

- one-line installation;
- `froge-mcp` CLI;
- collection startup;
- per-MCP process supervision;
- runtime token/session management;
- health/status;
- stop/restart;
- failure reporting.

## Phase 5 — Hermes collection integration

Verify that Hermes can:

- connect to the FROGE-managed environment;
- discover the individual MCPs;
- read their skills;
- choose the correct MCP;
- execute real tasks;
- receive results/errors.

## Phase 6 — Combined certification

Test multiple MCPs simultaneously and confirm isolation, correct routing, authentication, lifecycle behavior, and failure reporting.

## Phase 7 — Distribution certification

Test:

- one-line installation;
- fresh Windows environment;
- arbitrary working directory;
- reinstall/idempotency;
- restart;
- upgrade/update;
- recovery from a failed MCP.

## Final gate

The system is complete only when the required individual MCPs and the combined FROGE runtime have real evidence for their promised behavior.
