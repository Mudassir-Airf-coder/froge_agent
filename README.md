# FROGE Agent

**FROGE** is the working name for a modular, autonomous AI agent system designed to orchestrate models, tools, skills, MCP servers, memory, and local computer capabilities through one controlled architecture.

> **Status:** Architecture and documentation foundation — build phase starting.

## Vision

FROGE is intended to become a single control layer for an AI coding and automation workflow. Instead of treating every model, provider, CLI, MCP server, skill, and local tool as an isolated system, FROGE provides a common orchestration layer that can discover capabilities, select the right tool/model, preserve context, execute work, verify results, and recover from failures.

The project is being built in stages: **define → document → architect → implement → integrate → verify → operate**.

## Core Goals

- **Orchestration:** coordinate models, agents, tools, skills, and workflows.
- **Provider abstraction:** keep provider/model selection separate from application logic.
- **MCP control plane:** expose and control approved tools through a consistent MCP layer.
- **Context and memory:** preserve useful operational knowledge without blindly retaining noise.
- **Self-healing:** detect provider/model failures and recover through verified fallback paths.
- **Skills:** turn repeatable workflows into reusable, testable capabilities.
- **Verification:** important actions should have observable evidence and tests.
- **Local control:** integrate with installed tools and runtimes without hard-coding secrets.
- **Extensibility:** new providers, models, tools, MCP servers, and skills should be pluggable.

## High-Level Architecture

```text
                         ┌──────────────────────┐
                         │      FROGE Agent     │
                         │   Master Controller  │
                         └──────────┬───────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
       ┌─────▼─────┐          ┌─────▼─────┐          ┌─────▼─────┐
       │ Orchestrator│          │ Context & │          │  Policy & │
       │ / Planner  │          │  Memory   │          │  Safety   │
       └─────┬─────┘          └─────┬─────┘          └─────┬─────┘
             └──────────────────────┼──────────────────────┘
                                    │
                         ┌──────────▼──────────┐
                         │    MCP Control Plane │
                         └──────────┬──────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
   ┌────▼────┐                ┌─────▼─────┐               ┌─────▼─────┐
   │ Models & │                │   Tools   │               │  Skills   │
   │Providers │                │ / Runtime │               │ / Agents  │
   └─────────┘                └───────────┘               └───────────┘
                                    │
                         ┌──────────▼──────────┐
                         │ Verification / E2E   │
                         │ Evidence / Recovery │
                         └──────────────────────┘
```

## Repository Structure

```text
froge_agent/
├── README.md
├── AGENTS.md
├── ORCHESTRATOR.md
├── docs/
│   ├── VISION.md
│   ├── ARCHITECTURE.md
│   ├── ROADMAP.md
│   ├── MCP_CONTROL_PLANE.md
│   └── VERIFICATION.md
├── src/                  # FROGE implementation
├── mcp/                  # FROGE MCP control plane
├── skills/               # Reusable FROGE skills
├── providers/            # Provider/model adapters
├── tests/                # Unit/integration/E2E tests
├── scripts/              # Bootstrap, diagnostics, verification
└── config/               # Sanitized, non-secret configuration
```

## Design Principles

1. Architecture before accidental complexity.
2. One source of truth for project decisions.
3. Provider/model selection is a replaceable layer.
4. No secrets in Git; use environment variables or secure local credential storage.
5. Every integration gets a health check.
6. Every critical workflow gets an end-to-end test.
7. Failures become classified events, not mysterious exceptions.
8. Recovery must be verified before a fallback is trusted.
9. Memory stores useful knowledge and evidence, not uncontrolled noise.
10. Changes should remain understandable and reversible.

## Build Phases

### Phase 0 — Foundation
Repository structure, vision, architecture, operating contract, and documentation standards.

### Phase 1 — Control Plane
Configuration model, tool registry, provider/model registry, health checks, and execution contracts.

### Phase 2 — MCP Layer
MCP server/client architecture, tool discovery, lifecycle/health, and permission boundaries.

### Phase 3 — Orchestration
Intent intake, planning, routing, execution, and result validation.

### Phase 4 — Context & Memory
Session state, persistent operational memory, retrieval, and knowledge-graph integration where appropriate.

### Phase 5 — Recovery
Error classification, provider/model fallback, retry/cooldown policy, and recovery memory.

### Phase 6 — Verification
Unit, integration, contract, E2E, and regression testing.

### Phase 7 — Operational Build
Local installation/bootstrap, diagnostics, observability, documentation completion, and stable release workflow.

## Current State

The repository is now the documentation and architecture foundation for FROGE. Implementation should proceed against documented contracts and milestones rather than growing through disconnected experiments.

## Security

Never commit API keys, access tokens, passwords, session cookies, private keys, or other credentials. Use environment variables, local credential stores, and sanitized configuration examples.

## License

License will be selected during the implementation/release phase.
