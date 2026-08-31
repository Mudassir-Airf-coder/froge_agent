# FROGE Security Principles

**Status:** DOCUMENTED ONLY  
**Last updated:** 2026-08-31

## Non-Negotiable Rules

1. **Never commit secrets** — API keys, tokens, passwords, private keys, session cookies, or any credential material.
2. Secrets live in environment variables, local credential stores, or other secure mechanisms outside Git.
3. Documentation and knowledge records must never contain real credentials.
4. Logs and evidence must redact secrets.
5. Least privilege for agents, MCPs, and tools.
6. Filesystem and vault boundaries must be respected.
7. Destructive operations require explicit safeguards / confirmation where appropriate.
8. Important actions should be auditable.

## Current Reality

Only the policy statements exist. No secret-store implementation, no redaction library, no permission engine yet.

## Future Work

Concrete secret handling design will be added when configuration and provider integration phases begin. Until then the rule is absolute: no real credentials in the repository.

## Related

- README.md Security section
- AGENTS.md rule 6
