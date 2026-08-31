# FROGE — Current Implementation Status

**Baseline source:** repository state on `main` as inspected before this specification was added.

## Already implemented according to repository + implementation reports

- Packaging/config/logging/results/lifecycle state.
- Tool manifest and registry.
- Environment discovery.
- Installation abstraction with safe command execution.
- Health ladder L1–L6.
- Desired-state planner, dependency ordering and cycle detection.
- Bootstrap orchestration.
- Persistent `.froge/state.json` with atomic writes/audit operations.
- Generic adapter abstraction.
- Provider registry foundation.
- CLI: version, status, tools, doctor, plan, bootstrap, state, verify.
- JSON output and dry-run/idempotency paths.
- Universal install skill, skill runner and secret-redaction helpers.
- Research directory containing tool research documents.

The latest repository state reports 67 tests for the universal-install stage; future agents must rerun the actual current suite rather than trusting a historical number. The repository currently contains the research files and the updated system documentation created here.

## Not yet complete in the target system

1. Concrete, research-backed adapters for each approved external tool.
2. Complete machine bootstrap on a fresh Windows environment using verified installers.
3. Concrete functional health tests for each managed external tool.
4. Automatic update detection + safe update/rollback lifecycle.
5. Agent registry and real agent-to-agent task delegation.
6. MCP communication layer specifically for agent/tool communication.
7. Tool Expert workflow.
8. Skill Designer workflow and governed skill discovery/generation.
9. Capability revalidation after tool updates.
10. End-to-end continuous execution loop with durable context handoff.
11. Full failure injection/recovery verification.
12. Final hardening and release validation.

## Explicit exclusions

- Ollama.
- vLLM.
- Frontend/design.md.
- Generic/new MCP servers unrelated to agent communication.
- Omni Router MCP and Mega MCP unless explicitly re-authorized.
- Large uncontrolled skill/plugin catalog.

## Important documentation correction

Some older root documents still contain historical phrases such as “documentation-only” or “MCP deferred.” Treat this directory as the updated specification for the newly approved scope. Root documentation should be reconciled by the implementation agent rather than silently ignored.
