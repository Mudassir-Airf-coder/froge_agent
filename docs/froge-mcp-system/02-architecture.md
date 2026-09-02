# 02 — Architecture

## 1. System model

```text
                    ┌─────────────────────┐
                    │       HERMES        │
                    │ master/orchestrator │
                    └──────────┬──────────┘
                               │ MCP
                    endpoint + runtime auth
                               │
                    ┌──────────▼──────────┐
                    │      FROGE MCP      │
                    │ communication/control│
                    │       bridge        │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
        Adapter A          Adapter B          Adapter N
             │                 │                 │
        Tool process       Tool API/RPC       Tool runtime
```

## 2. FROGE responsibilities

### Communication
- Accept authenticated MCP requests from Hermes.
- Validate request schema.
- Assign/propagate correlation IDs.
- Route to the selected adapter.
- Normalize tool status/results/errors.

### Control
- Start/stop/inspect supported tool processes when the adapter explicitly supports lifecycle control.
- Apply execution policy before dispatch.
- Enforce timeouts and cancellation where technically possible.
- Record auditable events.

### Discovery
- Report installed/available integrations.
- Report adapter health/version and supported capabilities.
- Never claim an unverified capability as available.

## 3. Hermes responsibilities

- Interpret user intent.
- Plan and choose the appropriate worker/tool.
- Decide when to retry, switch tools, or ask for approval.
- Supply task parameters.
- Interpret results and continue the workflow.

FROGE must not silently become the planner or master.

## 4. Adapter responsibilities

Each adapter translates the FROGE-neutral contract into one concrete tool interface:

- CLI process.
- HTTP API.
- MCP client.
- RPC/stdio protocol.
- SDK/in-process API where appropriate.

An adapter owns tool-specific discovery, command construction, output parsing, lifecycle details and tool-specific error mapping.

## 5. Security boundary

No generic `run_any_command` escape hatch is required by the architecture. Tool execution should be capability-scoped and policy-checked. High-risk tools must have explicit approval/sandbox requirements.

## 6. OmniRoute boundary

OmniRoute is a separate model/API routing layer. FROGE may integrate with it through a dedicated adapter/control surface if explicitly required and verified, but FROGE must not absorb OmniRoute's routing responsibility.

## 7. Design principle

The stable FROGE contract must not depend on one tool's internal implementation. Tool-specific behavior stays behind adapters so the MCP core remains small, testable and replaceable.
