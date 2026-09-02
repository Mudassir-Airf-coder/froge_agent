# 08 — Verification Matrix

## Core rule

Every MCP must pass an evidence gate independently before it is included in the combined FROGE system.

| Gate | Required evidence |
|---|---|
| Source | Underlying tool repository/docs inspected |
| Install | Tool is actually installed or a reproducible setup exists |
| Discover | MCP can find/identify the tool |
| Health | MCP can prove usable runtime state |
| Capabilities | MCP reports only verified operations |
| Auth | Authentication works with real credentials/session handling |
| Hermes connect | Hermes connects to the MCP for real |
| Hermes discovery | Hermes can discover the MCP's capabilities |
| Execution | Hermes can request a real operation |
| Tool control | Underlying tool actually performs the requested work |
| Result | Result reaches Hermes correctly |
| Error | Failure is surfaced accurately |
| Permission | Restricted/unsafe requests are correctly controlled |
| Lifecycle | Start/stop/restart works as documented |
| Skill | Skill file matches actual behavior |
| Evidence | Test command/output or equivalent proof is recorded |

## Combined-system gate

After individual MCP verification:

1. Install/configure the collection.
2. Start multiple MCPs together.
3. Confirm each has an independent process/state.
4. Confirm runtime authentication works.
5. Connect Hermes.
6. Confirm Hermes can read every available skill.
7. Confirm Hermes can distinguish capabilities by MCP.
8. Execute at least one real task through each required MCP.
9. Confirm one failed MCP does not create a false global success state.
10. Confirm stop/restart behavior.

## Release states

- `RESEARCHED` — research only.
- `IMPLEMENTED` — code exists.
- `VERIFIED` — real end-to-end evidence exists.
- `BLOCKED` — required dependency/access/interface is unavailable.
- `UNSUPPORTED` — no safe verified integration path exists.

A combined release cannot be called complete while a required MCP remains only `RESEARCHED` or `IMPLEMENTED`.
