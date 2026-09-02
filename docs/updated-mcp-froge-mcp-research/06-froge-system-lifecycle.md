# 06 — FROGE System Lifecycle

## Goal

The combined FROGE layer should make the collection of individual MCPs feel like one installable system without collapsing their implementations into one MCP.

## Installation

Target experience:

```powershell
irm <official-froge-installer> | iex
```

The installer must install the FROGE system and its MCP components using the actual published repository/package locations. The final URL is not considered verified until it is tested from a fresh environment.

## Startup

Target user experience:

```powershell
froge-mcp start
```

The command should:

1. Load system configuration.
2. Discover configured MCPs.
3. Prepare runtime directories.
4. Generate or load the appropriate runtime authentication material.
5. Start each configured MCP independently.
6. Health-check each MCP.
7. Record readiness/failure state.
8. Publish the Hermes connection information.

## Process supervision

FROGE should know which MCP process belongs to which integration. It should not hide failures by reporting one global `READY` when one or more required MCPs are down.

## Runtime token

The runtime token is a session credential for the managed MCP environment. It must:

- be generated securely;
- never be committed to Git;
- never be hardcoded;
- never be printed unnecessarily;
- be protected with appropriate file permissions;
- be invalidated/rotated according to the runtime lifecycle.

The exact token propagation model must be implemented consistently across the individual MCPs.

## Status

The system should be able to distinguish at least:

- `READY`
- `PARTIAL`
- `STARTING`
- `STOPPING`
- `FAILED`
- `AUTH_FAILED`
- `MCP_UNAVAILABLE`

## Stop/restart

The system must support controlled stop/restart of the MCP collection while retaining per-MCP state. A restart must not accidentally destroy user configuration or credentials that are intentionally persistent.

## CWD independence

The user should be able to run the system command from an arbitrary working directory. Configuration and runtime state must use explicit user/system locations rather than relying on the current directory.

## Idempotency

Repeated installation/setup should not create broken duplicate registrations, corrupt valid configuration, or require manual cleanup. This must be proven by test, not assumed.
