# MCP Documentations

This directory is the master documentation specification for designing, researching, implementing, testing, verifying, and integrating **separate MCPs for the individual tools researched by FROGE Agent**.

The purpose of this documentation is to establish one consistent, evidence-first standard so every tool receives its own MCP design and lifecycle instead of being forced into one giant MCP.

---

## 1. Core Architecture

The target architecture is:

```text
USER
  |
  v
HERMES
(master / orchestrator)
  |
  +-------------------+-------------------+-------------------+
  |                   |                   |
  v                   v                   v
Tool MCP A         Tool MCP B         Tool MCP C
  |                   |                   |
  v                   v                   v
Actual Tool A      Actual Tool B      Actual Tool C
  |                   |                   |
  +-------------------+-------------------+
                      |
                      v
                 real result
                      |
                      v
                    HERMES
```

### Responsibilities

- **Hermes** is the master orchestrator and decision-maker.
- **Each MCP** is a dedicated integration/control surface for exactly one target tool or one tightly defined target runtime.
- **The underlying tool** remains the source of truth for its own capabilities and execution semantics.
- **FROGE** is the ecosystem/system layer that can later install, manage, start, stop, health-check, update, and organize the independently verified MCPs.

FROGE is **not** a second master agent, planner, model router, marketplace, or replacement for Hermes.

---

## 2. Non-Negotiable Design Rules

1. One target tool = one dedicated MCP unless research proves that a different boundary is technically necessary.
2. Do not create one universal MCP containing every tool integration.
3. Do not invent APIs, RPC methods, commands, capabilities, or tool behavior.
4. Use the target tool's real supported integration surface: native MCP, CLI, API, RPC, SDK, extension, local service, or another documented mechanism.
5. Research, implementation, and verification are separate states.
6. `RESEARCHED` never means `VERIFIED`.
7. `INFERRED` and `UNKNOWN` claims must remain explicitly marked until evidence resolves them.
8. No fake test results, fake screenshots, fake commands, fake compatibility, or assumed installation success.
9. Never expose or commit secrets, runtime tokens, credentials, API keys, or private authentication material.
10. Hermes must be able to understand what each MCP does, when to use it, what inputs it accepts, what it returns, and what limitations it has.
11. Every MCP must have its own documentation package, skill, task tracking, verification record, and evidence trail.
12. Do not modify or silently reinterpret unrelated existing research.
13. Implementation should begin only after the MCP's design and verification requirements are sufficiently documented.

---

## 3. MCP Documentation Package Standard

Every individual MCP must have its own directory:

```text
docs/MCP-Documentations/
  <tool-name>-mcp/
```

Each package should contain, at minimum:

```text
README.md
research.md
architecture.md
integration.md
mcp-spec.md
tools.md
capabilities.md
api-contract.md
authentication.md
security.md
configuration.md
installation.md
runtime.md
lifecycle.md
error-handling.md
testing.md
verification.md
hermes-integration.md
skill.md
task.md
tracker.md
decisions.md
limitations.md
evidence.md
implementation-plan.md
```

If a document is genuinely not applicable, keep the file and explicitly write `NOT APPLICABLE` with the reason and supporting evidence. Do not silently omit important sections.

---

## 4. README.md — MCP Identity and Executive Summary

The README for every MCP must define:

- MCP name and canonical tool name.
- Target tool/runtime.
- Purpose.
- Scope.
- Non-goals.
- Current status.
- Supported platforms.
- Supported versions, when verified.
- Integration surface.
- High-level architecture.
- Hermes relationship.
- FROGE relationship.
- Major capabilities.
- Known limitations.
- Security classification.
- Verification state.
- Links to the rest of the package.

Recommended status values:

```text
RESEARCHED
DESIGNED
IMPLEMENTATION_PENDING
IMPLEMENTED
LOCALLY_TESTED
HERMES_CONNECTED
VERIFIED
BLOCKED
UNSUPPORTED
```

A status must be backed by evidence.

---

## 5. research.md — Evidence-Based Tool Research

