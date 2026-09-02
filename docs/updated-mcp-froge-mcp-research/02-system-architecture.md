# 02 — Multi-MCP System Architecture

## High-level model

```text
                         USER
                           |
                           v
                    HERMES MASTER
                 (reasoning/orchestration)
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        TOOL MCP A     TOOL MCP B    TOOL MCP C   ...
             |             |             |
             v             v             v
        Tool A CLI/API   Tool B RPC   Tool C SDK   ...

                    FROGE MCP SYSTEM
          ---------------------------------------
          install | configure | auth | lifecycle
          process supervision | discovery | health
          endpoint/session management | logs/audit
```

The diagram is conceptual. Exact transport and wire details must follow the actual implementations and verification results.

## Why separate MCPs

A single giant MCP would couple every tool integration into one codebase and make failures, permissions, updates, and testing harder to isolate. A separate MCP per tool gives each integration a clear boundary and lets it be verified independently.

## Responsibilities

### Hermes

- Owns user-facing intent.
- Plans work.
- Chooses the MCP/tool.
- Decides whether work should be retried, switched, or escalated.
- Reads MCP skill information.
- Consumes MCP status/results/errors.

Hermes does not delegate its master role to FROGE.

### Individual MCP

- Owns the integration contract for one underlying tool.
- Knows how to discover the tool.
- Knows how to validate availability/version.
- Knows how to authenticate when required.
- Exposes only verified capabilities.
- Converts MCP requests into the tool's supported interface.
- Normalizes responses for Hermes.
- Enforces tool-specific safety and execution policy.

### FROGE MCP System

- Installs the MCP collection.
- Maintains system-level configuration.
- Starts/stops/restarts individual MCP processes.
- Generates and manages runtime authentication material.
- Checks health and readiness.
- Provides a stable system-level entry point for Hermes integration.
- Records lifecycle/audit information without leaking secrets.

FROGE does not decide which coding/reasoning tool should solve the user's task. Hermes does that.

## Process model

Each MCP should be independently startable. The combined FROGE command may start all configured MCPs, but process isolation must remain visible internally.

Conceptually:

```text
froge-mcp start
    |
    +-- start opencode-mcp
    +-- start codex-mcp
    +-- start claude-code-mcp
    +-- start pi-mcp
    +-- start ...
    |
    +-- generate/refresh runtime session credentials
    +-- health-check each MCP
    +-- publish readiness state
```

A failed MCP must be reported as failed; the system must not claim that every capability is ready.

## Capability ownership

Capabilities belong to the individual MCP that implements them. FROGE may aggregate discovery/status metadata, but it must not invent capabilities or silently emulate unsupported operations.

## Security boundary

No universal unrestricted `run_any_command` contract is required by this architecture. Every MCP must constrain how it invokes its underlying tool using the tool's real interface and the applicable permissions.

## Omni Router boundary

Omni Router remains a model/API routing layer. If an Omni Router MCP is built, it is a separate tool-specific MCP and does not turn FROGE into a model router.
