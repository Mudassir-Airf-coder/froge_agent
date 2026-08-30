# FROGE Agent Operating Contract

## Purpose

This document defines how agents working on FROGE should operate.

## Rules

1. Read the relevant project documentation before changing architecture or interfaces.
2. Prefer small, reversible changes.
3. Do not invent integrations or claim a tool/model works without verification.
4. Keep provider-specific logic behind provider adapters.
5. Keep MCP tools explicit, typed, permission-aware, and observable.
6. Never commit secrets or private credentials.
7. Add or update tests for behavior changes.
8. Run the narrowest relevant tests first, then integration/E2E tests when appropriate.
9. Record important architectural decisions in `docs/`.
10. Treat runtime state and generated artifacts as separate from source code unless explicitly required.

## Change Workflow

**Inspect → Plan → Implement → Test → Review → Document → Commit**

## Completion Standard

A task is not considered complete merely because code was written. The changed behavior must be demonstrated by an appropriate test or verification command, and any architectural change must be documented.