Research must establish what the target tool actually is and how it can technically be controlled.

Document:

- Official project/repository.
- Official documentation.
- Source repository when available.
- Version/release information.
- Installation methods.
- Operating-system support.
- Runtime requirements.
- CLI commands.
- API endpoints.
- RPC mechanisms.
- SDKs.
- Extensions/plugins.
- Native MCP support, if any.
- Authentication requirements.
- Configuration files/environment variables.
- Input/output formats.
- Streaming behavior.
- Session behavior.
- Process behavior.
- Filesystem behavior.
- Network behavior.
- Error behavior.
- Automation limitations.
- Known security considerations.
- Known integration limitations.

Every important claim should be classified as:

- `VERIFIED` — directly confirmed by reliable evidence/test.
- `RESEARCHED` — supported by source/documentation but not yet locally tested.
- `INFERRED` — logical inference, not direct evidence.
- `UNKNOWN` — not established.
- `BLOCKED` — required evidence/test cannot currently be obtained.

---

## 6. architecture.md — Dedicated MCP Architecture

Define the complete internal boundary of the MCP.

Include:

```text
Hermes
  |
  | MCP protocol / transport
  v
MCP Server
  |
  +--> validation
  +--> authorization
  +--> session/runtime manager
  +--> tool adapter
  +--> underlying tool
  +--> result normalization
  +--> error mapping
  +--> audit/observability
```

Document:

- Components.
- Responsibilities.
- Process boundaries.
- Data flow.
- Control flow.
- State management.
- Session model.
- Startup/shutdown behavior.
- Dependencies.
- Failure boundaries.
- Security boundaries.
- Windows-specific considerations.
- Future FROGE lifecycle integration.

The MCP must not duplicate Hermes orchestration logic.

---

## 7. integration.md — Real Tool Integration Contract

Document exactly how the MCP reaches the underlying tool.

Specify:

- Integration method.
- Required executable/package/service.
- Required version.
- Command/API/RPC surface.
- Process spawning rules, if applicable.
- Working directory rules.
- Environment variables.
- Input translation.
- Output translation.
- Timeout behavior.
- Cancellation behavior.
- Retry policy.
- Streaming handling.
- Exit-code handling.
- Tool-specific errors.
- Cleanup rules.

The integration must use the actual interface supported by the tool. Generic unrestricted shell execution must not be used as a substitute for a real integration contract.

---

## 8. mcp-spec.md — MCP Surface

Define the MCP interface exposed to Hermes.

For every MCP tool/resource/prompt, document:

- Name.
- Description.
- Purpose.
- Input schema.
- Required fields.
- Optional fields.
- Defaults.
- Validation rules.
- Output schema.
- Error schema.
- Side effects.
- Permissions.
- Idempotency.
- Timeout expectations.
- Cancellation semantics.
- Examples.

Only expose capabilities that are supported by the underlying tool and the MCP implementation.

---

## 9. tools.md — Tool Inventory

Create a complete inventory of MCP-exposed operations.

Recommended table:

| MCP Tool | Underlying Capability | Input | Output | Side Effect | Auth | Status |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

Every operation must map to a real underlying capability.

---

## 10. capabilities.md — Capability Matrix

Separate capabilities into:

- Available in underlying tool.
- Exposable through MCP.
- Implemented.
- Tested.
- Verified.
- Unsupported.
- Blocked.

Never mark a capability `VERIFIED` merely because the underlying tool appears to support it in documentation.

---

## 11. api-contract.md — Programmatic Contract

Document the exact programmatic contract between Hermes and the MCP.

Include:

- Transport.
- Endpoint/process model.
- Initialization.
- Handshake.
- Authentication.
- Tool discovery.
- Invocation.
- Result envelope.
- Error envelope.
- Notifications/events.
- Streaming.
- Cancellation.
- Session termination.
- Version compatibility.

Where MCP protocol standards already define behavior, reference the standard rather than inventing a parallel protocol.

---

## 12. authentication.md — Authentication Model

Document:

