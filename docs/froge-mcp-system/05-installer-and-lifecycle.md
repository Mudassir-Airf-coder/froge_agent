# 05 — Installer and Lifecycle

## 1. Installation UX

Target Windows UX:

```powershell
irm <official-froge-mcp-installer> | iex
```

The installer must install the published package from the canonical GitHub/release source, configure user-scoped runtime data, and verify the resulting CLI. The URL must be the real repository location and must be tested end-to-end before being documented as supported.

## 2. User-scoped data

Runtime configuration, authentication token and logs must live in a user-scoped location such as `%LOCALAPPDATA%\FROGE\MCP\`, not in the current working directory. Exact paths remain implementation-defined but must be documented by the shipped CLI/doctor command.

## 3. Lifecycle

```text
INSTALL
  ↓
VERIFY CLI
  ↓
DOCTOR
  ↓
START
  ↓
RUN SESSION
  ↓
STATUS / HEALTH
  ↓
STOP
  ↓
RESTART
```

## 4. Reinstall / idempotency

Running the installer again must not create duplicate/broken installations, destroy valid user configuration, expose secrets, or leave conflicting PATH entries. The installer should detect an existing installation and safely repair/update it.

## 5. Clean-machine acceptance test

Use a supported Windows machine/environment without an existing FROGE installation. Run only the documented prerequisites and the one-line installer. Then verify:

- command resolution from a new PowerShell session;
- version;
- doctor;
- start;
- authenticated status;
- mock/real capability;
- stop;
- restart.

## 6. Update policy

Version changes must be deliberate. The installer should not silently replace a running process in a way that loses active work. Update behavior and rollback/failure behavior must be documented and tested.

## 7. Uninstall

An uninstall path is desirable but is not a prerequisite for the core MCP architecture. If implemented, it must distinguish application files from user configuration/logs and require clear confirmation before destructive cleanup.
