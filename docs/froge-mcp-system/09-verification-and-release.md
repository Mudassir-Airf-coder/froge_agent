# 09 — Verification and Release

## Evidence gate

A feature is not complete because code exists or a test was written. It is complete when the relevant behavior has been exercised and the result is recorded.

## Core gates

### Gate A — Core
- unit/integration/security tests pass;
- CLI starts/stops correctly;
- authentication works;
- protected operations reject missing/invalid credentials;
- configuration is user-scoped and CWD-independent.

### Gate B — Distribution
- published/package install succeeds without editable mode;
- one-line installer succeeds from the canonical remote source;
- a new PowerShell session resolves `froge-mcp`;
- doctor/start/status/stop work after installation.

### Gate C — Idempotency
- installer repeated on an installed system;
- existing configuration preserved;
- no broken duplicate command;
- no credential leakage;
- recovery from a partial/failed install is documented.

### Gate D — Hermes
- Hermes connects with the runtime credential;
- handshake/verification succeeds;
- capability discovery is visible to Hermes;
- one controlled task completes end-to-end;
- failure is returned correctly.

### Gate E — Tool integrations
For each required tool:
- install/version verified;
- interface discovery verified;
- authentication verified where required;
- at least one real task verified;
- result captured;
- failure/timeout behavior verified;
- security policy verified.

### Gate F — Clean machine
Repeat the minimum installation and Hermes connection flow on a separate supported Windows environment with no prior FROGE installation.

## Release labels

- `DEV` — implementation exists.
- `RC` — all core and distribution gates pass, external integrations may still be incomplete.
- `READY` — required tool integrations and clean-machine flow pass.
- `PRODUCTION` — operational, security, update/recovery and support requirements defined and tested for the intended deployment environment.

Never label a release `PRODUCTION` solely because automated tests pass.
