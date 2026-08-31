# ADR-001: Documentation as Source of Truth

**Status:** Accepted  
**Date:** 2026-08-31

## Context

Conversation context is ephemeral. The project must remain understandable and resumable by any future agent that clones the repository.

## Decision

All architectural intent, decisions, current state, tasks, and progress must live in the repository documentation. The documentation is the contract that implementation follows.

## Consequences

- flow.md, task.md, tracker.md, and architecture docs are living documents.
- Implementation work must update documentation and tracker in the same change set when architecture or status changes.
- Chat history is never treated as the primary source of truth.
