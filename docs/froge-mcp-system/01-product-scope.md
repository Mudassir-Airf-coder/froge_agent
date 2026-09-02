# 01 — Product Scope

## 1. Goal

Build FROGE MCP as the MCP communication/control layer for Hermes. Hermes decides what should happen; FROGE connects Hermes to verified tools and carries controlled requests/results between them.

## 2. In scope

- MCP server/runtime lifecycle.
- Authentication and session handling.
- Tool/adapter discovery.
- Tool capability discovery.
- Controlled command/task dispatch.
- Process lifecycle management where a tool exposes a supported CLI/API/RPC surface.
- Structured result, status and error reporting.
- Per-tool permissions and execution policy.
- Hermes connection and FROGE MCP skill.
- One-line distribution installer and verification.
- Evidence-backed verification of each supported tool.
- Logs/audit events without leaking secrets.

## 3. Out of scope

- Replacing Hermes as master orchestrator.
- Becoming an LLM/model router; OmniRoute remains separate.
- Regenerating or replacing Omni Router MCP.
- A marketplace for arbitrary MCP servers/skills.
- Blind unrestricted terminal execution for every tool.
- Claiming compatibility merely because two products both mention MCP.
- Installing Ollama/vLLM as part of the universal FROGE installer.

## 4. Core acceptance criteria

FROGE is target-complete only when:

1. Hermes can authenticate to FROGE.
2. Hermes can discover the currently enabled FROGE capabilities.
3. A verified adapter can be selected for a supported tool.
4. Hermes can submit a bounded task through FROGE.
5. The tool executes through its documented/supported interface.
6. FROGE captures status, stdout/stderr or API result, exit/error state, and correlation ID.
7. Hermes receives a structured result.
8. Permission boundaries are enforced.
9. The installer works from a clean supported Windows environment.
10. Re-running installation does not corrupt the existing installation/configuration.
11. Every claimed supported tool has a real verification record.

## 5. Evidence states

- `RESEARCHED` — documented in `research/` only.
- `INFERRED` — technically plausible but not directly confirmed.
- `IMPLEMENTED` — code exists locally.
- `VERIFIED` — real end-to-end test passed.
- `BLOCKED` — required prerequisite is unavailable.
- `UNSUPPORTED` — explicitly outside the supported interface/scope.

Never promote `RESEARCHED` or `INFERRED` directly to `VERIFIED`.
