# Architectural Decisions — Updated MCP / FROGE MCP

## D1 — One MCP per tool

Each selected external/internal tool receives its own MCP boundary. There is no requirement to merge all tool integrations into one giant MCP.

## D2 — Hermes remains master

Hermes is the master/orchestrator. Individual MCPs are workers/interfaces that Hermes can use.

## D3 — FROGE is the system/lifecycle layer

FROGE packages and manages the MCP collection: installation, configuration, startup, authentication/session handling, health, process lifecycle, and system-level readiness.

## D4 — Skills are per MCP

Every MCP gets its own skill file so Hermes can understand that MCP's capabilities and operating rules.

## D5 — Independent verification first

Every MCP must be tested with Hermes independently before being accepted into the combined FROGE system.

## D6 — Research is not verification

Repository research establishes what may be possible. Only real execution evidence establishes that an integration works.

## D7 — Preserve tool-native boundaries

Each MCP must use the underlying tool's actual supported interface and security controls. FROGE must not flatten all tools into unrestricted command execution.

## D8 — Shared system authentication, explicit MCP boundaries

The final system may provide a common runtime authentication/session mechanism, while individual MCP credentials and permissions remain isolated where required by the underlying tool.

## D9 — Existing documentation is preserved

The earlier documentation at `docs/froge-mcp-system/` remains intact as historical/reference material. This new directory documents the revised architecture and does not delete the old work.

## D10 — Build incrementally

The order is:

```text
ONE MCP
 -> TEST WITH HERMES
 -> VERIFY
 -> SKILL + EVIDENCE
 -> NEXT MCP
 -> ...
 -> COMBINE IN FROGE
 -> ONE-LINE INSTALL
 -> FINAL HERMES SYSTEM TEST
```

This reduces coupling and makes failures attributable to a specific integration.
