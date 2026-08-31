# FROGE MCP — Agent Communication Contract

## Purpose

MCP is used here for **communication and coordination between FROGE-managed agents/tools**.

Primary goal:

```text
Hermes / Orchestrator
        |
        +--> delegate task --> specialist agent
        |
        +<-- result/evidence -- specialist agent
        |
        +--> delegate next task --> another agent
```

## Required capabilities

1. Register/identify approved agents.
2. Discover agent capabilities.
3. Submit a task with a unique task ID.
4. Pass structured task context and constraints.
5. Query task status.
6. Receive progress/events where supported.
7. Receive final result and evidence.
8. Cancel/stop a task when policy allows.
9. Preserve correlation IDs so multi-agent work can be traced.
10. Enforce permissions and prevent an agent from silently exceeding its role.

## Task envelope

Every delegated task should have:

- task ID
- parent task ID, if any
- sender
- recipient
- objective
- required inputs
- constraints
- allowed tools/skills
- expected output
- timeout/retry policy
- evidence requirements

## Result envelope

Every result should identify:

- task ID
- status: success / partial / failed / blocked
- summary
- files changed
- commands/tests executed
- evidence
- unresolved issues
- recommended next action

## Boundary

MCP is **not** the installation engine. Installation remains FROGE's adapter/installer responsibility. MCP only provides the communication boundary required for agents to cooperate.

No Omni Router MCP, Mega MCP or unrelated MCP servers are to be created under this contract.

## Verification

Before an MCP integration is considered complete, verify discovery, connectivity, task submission, result delivery, failure handling, permission boundaries and regression behavior.
