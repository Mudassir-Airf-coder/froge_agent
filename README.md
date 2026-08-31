# FROGE Agent

**FROGE** is a modular AI Development Control Plane intended to orchestrate models, tools, skills, MCP servers, memory, and local computer capabilities through one controlled, verifiable architecture.

> **Current Status (2026-08-31):** Documentation and architecture foundation.  
> Implementation has not started beyond a package stub.  
> The repository is the persistent source of truth.

## Quick Orientation for Any New Agent

1. Read [`docs/CURRENT-STATE.md`](docs/CURRENT-STATE.md) — what actually exists.
2. Read [`docs/tracker.md`](docs/tracker.md) — what is done / next / blocked.
3. Read [`docs/task.md`](docs/task.md) — the work breakdown.
4. Read [`docs/flow.md`](docs/flow.md) — current vs target lifecycle.
5. Read [`docs/GAPS.md`](docs/GAPS.md) — known gaps.
6. Read the contracts below.
7. Follow the operating rules in [`AGENTS.md`](AGENTS.md).

## Vision (Summary)

FROGE aims to become a single control layer that can discover, install, configure, verify, operate, monitor, and recover an ecosystem of AI development tools and agents on a developer machine (Windows-first).

It is **not** merely an installer, a chatbot, a single coding agent, or a single model router.

## Core Design Principles

1. Documentation is the source of truth.
2. Architecture before implementation.
3. Verification before mutation.
4. Never assume installation success.
5. One clear control plane.
6. Provider/model selection is a replaceable layer.
7. Failures are classified events; recovery is verified before trusted.
8. Memory stores useful knowledge and evidence, not noise.
9. No secrets in Git.
10. Changes must remain understandable and reversible.
11. Idempotent desired-state bootstrap.
12. Explicit tool and agent role contracts (no silent overlap).

## Current Repository Structure (Actual)

```text
froge_agent/
├── README.md
├── AGENTS.md                 # Operating contract for agents working on FROGE
├── ORCHESTRATOR.md           # Orchestrator responsibilities & pipeline
├── docs/
│   ├── CURRENT-STATE.md      # What actually exists right now
│   ├── GAPS.md               # Gap analysis
│   ├── flow.md               # Current vs target execution flow
│   ├── task.md               # Work breakdown with IDs & acceptance criteria
│   ├── tracker.md            # Live progress board
│   ├── ARCHITECTURE.md
│   ├── MCP_CONTROL_PLANE.md  # Intent only — implementation deferred
│   ├── ROADMAP.md
│   ├── bootstrap.md
│   ├── tools.md
│   ├── agents.md
│   ├── providers.md
│   ├── skills.md
│   ├── plugins.md
│   ├── health.md
│   ├── recovery.md
│   ├── security.md
│   ├── testing.md
│   └── adr/                  # Architecture Decision Records
└── src/froge/
    └── __init__.py           # Package stub (__version__ = "0.1.0")
```

Folders such as `mcp/`, `skills/`, `providers/`, `tests/`, `scripts/`, `config/` are **planned** and do not exist yet.

## Key Contracts

| Document | Purpose |
|----------|---------|
| [AGENTS.md](AGENTS.md) | How agents must operate on this repository |
| [ORCHESTRATOR.md](ORCHESTRATOR.md) | Central decision/execution layer contract |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System layers |
| [docs/MCP_CONTROL_PLANE.md](docs/MCP_CONTROL_PLANE.md) | Future MCP boundary (implementation deferred — ADR-004) |
| [docs/bootstrap.md](docs/bootstrap.md) | Desired-state machine |
| [docs/health.md](docs/health.md) | Health ladder & vocabulary |
| [docs/recovery.md](docs/recovery.md) | Failure taxonomy & recovery pipeline |
| [docs/security.md](docs/security.md) | Security principles |
| [docs/testing.md](docs/testing.md) | Evidence standard |

## Explicitly Out of Scope (Current Phase)

- MCP server/client implementation
- Omni Router MCP
- Mega MCP construction or redesign
- Frontend / UI / design.md
- Any production runtime code beyond the documentation foundation

See ADR-004 and ADR-005.

## Build Phases (High Level)

See [docs/ROADMAP.md](docs/ROADMAP.md) and the detailed task list in [docs/task.md](docs/task.md).

- **Phase 0** — Repository audit & documentation foundation (in progress)
- **Phase 1** — Core architecture contracts (documentation)
- Later phases — Implementation against the documented contracts

## Security

Never commit API keys, access tokens, passwords, private keys, or other credentials.  
Use environment variables or secure local credential storage.  
See [docs/security.md](docs/security.md).

## License

License will be selected during the implementation/release phase.
