# FROGE Agent — Live Tracker

**Last updated:** 2026-09-01

## Snapshot

| Item | Value |
|------|-------|
| Status | Bootstrap COMPLETE + **Universal Install Skill ACTIVE** |
| Tests | **67 passed** |
| Skill | `skills/froge-universal-install.skill.md` |
| CLI | + `froge install-skill` |

## Board

- 🟢 Bootstrap control plane
- 🟢 Universal Tool Installation & Verification Skill
- 🟢 Skill runner + report format
- 🟢 Secret redaction helpers
- 🟢 Expanded inventory (nimble-clock, ohsc, graphify as REQUIRES_VALIDATION)
- ⬜ Concrete external tool adapters (verified research required)
- ⬜ Windows winget IDs (verified research required)
- 🚫 MCP / skills catalog / plugins / frontend / Ollama / vLLM

## Evidence

- pytest: 67 passed
- froge install-skill --dry-run → PARTIAL, KEEP=4, REQUIRES_VALIDATION=10
- No invented external install commands
