# FROGE Architecture

**Last updated:** 2026-08-31  
**Status:** Target architecture documented; implementation is documentation-only at this stage.

## System Model (Target)

```text
User / Agent Request
        │
        ▼
┌────────────────────┐
│ FROGE Orchestrator │
└─────────┬──────────┘
          │
   ┌──────┼───────────────┐
   ▼      ▼               ▼
 Planner  Policy       Session
   │      Engine        Manager
   └──────┬───────────────┘
          ▼
┌──────────────────────────┐
│ Capability / MCP Control  │
│ Plane (future)            │
└────────────┬─────────────┘
             │
   ┌─────────┼──────────┐
   ▼         ▼          ▼
Providers  Tools      Skills
Models     Runtimes   Agents
   │         │          │
   └─────────┼──────────┘
             ▼
       Execution Layer
             │
       ┌─────┴─────┐
       ▼           ▼
   Verification  Recovery
       │           │
       └─────┬─────┘
             ▼
       Memory / Evidence
```

## Core Layers (Target)

1. **Orchestration** — intent, planning, routing, execution coordination, result handling (see ORCHESTRATOR.md).
2. **Provider and Model Layer** — abstraction, health, failover (see providers.md).
3. **MCP Control Plane** — discoverable, permissioned, observable tools (implementation deferred — ADR-004).
4. **Skill Layer** — reusable operational knowledge (see skills.md).
5. **Context and Memory** — selective session + durable operational knowledge (future).
6. **Recovery** — classified failures + verified recovery (see recovery.md).
7. **Verification** — evidence-based testing (see testing.md).

## Bootstrap Layer (Prerequisite)

Machine preparation via desired-state detection and idempotent install/update/repair/verify (see bootstrap.md).

## Design Boundary

The orchestrator coordinates layers; it must not become a monolithic implementation of every provider, tool, or skill.

## Local System Integration

FROGE is intended to control approved software and runtimes through the control-plane layer. Secrets remain outside Git.

## Current Reality vs Target

See `docs/CURRENT-STATE.md` and `docs/flow.md`. Almost all of the above is still target architecture. Only documentation and a package stub exist.

## Related Living Documents

- docs/flow.md
- docs/task.md
- docs/tracker.md
- docs/GAPS.md
- docs/adr/
