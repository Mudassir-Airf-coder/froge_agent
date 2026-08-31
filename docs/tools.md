# FROGE Tool Ecosystem

**Status:** DOCUMENTED AS CONCEPTUAL / REQUIRES VALIDATION  
**Last updated:** 2026-08-31

## Rule

No tool capability is treated as fact until verified against official documentation or the actual installed artifact.  
All roles below are **architectural hypotheses** derived from project intent, not verified claims.

## Tools Currently Referenced by Project Intent

| Tool | Proposed Role | Current Repo Status | Verification Status |
|------|---------------|---------------------|---------------------|
| OpenCode | Primary Software Engineering / Coding Agent | Not present | REQUIRES VALIDATION |
| Hermes | Persistent Automation / Long-Running Agent Runtime | Not present | REQUIRES VALIDATION |
| OpenClaw | Autonomous Agent / Automation Runtime | Not present | REQUIRES VALIDATION |
| NemoClaw / Nemo-related | NVIDIA-Oriented Agent/Runtime Integration | Not present | REQUIRES VALIDATION |
| Prime Agent | Specialized Development/Agent Runtime | Not present | REQUIRES VALIDATION |
| FreeBuff | Lightweight / free coding-agent path (project-specific workflow) | Not present | REQUIRES VALIDATION |
| Omni Router | Provider / Model Routing Layer | Not present | REQUIRES VALIDATION |

## Required Fields for Every Tool (Template)

When a tool is promoted from “REQUIRES VALIDATION” to documented:

- Tool Name
- Role
- Why FROGE Uses It
- Responsibilities
- Non-Responsibilities
- Inputs / Outputs
- Dependencies
- Provider / Model Requirements
- Configuration
- Runtime / Gateway
- Health Check definition
- Functional Check definition
- Failure Modes
- Recovery
- Integration Points
- Permissions
- Current Status (in repo)
- Target Status
- Research sources + date

## Explicit Current-Phase Restriction

- Do **not** implement any of these tools.
- Do **not** create Omni Router MCP or any MCP servers.
- Only document the future integration boundary.

## Related

- docs/agents.md (runtime agent contracts will reference these tools)
- docs/GAPS.md (Tool Ecosystem gap)