- Hermes-to-MCP authentication.
- MCP-to-tool authentication.
- Local credentials.
- Environment variables.
- Runtime/session credentials.
- Credential storage.
- Credential rotation.
- Credential lifetime.
- Unauthorized behavior.
- Secret redaction.

Runtime tokens must be treated as runtime/session credentials, not permanent public API keys.

---

## 13. security.md — Security Model

Cover:

- Least privilege.
- Process isolation.
- Filesystem restrictions.
- Network restrictions.
- Command restrictions.
- Input validation.
- Output validation.
- Secret handling.
- Logging redaction.
- Token handling.
- Path traversal protection.
- Resource exhaustion.
- Timeouts.
- Child-process cleanup.
- Auditability.
- Failure containment.
- Windows-specific security concerns.

Clearly distinguish implemented protections from planned protections.

---

## 14. configuration.md — Configuration

Document all configuration sources:

- CLI arguments.
- Environment variables.
- Configuration files.
- Default values.
- Required values.
- Optional values.
- Validation.
- Precedence.
- Per-user configuration.
- Machine-wide configuration, if supported.
- Secrets versus non-secret configuration.

Provide safe examples without real credentials.

---

## 15. installation.md — Installation

Document the real installation lifecycle:

```text
Prerequisites
  -> install target tool
  -> install MCP
  -> configure
  -> verify executable/runtime
  -> start
  -> health/readiness
  -> connect Hermes
```

Include:

- Windows-first installation.
- Dependencies.
- Exact commands.
- Version checks.
- PATH requirements.
- Fresh-machine expectations.
- Reinstallation.
- Idempotency.
- Upgrade/downgrade.
- Uninstallation.
- Troubleshooting.

Do not call a local editable developer install proof of end-user installation.

---

## 16. runtime.md — Runtime Model

Define:

- Process model.
- Ports/endpoints where applicable.
- Local versus remote operation.
- Startup dependencies.
- Readiness.
- Health checks.
- Sessions.
- Runtime tokens.
- Logs.
- PID/process management.
- Child processes.
- Shutdown.
- Crash recovery.
- Resource cleanup.

---

## 17. lifecycle.md — MCP Lifecycle

Define:

```text
DISCOVER
  -> INSTALL
  -> CONFIGURE
  -> START
  -> HEALTHY
  -> CONNECT
  -> READY
  -> EXECUTE
  -> MONITOR
  -> STOP
  -> UPDATE
  -> VERIFY
```

Document who performs each lifecycle action: Hermes, FROGE, the MCP itself, or the user.

---

## 18. error-handling.md — Failure Semantics

Define normalized error categories:

- Invalid input.
- Authentication failure.
- Authorization failure.
- Tool unavailable.
- MCP unavailable.
- Dependency missing.
- Timeout.
- Cancellation.
- Process crash.
- Tool-native error.
- Protocol error.
- Configuration error.
- Resource exhaustion.
- Unknown error.

Every error should preserve useful diagnostic information without leaking secrets.

---

## 19. testing.md — Test Strategy

Testing must progress through layers:

1. Static validation.
2. Unit tests.
3. MCP protocol tests.
4. Adapter tests.
5. Real underlying-tool tests.
6. End-to-end Hermes → MCP → tool tests.
7. Failure-path tests.
8. Security tests.
9. Clean-environment installation tests.
10. Regression tests.

A mocked tool does not prove a real integration.

---

## 20. verification.md — Verification Gates

Use explicit gates.

### Gate A — Research

The tool and integration surface are understood from evidence.

### Gate B — Installation

The target tool and MCP can actually be installed in the supported environment.

### Gate C — Startup

The MCP starts and reaches readiness.

### Gate D — Capability

At least the required real capabilities execute successfully.

### Gate E — Result

Real results return to the MCP and Hermes correctly.

### Gate F — Failure

Expected failures are handled and normalized.

### Gate G — Security

Authentication, authorization, secret handling, and restrictions behave as designed.

### Gate H — Distribution

The intended installation/update path works in a clean environment when distribution is in scope.

Only after the applicable gates pass should an MCP be called `VERIFIED`.

