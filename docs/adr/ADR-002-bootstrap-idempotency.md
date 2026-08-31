# ADR-002: Bootstrap Idempotency

**Status:** Accepted  
**Date:** 2026-08-31

## Context

Blind reinstallation or upgrading is unsafe and non-reproducible.

## Decision

Bootstrap must be desired-state and idempotent: detect MISSING / OUTDATED / CURRENT / BROKEN / UNKNOWN and act accordingly. Re-running on a healthy system verifies and keeps; it does not destroy.

## Consequences

- Detection and classification precede mutation.
- Verification evidence is required after every action.
- Implementation of bootstrap must follow the state machine in docs/bootstrap.md.
