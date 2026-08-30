# FROGE Orchestrator

## Role

The orchestrator is the central decision and execution layer of FROGE. It should coordinate tasks without coupling the core system to one model, provider, CLI, or MCP implementation.

## Responsibilities

1. Accept a task and establish a task/session context.
2. Inspect available capabilities and constraints.
3. Build or select an execution plan.
4. Route model and tool calls through registered adapters.
5. Execute steps with explicit permissions and timeouts.
6. Validate results and collect evidence.
7. Classify failures and invoke approved recovery policies.
8. Preserve useful operational state for future decisions.
9. Return a structured result containing status, evidence, and relevant errors.

## Logical Pipeline

```text
Task Intake
   ↓
Context / Session
   ↓
Planning
   ↓
Capability Discovery
   ↓
Routing
   ↓
Execution
   ↓
Validation
   ├── PASS → Result + Evidence
   └── FAIL → Error Classification → Recovery → Re-validate
```

## Provider Independence

The orchestrator must not contain hard-coded provider-specific behavior. Providers and models belong in the provider registry/adapters. The orchestrator consumes normalized capabilities and health information.

## MCP Independence

MCP tools are discovered and invoked through the MCP control layer. The orchestrator should not assume that a particular MCP server exists unless it is declared and healthy.

## Recovery

Recovery is policy-driven. A provider/model may be retried, cooled down, replaced, or escalated based on a classified failure. A fallback is trusted only after a successful health/response verification.

## Future Implementation Contract

The concrete implementation should define typed contracts for:

- `Task`
- `Plan`
- `ExecutionStep`
- `Provider`
- `Model`
- `Tool`
- `Skill`
- `HealthStatus`
- `ErrorEvent`
- `RecoveryAction`
- `ExecutionResult`
- `Evidence`

These contracts should become stable interfaces before large-scale implementation begins.