---

## 21. hermes-integration.md — Hermes Contract

Hermes remains the master.

Document:

- MCP discovery.
- MCP connection.
- Authentication.
- Capability discovery.
- Skill loading.
- Tool selection.
- Input construction.
- Dispatch.
- Result handling.
- Error handling.
- Session management.
- Context passing.
- Multi-MCP coordination.

The intended path is:

```text
User request
   -> Hermes understands intent
   -> Hermes reads/selects MCP skill
   -> Hermes selects dedicated MCP
   -> Hermes invokes MCP tool
   -> MCP validates request
   -> MCP controls actual underlying tool
   -> MCP normalizes result
   -> Hermes receives result
   -> Hermes decides next action
```

---

## 22. skill.md — MCP Skill Specification

Every MCP must have a corresponding skill file, normally at:

```text
skills/<tool-name>-mcp/SKILL.md
```

The skill must tell Hermes/agent systems:

- What this MCP controls.
- When to use it.
- When not to use it.
- Available MCP tools.
- Input requirements.
- Output expectations.
- Authentication requirements.
- Runtime requirements.
- Safety restrictions.
- Failure behavior.
- Verification status.
- Known limitations.
- Examples of correct task routing.

The skill is an operational instruction layer, not a replacement for the technical documentation.

---

## 23. task.md — Implementation Task Plan

Maintain a concrete checklist:

```text
[ ] Research complete
[ ] Integration surface selected
[ ] Architecture complete
[ ] MCP tools defined
[ ] Schemas defined
[ ] Security model defined
[ ] Authentication defined
[ ] Configuration defined
[ ] Installation defined
[ ] Runtime defined
[ ] Implementation started
[ ] Unit tests passing
[ ] Real tool test passing
[ ] Hermes connection passing
[ ] Failure tests passing
[ ] Security tests passing
[ ] Verification evidence captured
[ ] Skill finalized
[ ] Release gate passed
```

---

## 24. tracker.md — Progress Tracker

Track each milestone with:

- Date.
- Status.
- Owner/actor.
- Evidence.
- Blocking issue.
- Next action.

Never mark a task complete without evidence when the task requires verification.

---

## 25. decisions.md — Architecture Decisions

Record important decisions such as:

- Why this MCP boundary exists.
- Why a particular integration method was selected.
- Why an alternative was rejected.
- Why a capability is unsupported.
- Security decisions.
- Runtime decisions.
- Hermes interaction decisions.
- Windows-specific decisions.

Decisions should be durable and reviewable.

---

## 26. limitations.md — Known Limitations

Explicitly document:

- Unsupported platforms.
- Unsupported versions.
- Missing APIs.
- Missing native MCP support.
- Unverified capabilities.
- Performance constraints.
- Authentication limitations.
- Runtime limitations.
- Distribution limitations.
- Security limitations.

Do not hide uncertainty.

---

## 27. evidence.md — Evidence Ledger

Every major verification claim should point to evidence such as:

- Command output.
- Test result.
- Version output.
- MCP initialization result.
- Real tool invocation.
- Real result.
- Error-path result.
- Health check.
- Clean-install result.
- Source/documentation reference.

Recommended structure:

| ID | Claim | Evidence | Environment | Date | Status |
|---|---|---|---|---|---|
| E-001 | ... | ... | ... | ... | VERIFIED |

Evidence must be reproducible where practical.

---

## 28. implementation-plan.md — Build Sequence

Implementation should follow this sequence:

### Phase 1 — Research

Understand the tool and identify the real integration surface.

### Phase 2 — Boundary

Define what the MCP owns and what remains the tool's responsibility.

### Phase 3 — Contract

Define MCP tools, schemas, authentication, errors, runtime, and security.

### Phase 4 — Adapter

Implement the smallest real adapter required to control the underlying tool.

### Phase 5 — MCP Server

Expose the verified capability through MCP.

### Phase 6 — Local Tests

Run unit, protocol, adapter, and real-tool tests.

### Phase 7 — Hermes Integration

