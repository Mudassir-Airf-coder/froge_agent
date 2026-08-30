# FROGE MCP Control Plane

## Purpose

The MCP control plane is the integration boundary between FROGE and external/local capabilities. It should make tools discoverable, callable, observable, and governable without coupling the orchestrator to individual implementations.

## Responsibilities

- Register approved MCP servers and tools.
- Discover tool metadata and capabilities.
- Validate tool inputs and outputs.
- Track health and availability.
- Enforce permissions and policy boundaries.
- Provide consistent lifecycle operations.
- Record execution evidence needed for verification.
- Support local installed tools and runtimes through explicit adapters.

## Planned Components

```text
MCP Control Plane
├── Server Registry
├── Tool Registry
├── Transport Manager
├── Capability Discovery
├── Permission / Policy Layer
├── Health Monitor
├── Invocation Layer
├── Evidence Collector
└── Lifecycle Manager
```

## Safety and Reliability

A tool being registered does not mean it is automatically trusted. FROGE should distinguish between discovered, configured, healthy, authorized, and verified capabilities.

## Planned Verification

Every MCP integration should have:

1. discovery test,
2. configuration test,
3. connectivity/health test,
4. real invocation test,
5. failure-path test,
6. permission-boundary test,
7. regression test.
