# FROGE — Complete Updated System Specification

## 1. Mission

FROGE is a local-first AI-agent control plane that prepares a machine, manages approved tools, verifies them with evidence, coordinates agents, preserves context, and continuously drives work toward a defined end state.

The system is not a generic package manager and not a generic MCP host. Its job is controlled orchestration of the user's approved AI development environment.

## 2. Major subsystems

```text
User Request
    |
    v
FROGE Orchestrator
    |
    +--> Task Planner / Dependency Graph
    |
    +--> Tool & Environment Manager
    |       +--> Discover
    |       +--> Install
    |       +--> Configure
    |       +--> Start/Stop where applicable
    |       +--> Update
    |       +--> Repair
    |       +--> Verify
    |
    +--> Agent Coordination Layer
    |       +--> Hermes / coordinator
    |       +--> coding agents (e.g. CodeBuff/FreeBuff)
    |       +--> specialist agents
    |       +--> MCP communication boundary
    |
    +--> Skill System
    |       +--> find existing skill
    |       +--> generate missing skill
    |       +--> validate skill
    |       +--> execute skill
    |       +--> version/evolve skill
    |
    +--> Update Manager
    |       +--> detect new versions
    |       +--> inspect release/change information
    |       +--> plan update
    |       +--> update
    |       +--> verify/regression check
    |
    +--> State / Evidence / Memory
            +--> persistent state
            +--> audit trail
            +--> evidence
            +--> task/tracker state
            +--> durable context
```

## 3. Tool lifecycle

Every managed tool follows the same desired-state lifecycle:

`DISCOVER -> CLASSIFY -> PLAN -> INSTALL/KEEP/UPDATE/REPAIR -> VERIFY -> RECORD -> REPORT`

A tool is never declared healthy merely because an executable exists. Verification must progress through the documented health ladder and, where possible, include a functional test.

## 4. Tool inventory model

The implementation must support at least these researched/approved categories, while treating the repository research as the source of truth for exact commands and capabilities:

- Coding/execution: CodeBuff/FreeBuff, OpenCode, Claude Code, Codex.
- Agent runtimes/coordinators: Hermes, OpenClaw, NemoClaw, Prime Agent, Atomic Agent.
- Routing/control: Omni Router, Nimble Clock.
- Knowledge/context: OHSC, Graphify.
- Base system prerequisites: Python, Git, Node.js, npm and other prerequisites explicitly required by verified research.

Ollama and vLLM are excluded from installation/integration scope.

## 5. Automatic update system

After a tool is installed and verified, FROGE must be able to monitor its declared update source/version signal. When a newer version is detected:

1. record the current version;
2. identify the candidate new version;
3. consult verified research/adapter rules;
4. create an update plan;
5. perform the update only through the approved adapter;
6. verify version and functional health;
7. run relevant regression checks;
8. persist before/after evidence;
9. roll back or enter recovery if verification fails;
10. update documentation/tracker when the change affects behavior.

Updates must be idempotent and must not silently replace a working tool with an unverified package.

## 6. Agent roles

### Coordinator / Hermes
Owns high-level task delegation and receives results. It does not need to implement every specialist capability itself.

### Coding agent
Builds and changes repository code according to the task contract, using the installed execution tools and skills.

### Tool Expert
A dedicated specialist whose only responsibility is researching, installing, configuring, verifying and maintaining tools, skills, plugins or integrations supplied by a user. It must use the repository's research before acting and must report evidence.

### Skill Designer / Skill Expert
A dedicated specialist responsible for skill discovery and design. For a user request it first searches for an existing relevant skill. If none is suitable, it designs a new reusable skill, validates it, and stores it in the skill repository. It does not automatically convert every error into a skill; skill creation is driven by reusable capability value.

### Research / Verification specialists
May be spawned in parallel when a task needs independent validation, compatibility checking or troubleshooting.

## 7. Skill decision policy

For every task:

`User task -> identify required capability -> search installed/local skills -> search approved skill sources -> if suitable skill exists, use it -> otherwise design skill -> validate -> execute -> record result.`

A skill is reusable operational knowledge, not a plugin and not an MCP server. Skills must contain prerequisites, inputs, procedure, verification, failure handling, safety constraints and expected outputs.

## 8. MCP boundary

FROGE MCPs exist specifically so agents/tools can communicate and delegate work to each other. The MCP layer must expose controlled communication primitives such as task submission, task status, result delivery, capability discovery and permission-aware invocation where required by the architecture.

Do not use MCP as a substitute for the installation engine, skill catalog, generic web service integration or arbitrary application APIs.

## 9. Context continuity

`.context.md` is the durable handoff record. Agents must update it at meaningful checkpoints, especially before context-window exhaustion. It contains current objective, completed work, active task, decisions, constraints, evidence, failures, next action and important file locations. It must never contain secrets.

## 10. Completion model

The system is complete only when the implementation, tests, runtime verification, documentation, state and tracker agree. 'Code exists' is not completion. Every major subsystem needs acceptance criteria and evidence.