Connect Hermes and verify the full request/result path.

### Phase 8 — Security + Failure Tests

Test invalid input, auth failures, unavailable tool, timeout, crash, cancellation, and cleanup.

### Phase 9 — Distribution

If in scope, verify clean-machine installation and lifecycle management.

### Phase 10 — Release Gate

Capture evidence and only then promote the MCP to `VERIFIED`.

---

## 29. Tool Selection for This Project

The repository's existing research archive is the source for determining which tools receive dedicated MCP documentation.

Known researched targets include:

- OpenCode
- Omni Router
- Codex
- Claude Code
- Prime Agent
- Atomic Agents
- OpenClaw
- Freebuff / Codebuff
- DeepSeek Harness
- NemoClaw
- Pi Agent
- Strix

Hermes is the master/orchestrator and therefore is documented as the controller rather than treated as an ordinary worker MCP unless later research establishes a separate justified boundary.

The final inclusion/status of each target must be evidence-driven. A tool may be marked `BLOCKED` or `UNSUPPORTED` rather than forcing an MCP design when the required integration surface does not exist or cannot be verified.

---

## 30. Relationship With FROGE

The dedicated MCPs are independent components first.

Later, FROGE can provide ecosystem lifecycle management:

```text
                 HERMES
                    |
       +------------+------------+
       |            |            |
    MCP-A         MCP-B        MCP-C
       |            |            |
    Tool-A        Tool-B       Tool-C
       \            |           /
        +-----------+----------+
                    |
                 FROGE
          lifecycle/system layer
```

FROGE may eventually handle:

- Discovery.
- Installation.
- Configuration.
- Startup.
- Shutdown.
- Health/readiness.
- Version tracking.
- Updates.
- Runtime/session management.
- Logging/audit.
- MCP registry/cataloging.
- Compatibility checks.

These responsibilities must not turn FROGE into the master reasoning agent.

---

## 31. Final Quality Standard

An individual MCP is considered documentation-complete only when a new engineer/agent can answer all of these questions without guessing:

1. What exact tool does this MCP control?
2. What real interface does it use?
3. What can the MCP actually do?
4. What can it not do?
5. How is it installed?
6. How is it configured?
7. How is it authenticated?
8. How is it started?
9. How does Hermes connect to it?
10. What exact MCP tools are exposed?
11. What are the input/output schemas?
12. What happens when the tool fails?
13. What security boundaries exist?
14. How is the integration tested?
15. What has actually been verified?
16. What evidence proves verification?
17. What remains unknown or blocked?
18. What is the implementation sequence?
19. What skill should Hermes use for this MCP?
20. How will FROGE later manage this MCP without taking over Hermes's orchestration role?

If any answer requires an unsupported assumption, the documentation must explicitly say `UNKNOWN`, `INFERRED`, or `BLOCKED`.

---

## 32. Definition of Done

A dedicated MCP package reaches `DOCUMENTATION COMPLETE` when:

- Research is evidence-backed.
- Architecture is defined.
- Integration surface is identified.
- MCP contract is explicit.
- Tool inventory is complete.
- Capabilities are classified.
- Authentication/security are defined.
- Configuration/runtime/lifecycle are defined.
- Installation is documented.
- Error semantics are defined.
- Testing and verification gates are defined.
- Hermes integration is defined.
- Skill is specified.
- Task and tracker are present.
- Decisions and limitations are recorded.
- Evidence requirements are explicit.
- Implementation plan is actionable.

`DOCUMENTATION COMPLETE` does **not** automatically mean `VERIFIED` or `PRODUCTION READY`.

---

## 33. Source of Truth

For this repository:

1. Existing research under `research/` is the primary evidence base for tool capabilities and integration surfaces.
2. Official source/documentation should be preferred when validating technical claims.
3. Local test evidence is required before promoting claims to verified implementation.
4. Unknowns must remain visible.
5. This document defines the standard for all future individual MCP documentation packages.

The objective is a clean, modular, evidence-first MCP ecosystem in which every tool has an independently understandable and independently verifiable integration path to Hermes.
