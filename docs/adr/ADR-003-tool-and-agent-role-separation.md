# ADR-003: Tool and Agent Role Separation

**Status:** Accepted  
**Date:** 2026-08-31

## Context

Installing many AI tools without clear roles creates overlap, conflict, and unmaintainable orchestration.

## Decision

Every integrated tool and every runtime agent must have an explicit role contract (responsibilities, non-responsibilities, boundaries). Overlap requires an ADR that names the authoritative owner.

## Consequences

- docs/tools.md and docs/agents.md are mandatory before integration work.
- Roles start as hypotheses marked REQUIRES VALIDATION until verified.
