# 06 — Security Model

## 1. Credential rules

- Runtime tokens are generated with a cryptographically secure random source.
- Tokens are session/runtime credentials, not public API keys.
- Never commit tokens, API keys, cookies, auth files or private credentials.
- Never print credentials in normal logs or verification reports.
- Use timing-safe token comparison.

## 2. Authentication

The FROGE server must require authentication for protected operations while allowing only the minimum necessary unauthenticated health/diagnostic surface.

## 3. Authorization

Authentication answers `who is connected`; authorization answers `what they may do`.

FROGE must enforce capability-level permissions so that Hermes cannot accidentally turn a low-risk integration into unrestricted host execution.

## 4. Process execution

Tool adapters should prefer documented CLI/API/RPC interfaces. If a tool requires shell/process execution, the adapter must define:

- executable allow-list;
- argument validation;
- working-directory policy;
- environment-variable policy;
- timeout;
- cancellation behavior;
- stdout/stderr capture limits;
- exit-code mapping.

## 5. High-risk tools

Prime Agent research explicitly warns that its model-generated Python/project commands execute with user permissions and that its isolation is not a security sandbox. Treat this class of integration as high-risk and require external isolation before production use.

OpenCode, Codex, Claude Code and other tools may also expose powerful shell or full-access capabilities. FROGE must not erase their permission/sandbox controls merely to make automation convenient.

## 6. Remote exposure

Default deployment should remain local/localhost unless a deliberate secure remote-access design is implemented. Remote exposure requires transport security, authentication, authorization, and an explicit threat model.

## 7. Auditability

Each dispatched task should have a correlation ID and auditable lifecycle events without storing secrets. Logs must make it possible to answer what was requested, which adapter ran, what policy applied, and whether execution succeeded or failed.
