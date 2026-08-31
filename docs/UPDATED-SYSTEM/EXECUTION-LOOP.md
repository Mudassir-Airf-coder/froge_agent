# FROGE Loop / Harness Engineering Contract

## Core loop

The implementation agent must operate as a bounded, evidence-driven loop rather than stopping after writing code.

```text
READ -> PLAN -> IMPLEMENT -> TEST -> VERIFY -> AUDIT -> UPDATE DOCS
  ^                                      |
  |------------ NEXT UNFINISHED TASK ----|
```

## Start-of-loop

1. Read `docs/UPDATED-SYSTEM/README.md`.
2. Read `.context.md`.
3. Read `CURRENT-IMPLEMENTATION-STATUS.md`.
4. Read `task.md` and `tracker.md`.
5. Inspect the actual repository tree and current code.
6. Select the highest-priority unfinished task whose dependencies are satisfied.

## End-of-loop

A task may move to COMPLETE only after:

- implementation exists;
- tests pass;
- runtime behavior is checked where applicable;
- failure paths are checked where applicable;
- evidence is recorded;
- documentation matches code;
- `task.md` and `tracker.md` are updated;
- `.context.md` is updated;
- changes are committed/pushed.

## Context-window checkpoint

Before the context window becomes unsafe or after a major milestone, write a concise checkpoint to `.context.md`. Never rely on hidden conversation memory for project state.

## Failure loop

If a task fails:

`capture evidence -> classify -> fix -> retest -> reverify`

Do not mark the task complete merely because a patch was written.

## Stop condition

The agent stops only when the task system declares the implementation scope complete and the final verification gates pass. If blocked by missing external research, record the blocker precisely and continue with independent tasks rather than inventing facts.
