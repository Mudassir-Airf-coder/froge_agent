# FROGE Automatic Tool Update System

## Goal

Once an approved tool is installed, FROGE must keep its lifecycle under management and detect meaningful version updates without breaking a working environment.

## Update pipeline

```text
Installed + Verified Tool
        |
        v
Version / Update Signal
        |
        v
New Version Candidate
        |
        v
Research + Compatibility Validation
        |
        v
Update Plan
        |
        v
Approved Adapter Update
        |
        v
Version Verification
        |
        v
Functional / Regression Verification
        |
   +----+----+
   |         |
 PASS      FAIL
   |         |
 RECORD   RECOVER / ROLLBACK / BLOCK
```

## Rules

- Never update solely because a newer version string exists; compatibility and adapter evidence are required.
- Never fabricate a release URL, package command or migration step.
- Preserve the previous known-good state where practical.
- Record current version, target version, adapter used, verification output and result.
- Re-running the updater on an already-current tool must be a no-op.
- Updates that change tool capabilities should trigger a capability/skill revalidation check.
- Secrets must never enter logs, Git commits or `.context.md`.

## Future extension

The same mechanism may later monitor tool capability changes, not only version numbers, so newly introduced functions can be reflected in the tool registry and relevant skills.
