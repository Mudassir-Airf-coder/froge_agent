# 03 — Tool Integration Specification

## 1. Universal adapter contract

Every supported tool integration must expose, conceptually, these operations:

- `discover()` — detect installation and executable/API surface.
- `version()` — return the detected version.
- `health()` — prove the interface is reachable/usable.
- `capabilities()` — return only capabilities supported and verified by the adapter.
- `start()` — start the tool/runtime if applicable.
- `stop()` — stop it if lifecycle control is supported.
- `execute(task)` — submit a bounded task through the tool's supported interface.
- `status(correlation_id)` — retrieve progress/result where supported.
- `cancel(correlation_id)` — cancel where supported.
- `normalize_result()` — convert tool-specific output into the FROGE result contract.

Not every tool will support every operation. Unsupported operations must return an explicit `UNSUPPORTED` result rather than pretending to work.

## 2. Capability classes

### READ_ONLY
Examples: version, health, session listing, configuration inspection, capability discovery.

### CONTROLLED_WRITE
Examples: creating a session, changing a bounded configuration value, dispatching a task with explicit policy.

### HIGH_RISK
Examples: unrestricted shell execution, dangerous/full-access sandbox modes, arbitrary plugin installation, or execution against an untrusted workspace.

High-risk capability requires explicit policy/approval and, where appropriate, an external sandbox or disposable workspace.

## 3. Execution lifecycle

```text
REQUEST
  ↓
AUTHENTICATE
  ↓
VALIDATE
  ↓
CHECK POLICY
  ↓
RESOLVE ADAPTER
  ↓
DISCOVER/HEALTH CHECK
  ↓
DISPATCH
  ↓
MONITOR
  ↓
CAPTURE RESULT
  ↓
NORMALIZE
  ↓
AUDIT
  ↓
RETURN TO HERMES
```

## 4. Required adapter evidence

Before an adapter is marked `VERIFIED`, record:

- tool name and exact version;
- installation method;
- executable/API location;
- authentication method, without recording secrets;
- supported capability list;
- exact test task;
- expected result;
- observed result;
- stdout/stderr or API response summary;
- exit/error behavior;
- timeout/cancellation behavior if supported;
- security classification;
- known limitations.

## 5. Special tool categories from research

- OpenCode: strong CLI/headless/server/ACP surfaces; unrestricted non-interactive permissions are a high-risk area.
- Codex: CLI and MCP lifecycle surfaces; sandbox/approval policy must be preserved.
- Claude Code: CLI, hooks, MCP and subagent surfaces; shell/plugin permissions require strict policy.
- Pi: RPC/SDK/extension surfaces are promising for external control; native MCP is not part of the core design.
- DeepSeek Harness: plugin architecture and delegation to Codex/Claude Code are documented, but its own MCP surface needs direct verification.
- NemoClaw: OpenShell sandbox and OpenAI-compatible inference endpoint are strongly documented; Windows story requires verification.
- OpenClaw: gateway-first architecture; MCP control and integration surface require direct verification before implementation.
- Atomic Agents: Python framework/library, not a standalone worker CLI; integration should be an SDK/library integration rather than process spawning.
- Freebuff/Codebuff: CLI exists, but MCP and custom gateway behavior require direct verification.
- Prime Agent: high-risk execution model with no built-in security sandbox; any integration requires an external isolation strategy.
- Strix: research is insufficient for an executable adapter; keep `UNKNOWN` until direct investigation.

## 6. Adapter rule

Research tells us what to investigate. Verification determines what FROGE is allowed to advertise and execute.
