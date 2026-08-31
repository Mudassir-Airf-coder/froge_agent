# FROGE Failure & Recovery Model

**Status:** DOCUMENTED ONLY  
**Last updated:** 2026-08-31

## Target Pipeline

```
DETECT
  ↓
CLASSIFY
  ↓
DIAGNOSE
  ↓
REPAIR / FAILOVER / RETRY (bounded)
  ↓
VERIFY
  ↓
RECORD (knowledge + recovery memory)
```

## Failure Categories (Target Taxonomy)

- INSTALLATION_FAILURE
- CONFIGURATION_FAILURE
- AUTH_FAILURE / API_KEY_ERROR
- PROVIDER_FAILURE / PROVIDER_UNAVAILABLE
- MODEL_FAILURE / MODEL_UNAVAILABLE
- RATE_LIMIT / QUOTA_EXCEEDED
- NETWORK_ERROR / TIMEOUT
- GATEWAY_FAILURE
- DEPENDENCY_FAILURE
- PORT_CONFLICT
- PERMISSION_FAILURE
- RUNTIME_FAILURE
- UNKNOWN_FAILURE

## Recovery Principles

1. Never treat a fallback as trusted until it has been health-checked and functionally verified.
2. Cooldowns for repeatedly failing providers/models.
3. Successful recovery paths should become useful memory for future routing (model-health memory).
4. Same-session continuity is a goal; exact mechanism is **TBD**.
5. All recovery actions must be explainable and recorded.

## Current Reality

No recovery implementation exists. The above is target architecture only.

## Related

- ORCHESTRATOR.md (recovery is part of the pipeline)
- docs/health.md
- docs/providers.md
