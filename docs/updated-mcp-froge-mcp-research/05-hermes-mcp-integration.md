# 05 — Hermes Integration

## Role

Hermes is the single master/orchestrator. It connects to and uses the MCPs; it does not become subordinate to FROGE.

## Connection model

```text
Hermes
  |
  +-- MCP connection / discovery
        |
        +-- OpenCode MCP
        +-- Codex MCP
        +-- Claude Code MCP
        +-- Pi MCP
        +-- ...
```

The final FROGE system may provide a managed entry point or aggregated discovery mechanism, but the individual MCP identity and capability boundaries remain explicit.

## Startup sequence

```text
FROGE install
    -> configure MCP collection
    -> FROGE start
    -> start configured MCPs
    -> create runtime session/token
    -> health-check MCPs
    -> publish ready state
    -> Hermes connects/authenticates
    -> Hermes reads MCP skills
    -> Hermes discovers capabilities
    -> Hermes dispatches work
```

## Hermes decision flow

1. Read available MCP skill information.
2. Match user intent to a verified capability.
3. Select the correct MCP.
4. Send a bounded task request.
5. Monitor status.
6. Receive result/error.
7. Decide next action.

## Important distinction

FROGE may manage processes and expose discovery information, but it must not make the user-intent planning decision that belongs to Hermes.

## Verification handshake

A successful integration test should provide evidence for:

- MCP endpoint reachable;
- authentication valid;
- Hermes recognized the MCP;
- capabilities were discoverable;
- Hermes successfully invoked at least one real capability;
- underlying tool performed the operation;
- result reached Hermes;
- failure paths are distinguishable.

## Research limitation

The existing research may identify Hermes behavior and the candidate tools without proving this exact final multi-MCP connection flow. Therefore this document defines the target architecture; the actual Hermes handshake remains an implementation/verification task until tested for real.
