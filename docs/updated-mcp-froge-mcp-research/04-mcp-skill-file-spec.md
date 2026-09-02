# 04 — MCP Skill File Specification

## Purpose

Every individual MCP must ship with a dedicated skill file so Hermes, or another compatible agent, can understand how to use that MCP without guessing.

Recommended location:

```text
skills/<mcp-name>/SKILL.md
```

## Required sections

Each skill should contain:

1. **Identity** — MCP name and underlying tool.
2. **Purpose** — what the MCP gives Hermes access to.
3. **Startup** — exact verified command(s).
4. **Endpoint/transport** — exact verified connection information.
5. **Authentication** — how runtime credentials are supplied; never embed real secrets.
6. **Capabilities** — every exposed tool/action with a short description.
7. **Input contract** — required parameters, limits, and safe values.
8. **Output contract** — result/status/error shape.
9. **Lifecycle** — start, status, stop, restart, and cancellation behavior where supported.
10. **Underlying tool interface** — CLI/API/RPC/SDK/native MCP/etc.
11. **Permissions** — read/write/high-risk boundaries.
12. **Failure modes** — expected errors and recovery behavior.
13. **Verification state** — `RESEARCHED`, `IMPLEMENTED`, `VERIFIED`, `BLOCKED`, or `UNSUPPORTED`.
14. **Evidence** — links/notes identifying the test or repository evidence behind claims.
15. **Examples** — short safe examples using placeholders rather than credentials.

## Skill design rule

The skill file is operational documentation, not marketing copy. It must tell Hermes what the MCP actually supports today.

## Combined system discovery

FROGE may expose an index of installed MCP skills, but each skill remains independently authoritative for its own MCP capabilities.

Conceptually:

```text
FROGE skill index
  |
  +-- OpenCode MCP skill
  +-- Codex MCP skill
  +-- Claude Code MCP skill
  +-- Pi Agent MCP skill
  +-- ...
```

## No hidden assumptions

If a tool's research does not establish an integration method, the skill must say so. The implementation cannot silently convert an inference into a claimed capability.
