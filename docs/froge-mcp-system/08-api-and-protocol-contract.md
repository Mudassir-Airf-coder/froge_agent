# 08 — API and Protocol Contract

## 1. Transport

FROGE exposes its MCP server through the transport implemented by the existing core. The documentation must describe the actual transport and endpoint discovered from the implementation; this specification must not invent a new transport.

## 2. Session identity

Every runtime has a session identity and authentication credential. Requests should carry or receive a correlation ID so one task can be traced across adapter, process and result events.

## 3. Capability discovery

The client must be able to obtain a structured description containing, at minimum:

- adapter/tool identifier;
- installed/version state;
- health state;
- available operations;
- risk classification;
- required permissions;
- current availability.

## 4. Task request

Conceptual request:

```json
{
  "adapter": "<tool>",
  "capability": "<operation>",
  "task": {"...": "tool-specific validated parameters"},
  "timeout_ms": 120000,
  "correlation_id": "<id>"
}
```

The exact wire schema must follow the implemented MCP/tool schema. This example is a conceptual contract, not a literal promise about the current JSON shape.

## 5. Result

Conceptual normalized result:

```json
{
  "correlation_id": "<id>",
  "status": "success|failed|denied|timeout|cancelled|unsupported",
  "adapter": "<tool>",
  "result": {},
  "error": null,
  "duration_ms": 0
}
```

## 6. Error semantics

Errors must be explicit, stable enough for Hermes to reason about, and never replaced with a fake success message.

## 7. Backward compatibility

Changes to the core MCP contract require a documented decision and regression tests. Tool-specific adapter changes should not require breaking the stable FROGE protocol.
