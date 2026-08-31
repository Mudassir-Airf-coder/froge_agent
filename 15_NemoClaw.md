# NemoClaw

## Identity
- Vendor: **NVIDIA**
- Category: An **OpenClaw plugin**, not a standalone agent — it packages NVIDIA's **OpenShell** sandbox runtime together with OpenClaw to run agents in isolated, kernel-level-isolated environments, primarily aimed at NVIDIA hardware (DGX Spark referenced repeatedly in official tutorials)
- Docs: docs.nvidia.com/nemoclaw/ (versioned, e.g. `0.0.16` seen in sources — this is an early-stage/low-version-number project)
- Companion project: **NVIDIA OpenShell** — "an open-source runtime for running autonomous AI agents in sandboxed environments with kernel-level isolation" `[OFFICIAL SOURCE: build.nvidia.com/spark/nemoclaw/overview]`

## Core Functionality
- `nemoclaw onboard` — interactive onboarding wizard that sets up an inference provider
- Wraps OpenClaw's agent runtime inside an OpenShell sandbox — the design goal is explicitly: **"all without exposing your host filesystem or network to the agent"** — a genuinely strong isolation claim if accurate
- Provides a browser-based chat dashboard once running (accessible via a dashboard URL) — NOT a bare terminal-only tool
- Official tutorial framing: "Run OpenClaw in an OpenShell sandbox on DGX Spark with Ollama (e.g. NVIDIA Nemotron 3 Super)" — i.e., the flagship use case is pairing NemoClaw with a **locally-hosted Nemotron model via Ollama**

## Local Inference Routing (deep — best-documented section found)
- All approaches route through the **same `inference.local` routing model**
- Critical architectural detail: **"The agent inside the sandbox never connects to your model server directly. OpenShell intercepts inference traffic and forwards it to the local endpoint you configure."** `[OFFICIAL SOURCE, high confidence — direct quote from docs.nvidia.com]` — this is a meaningfully different (and more locked-down) network model than every other tool in this research set, where the agent process itself typically dials out to whatever endpoint is configured.
- **Ollama**: default local inference option; onboard wizard auto-detects a running Ollama instance, and can start Ollama for you if it isn't running (on macOS, can also install Ollama via Homebrew if absent)
- **OpenAI-Compatible Server**: works with any server implementing `/v1/chat/completions` — vLLM, TensorRT-LLM, llama.cpp, LocalAI, "and others" are explicitly named as tested-compatible. Setup: run your server (example given: `vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000`), then `nemoclaw onboard`, choose "Other OpenAI-compatible endpoint," enter the base URL (e.g. `http://localhost:8000/v1`), and an API key (any non-empty string like `dummy` if the server doesn't require auth). **NemoClaw validates the endpoint with a live test request before continuing.**
- **Non-interactive/scripted setup** (relevant for automation/CI): environment variables `NEMOCLAW_PROVIDER=custom`, `NEMOCLAW_ENDPOINT_URL=http://localhost:8000/v1`, and `NEMOCLAW_MODEL` (optional Ollama model tag)
- Experimental options also mentioned for vLLM and NVIDIA NIM specifically

## Omni Router Compatibility — the clearest case in this entire research set
- **YES, with very high confidence.** NemoClaw's documented "OpenAI-Compatible Server" path is generic and explicitly validated by the tool itself: point `NEMOCLAW_ENDPOINT_URL` at `http://localhost:20128/v1`, and per the tool's own onboarding logic it should "just work" the same way it would for any other OpenAI-compatible server (vLLM/LocalAI/etc. are already confirmed working this way). This is `[INFERRED]` in the sense that Omni Router wasn't named directly, but it's the strongest and most mechanically specific inference of any tool researched here, because NemoClaw's endpoint-swap mechanism is fully documented end-to-end including the validation step.

## Security Model
- Sandbox isolation is the entire point of the product — "kernel-level isolation," no direct host filesystem/network exposure to the agent, traffic interception/forwarding pattern for inference calls
- This is architecturally the **safest** tool in the full 15-tool set researched here, assuming the sandbox claims hold up under independent verification (not independently audited in this pass — vendor claim from NVIDIA's own docs, reasonably credible given NVIDIA's stated OpenShell design, but still a vendor claim)

## Hermes / MCP Control Potential
- READ_ONLY: dashboard status, endpoint validation results
- CONTROLLED_WRITE: `nemoclaw onboard` reconfiguration, non-interactive env-var-driven setup (genuinely automation-friendly — one of the few tools in this set with clean, documented non-interactive/CI-style configuration)
- HIGH_RISK: none inherent — the sandbox model is specifically designed to minimize this category, which makes NemoClaw a strong **template** for how Hermes should sandbox its OWN delegated workers, not just a tool to control.
- Because it's an OpenClaw plugin rather than an independent product, treat this file alongside `10_OpenClaw.md` — NemoClaw's security posture is meaningfully better than bare OpenClaw's (bare OpenClaw's sandboxing is opt-in; NemoClaw's is the entire point of the product).

## Windows Notes
`[UNKNOWN]` — the DGX Spark/NVIDIA-hardware framing suggests a Linux-first tool; no Windows documentation was surfaced in this pass. Given OpenClaw itself has a native Windows installer, NemoClaw's Windows story should be checked directly before assuming parity.

## Evidence Sources
`[OFFICIAL SOURCE]` docs.nvidia.com/nemoclaw (Use a Local Inference Server page — directly fetched, high confidence, very specific and mechanically detailed), build.nvidia.com/spark/nemoclaw/overview. This is the single best-sourced file in the set (single authoritative vendor doc, not a patchwork of secondary community sources), but coverage is narrow — only the local-inference-routing feature was deeply documented in the sources retrieved; broader NemoClaw feature coverage (skills, hooks, memory, etc.) needs a follow-up pass against the full docs.nvidia.com/nemoclaw site.
