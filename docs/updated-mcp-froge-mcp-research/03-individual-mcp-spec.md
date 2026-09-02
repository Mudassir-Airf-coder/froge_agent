# 03 — Individual MCP Specification

## Purpose

Every supported tool receives its own MCP. The MCP is a thin, explicit integration boundary around that one tool.

## Required MCP contract

Each MCP should define the following logical operations where the underlying tool supports them:

- `discover` — locate and identify the underlying tool.
- `version` — report the installed/versioned tool.
- `health` — determine whether the tool is reachable/usable.
- `capabilities` — list verified operations.
- `start` — start the underlying runtime when applicable.
- `stop` — stop it when applicable.
- `execute` — submit a bounded task through the verified interface.
- `status` — report task/runtime state.
- `cancel` — cancel work when supported.
- `normalize_result` — convert native output into a stable Hermes-facing result.

An operation may be marked unsupported when the underlying tool does not provide it.

## Integration surfaces

The MCP must use the integration surface actually supported by the tool. Possible surfaces include:

- CLI
- HTTP/API
- RPC
- SDK
- extension/plugin interface
- native MCP
- another documented programmatic interface

The project must not invent a native API simply because one would be convenient.

## Generic lifecycle

```text
DISCOVER
   -> VALIDATE INSTALLATION
   -> AUTHENTICATE
   -> CHECK HEALTH
   -> VALIDATE REQUEST
   -> APPLY POLICY
   -> DISPATCH
   -> MONITOR
   -> CAPTURE
   -> NORMALIZE
   -> AUDIT
   -> RETURN
```

## Tool-specific isolation

Each MCP owns:

- tool discovery logic;
- tool-specific configuration;
- tool-specific authentication requirements;
- command/API/RPC mapping;
- native error mapping;
- capability declaration;
- execution limits;
- tool-specific documentation references.

This prevents one MCP from accumulating unrelated integration logic.

## Result contract

At minimum, a completed task should allow Hermes to distinguish:

- accepted/started;
- running;
- completed;
- cancelled;
- failed;
- timed out;
- unsupported;
- blocked by policy/authentication.

Native stdout/stderr/API payloads should be retained as appropriate, but secrets must be redacted.

## Verification rule

An MCP is `VERIFIED` only after a real test proves the complete path:

```text
Hermes -> MCP -> underlying tool -> real operation -> MCP -> Hermes
```

A unit test that mocks the underlying tool is not sufficient for the `VERIFIED` state.
