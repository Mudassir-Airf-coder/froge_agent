# FROGE Testing Philosophy

**Status:** DOCUMENTED ONLY  
**Last updated:** 2026-08-31

## Core Rule

A task is not complete because code was written or a command returned exit code 0.  
It is complete when the intended capability has been **executed, verified, and evidenced**.

## Target Test Layers

- Preflight / environment checks
- Installation tests
- Configuration tests
- Health tests
- Functional / capability tests
- MCP tests (when MCP work begins)
- Provider / model tests
- Integration tests
- End-to-end tests
- Failure-injection tests
- Regression tests

## Evidence Standard

IMPLEMENTED → EXECUTED → VERIFIED → EVIDENCED

Never claim:
- COMPLETE
- PASS
- INTEGRATED
- HEALTHY

without the corresponding evidence.

## Current Reality

Zero tests exist in the repository.

## Related

- docs/health.md
- docs/task.md (every task has Acceptance Criteria + Evidence Required)
- AGENTS.md completion standard
