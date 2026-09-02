# 09 — One-Line Installer Specification

## Goal

The final distribution should provide a normal CLI-style experience:

```powershell
<one-line-install-command>
```

then:

```powershell
froge-mcp start
```

The installer is separate from the runtime start command.

## Installer responsibilities

- Obtain the published FROGE package/repository from the official project source.
- Install the FROGE CLI.
- Install/register the required individual MCP packages/components.
- Create user-scoped configuration/runtime directories.
- Avoid writing secrets into the repository.
- Perform basic post-install validation.
- Be safe to run again.

## Startup responsibilities

`froge-mcp start` must operate as a runtime command, not as an installation script. It should:

- load configuration;
- discover configured MCPs;
- start them independently;
- generate/manage runtime token/session state;
- health-check them;
- expose readiness to Hermes.

## Clean-machine proof

The one-line installer is not considered verified until tested on a Windows environment that does not already contain the FROGE installation/configuration.

Required proof:

```text
ONE-LINE INSTALL
   -> CLI AVAILABLE
   -> DOCTOR/HEALTH PASS
   -> FROGE START
   -> ALL REQUIRED MCPs START
   -> HERMES CONNECTS
   -> REAL TASK EXECUTES
```

## Idempotency proof

Run the installer/setup a second time and verify:

- no broken duplicate CLI;
- no corrupted configuration;
- no duplicate process registrations;
- no lost valid user configuration;
- system still starts;
- Hermes still connects.

## Repository URL rule

The final installer URL must point to the actual published FROGE repository/file location. A placeholder or untested raw URL must never be presented as verified.
