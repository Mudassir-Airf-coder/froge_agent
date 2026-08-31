# FROGE Health Model

**Status:** DOCUMENTED ONLY  
**Last updated:** 2026-08-31

## Core Principle

**Installed ≠ Configured ≠ Running ≠ Healthy ≠ Functionally Verified**

A process existing or a `--version` command succeeding is never sufficient proof that a capability works.

## Target Health Ladder (per important tool / service)

1. **Discoverable / Installed** — binary or package present
2. **Correct version** — meets compatibility constraints
3. **Executable available** — on PATH or configured location
4. **Configuration valid** — required config files / env present and parseable
5. **Service / Gateway running** (if applicable) — process + port / endpoint
6. **API / endpoint responding** — basic reachability
7. **Authentication valid** — credentials accepted (without exposing them)
8. **Functional test successful** — a minimal real capability exercise passes and produces evidence

## Health Status Vocabulary (Target)

- `UNKNOWN`
- `MISSING`
- `INSTALLED`
- `CONFIGURED`
- `RUNNING`
- `HEALTHY`
- `FUNCTIONALLY_VERIFIED`
- `DEGRADED`
- `FAILED`
- `COOLDOWN`

Exact enum and evidence schema are TBD and must be defined before implementation.

## Evidence Requirement

Every health claim must be accompanied by observable evidence (command output, response, log excerpt, test result) that can be recorded.

## Related

- docs/bootstrap.md
- docs/recovery.md
- docs/testing.md
