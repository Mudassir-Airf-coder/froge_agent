# FROGE — Updated System Specification

**Status:** AUTHORITATIVE IMPLEMENTATION SPECIFICATION (supersedes stale target-only statements where they conflict)

This directory defines the next-generation FROGE system agreed during the project design discussion. It is the documentation an implementation agent must read before changing the repository.

## Read order

1. `CURRENT-IMPLEMENTATION-STATUS.md` — what already exists and what remains.
2. `SYSTEM-SPEC.md` — complete target system and responsibilities.
3. `EXECUTION-LOOP.md` — loop/harness engineering rules.
4. `MCP-AGENT-COMMUNICATION.md` — the only intended purpose of FROGE MCPs.
5. `SKILL-SYSTEM.md` — skill discovery, generation, installation, verification and ownership.
6. `UPDATE-SYSTEM.md` — automatic tool update detection and safe upgrade flow.
7. `task.md` — executable implementation backlog.
8. `tracker.md` — live completion state.
9. `.context.md` — durable handoff/context file for context-window exhaustion.
10. `IMPLEMENTATION-PROMPT.md` — copy/paste prompt for a coding agent.

## Binding scope decisions

- MCP work is allowed only for **agent-to-agent/tool-to-agent communication and task delegation**. Do not build unrelated MCP servers.
- Omni Router MCP, Mega MCP and arbitrary capability MCPs are not part of this implementation unless explicitly re-authorized.
- Ollama and vLLM are excluded.
- Frontend/design work is excluded from this cycle.
- A large skills/plugin catalog is excluded; the architecture must support it later without forcing it now.
- External install/update commands must come from verified research in `research/`, not invented commands.
- CodeBuff/FreeBuff is the execution/coding layer used to build and operate the system; FROGE owns orchestration, verification, state and lifecycle policy.
- Every implementation change must be tested, evidenced, documented and reflected in the tracker.
