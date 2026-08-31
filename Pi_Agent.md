# Pi Agent

## 1. Identity

- **Official/project name:** Pi (also called "Pi Coding Agent" / "Pi Agent Harness"). `[OFFICIAL SOURCE]`
- **Name collision warning:** "Pi Agent" and "Pi" collide with many unrelated projects — PiDeck, pi-agent-desktop wrappers, `pi-agents` orchestration layers, an Inflection AI chatbot once called "Pi", and Raspberry Pi tooling. This document covers **only** the terminal coding-agent harness at `pi.dev`, maintained by Earendil Inc. and originally created by Mario Zechner (aka "badlogic", creator of libGDX). `[OFFICIAL SOURCE, GITHUB]`
- **Vendor/organization:** Earendil Inc. (Zechner joined as a major stakeholder and brought the project with him around April 2026, per community reporting). `[COMMUNITY, corroborated by 2 independent sources]`
- **Repository:** `https://github.com/earendil-works/pi` (monorepo; formerly `badlogic/pi-mono`, some doc/source links still reference the old `pi-mono` path). `[GITHUB]`
- **Official website/docs:** `https://pi.dev`, documentation at `https://pi.dev/docs/latest`. `[OFFICIAL SOURCE]`
- **Category:** Terminal-based, self-extensible AI coding agent CLI, distributed as a small monorepo of composable packages (agent runtime, unified LLM API, TUI library, coding-agent CLI). Not an IDE plugin, not a GUI product, not a managed cloud service. `[OFFICIAL SOURCE]`
- **License:** MIT. `[OFFICIAL SOURCE, GITHUB]`
- **Current/researched version:** Repo shows active development with 5,800+ commits; a mirrored release channel lists v0.84.1 as a recent build. Treat any specific version number as a snapshot — Pi ships frequently. `[GITHUB, COMMUNITY]`
- **Primary purpose:** A minimal terminal coding harness — deliberately small core (4 built-in tools + a short system prompt) that developers extend via TypeScript extensions, Agent Skills, prompt templates, themes, and shareable "Pi packages" rather than relying on built-in product features. `[OFFICIAL SOURCE]`
- **Target users:** Developers who want to shape their own agent harness instead of accepting a fixed, feature-heavy product; teams building custom coding-agent distributions (community example: `spences10/my-pi`, a curated Pi distribution with MCP, LSP, telemetry pre-wired). `[GITHUB, COMMUNITY]`
- **Platform support:** npm-installable (`@earendil-works/pi-coding-agent`) on any platform with Node.js; also has a POSIX shell installer (`pi.dev/install.sh`) and a PowerShell installer (`pi.dev/install.ps1`) for native Windows use; documented platform-setup pages exist for Windows, Termux (Android), and tmux. `[OFFICIAL SOURCE]`

## 2. Specialization

Pi's core specialty is being a **minimal, unopinionated coding-agent harness** rather than a full-featured coding-agent product. `[OFFICIAL SOURCE]`

Its own documentation and multiple independent community reviews describe a deliberate "what we didn't build" stance: Pi's design principles explicitly state that it does **not** ship built-in MCP support, sub-agents, permission popups, plan mode, to-do tracking, or background bash — these are left for the user to add via extensions or install as packages. `[OFFICIAL SOURCE, COMMUNITY — corroborated by 3 independent write-ups]`

What it is comparatively good at, per vendor and reviewer accounts:
- **Context efficiency / low token overhead** — an external benchmark cited by Earendil (Databricks' internal multi-million-line-codebase coding-agent benchmark) reportedly found Pi achieved the highest pass rate among harnesses tested on Opus 4.8 at high thinking effort, at lower cost, because it sent roughly 3x less context per turn. `[COMMUNITY, single-sourced via an Earendil-linked case-study post — treat as vendor-adjacent, not independently verified]`
- **Composability** — because the monorepo splits into `pi-ai` (unified multi-provider LLM API), `pi-agent-core` (agent loop/tool-calling runtime), `pi-coding-agent` (interactive CLI), and `pi-tui` (terminal UI library), the runtime can be embedded in other Node.js applications rather than used only as a CLI. `[OFFICIAL SOURCE, GITHUB]`
- **Deep extensibility surface** — an extremely detailed TypeScript extension API (lifecycle events, custom tools, custom UI, dynamic provider registration) that most competing minimal harnesses do not expose to this depth. `[OFFICIAL SOURCE]`

## 3. Core Functionalities

- **Code generation/editing** — native. Built-in tools are deliberately minimal: `read`, `write`, `edit`, `bash` (plus `powershell`, `grep`, `find`, `ls` per the extensions documentation's list of overridable built-ins). `[OFFICIAL SOURCE]`
- **Terminal/shell execution** — native, via the `bash`/`powershell` tools and the `!`/`!!` user-bash shortcuts (which can be intercepted or redirected, e.g. to SSH, via the `user_bash` extension event). `[OFFICIAL SOURCE]`
- **Planning / sub-agents / plan mode** — **not built in.** The vendor's own "Design principles" documentation states these are intentionally omitted; users build or install them via extensions/packages. `[OFFICIAL SOURCE, COMMUNITY]`
- **Autonomous execution** — native agent loop (`pi-agent-core`) handling tool calling and state management; supports auto-retry on transient provider errors and auto-compaction when context nears its limit. `[OFFICIAL SOURCE]`
- **File operations** — native (`read`/`write`/`edit`/`grep`/`find`/`ls`), each of which is independently overridable by an extension and supports pluggable "Operations" interfaces for remote execution (SSH, containers). `[OFFICIAL SOURCE]`
- **Memory / project context** — session-based, not persistent cross-session memory in the product sense. Context comes from `AGENTS.md`/`CLAUDE.md`/`AGENTS.override.md` files loaded regardless of project trust (unless disabled), plus whatever an extension injects. `[OFFICIAL SOURCE]`
- **Task delegation / background execution** — **not built in** as a first-class concept (no built-in sub-agents or background-bash); can be built via extensions (community example: Shopify's `pi-autoresearch`, an autonomous optimization-loop extension). `[COMMUNITY]`
- **Testing/debugging** — no dedicated built-in testing framework integration; relies on the `bash` tool plus whatever project tooling exists. `[INFERRED — no vendor documentation of a distinct testing subsystem was found]`
- **Session management** — native and unusually deep: sessions are stored as an append-only JSONL entry tree, support `/fork`, `/clone`, `/tree` navigation, branch summarization, manual and automatic **compaction**, and session renaming — all independently documented (`sessions.md`, `compaction.md`, `session-format.md`). `[OFFICIAL SOURCE]`
- **Workflow automation** — via **Agent Skills** (on-demand capability packages, Agent-Skills-standard-compliant), **Prompt Templates** (reusable prompts expanded from slash commands), **Themes**, and **Pi Packages** (bundles of the above, shareable via npm or git). `[OFFICIAL SOURCE]`
- **Custom UI** — extensions can register full custom TUI components (dialogs, widgets, status bar entries, footer/header content, custom editors) via `ctx.ui` and `@earendil-works/pi-tui`. `[OFFICIAL SOURCE]`

## 4. CLI / Operation Model

**Installation** `[OFFICIAL SOURCE]`:
```bash
# npm (any platform with Node.js)
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# macOS / Linux
curl -fsSL https://pi.dev/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://pi.dev/install.ps1 | iex"

# pnpm / bun equivalents also documented
```
Uninstall: `npm uninstall -g @earendil-works/pi-coding-agent` (or the matching `pnpm remove -g` / `yarn global remove` / `bun uninstall -g`).

**Main executable:** `pi`, run inside a project directory. First run prompts for authentication (`/login` for subscription providers, or an API-key environment variable such as `ANTHROPIC_API_KEY`). `[OFFICIAL SOURCE]`

**Four operating modes**, per the vendor's own summary: interactive (TUI), print/JSON (`--mode json` or `-p`), RPC (`--mode rpc`), and SDK (embed via `@earendil-works/pi-coding-agent`'s `AgentSession`/`createAgentSession` in a Node.js app). `[OFFICIAL SOURCE]`

**Interactive mode:** default TUI with slash commands (`/login`, `/logout`, `/model`, `/settings`, `/reload`, `/new`, `/resume`, `/fork`, `/clone`, `/tree`, `/compact`, `/name`, `/skill:<name>`, `/scoped-models`, etc.), keybindings (documented separately in `keybindings.md`), and `!`/`!!` inline shell execution. `[OFFICIAL SOURCE]`

**Non-interactive / headless modes:**
- `--mode json`: JSON event stream mode, print-mode style structured events (documented at `json.md`, not deeply researched in this pass — `[UNKNOWN, not fetched]`).
- `--mode rpc`: full JSON-over-stdin/stdout protocol for embedding Pi in other applications/IDEs (see Section 9 — APIs). `[OFFICIAL SOURCE]`

**Automation possibilities:** RPC mode explicitly targets external orchestration; `--extension`/`-e <path>` allows quick extension testing without installing to a discovery path; `--no-builtin-tools` starts Pi with zero built-in tools (extension tools only); `pi --list-models` and `--models`/`enabledModels` allow scoping the available model catalogue; `--session-dir`, `--no-session`, `--name`/`-n` control session persistence for scripted/CI use. `[OFFICIAL SOURCE]`

**Configuration files:**
- Global: `~/.pi/agent/settings.json`, `~/.pi/agent/extensions/`, `~/.pi/agent/skills/`, `~/.pi/agent/auth.json`, `~/.pi/agent/trust.json`, `~/.pi/agent/models-store.json` `[OFFICIAL SOURCE]`
- Project (loaded only after project trust is granted): `.pi/settings.json`, `.pi/extensions/`, `.pi/skills/`, `.pi/prompts/`, `.pi/themes/`, `.pi/SYSTEM.md`, `.pi/APPEND_SYSTEM.md` `[OFFICIAL SOURCE]`
- `.agents/skills/` (project, searched up to the git root) and `~/.agents/skills/` (global) are also honored, enabling skill sharing across different agent harnesses. `[OFFICIAL SOURCE]`
- `CONFIG_DIR_NAME` — Pi's own API exposes this constant instead of a hardcoded `.pi` string because "rebranded distributions can use a different config directory name," implying Pi is designed to be white-labeled/forked by downstream distributions. `[OFFICIAL SOURCE, INFERRED implication]`

**Environment variables:** a dedicated `environment-variables.md` reference page exists (not deeply fetched in this pass) covering Pi process configuration and session metadata exposed to bash tools (confirmed concretely for the `bash`/`powershell` tools: `PI_SESSION_ID`, `PI_SESSION_FILE`, `PI_PROVIDER`, `PI_MODEL`, `PI_REASONING_LEVEL`, toggleable via `exposeSessionEnvironment: false`). `[OFFICIAL SOURCE]`

**Logs/output:** sessions are the durable record — an append-only JSONL entry tree per session (`session-format.md`), exportable to HTML (`export_html` RPC command / presumably a matching CLI or slash command). No separate "debug log" file was found in this research pass. `[OFFICIAL SOURCE, partial — `[UNKNOWN]` for a dedicated debug/verbose logging flag]`

**Session/state handling:** extremely well documented — branching, forking, cloning, tree navigation, labels/bookmarks, manual/automatic compaction with custom summarizers, and a stable `SessionManager` API usable both from extensions and from the RPC client. `[OFFICIAL SOURCE]`

## 5. Architecture

```
pi (CLI) ──┬─► pi-coding-agent   (interactive CLI, session mgmt, modes: tui/json/rpc/print)
           ├─► pi-agent-core     (agent loop, tool calling, state management)
           ├─► pi-ai             (unified multi-provider LLM API: Anthropic/OpenAI/Google/…)
           ├─► pi-tui            (terminal UI library, differential rendering)
           └─► pi-telemetry      (vendor-neutral telemetry contracts + reference adapter)

Extension layer (TypeScript, jiti-loaded, no compile step)
  → subscribes to a documented lifecycle event stream
      (project_trust → session_start → resources_discover →
       before_agent_start → agent_start → turn loop
       [context → provider request/response → tool_call/tool_result] →
       agent_end → agent_settled)
  → can register: custom tools, custom providers, commands, shortcuts,
      CLI flags, message/entry renderers, markdown transformers, custom UI

Skill / Prompt-template / Theme / Package layer
  → Agent-Skills-standard-compliant SKILL.md packages, loaded on demand
  → Pi Packages (npm: or git: installable bundles of the above)

Configuration layer: global (~/.pi/agent/) + project (.pi/, gated by project trust)
Storage/memory layer: append-only JSONL session files, models-store.json cache, auth.json
Execution/sandbox layer: NONE — no built-in sandbox (see Section 11)
API/server layer: RPC mode (JSON-over-stdio) + SDK (in-process AgentSession)
Authentication layer: OAuth (subscriptions) + API-key + auth.json + provider extensions
```
`[OFFICIAL SOURCE, GITHUB — synthesized from the repo README and the extensions/RPC/security docs; the diagram itself is this document's construction, not copied from Pi's own docs]`

## 6. Models / Providers

Officially supported, via the unified `pi-ai` package `[OFFICIAL SOURCE]`:

- **Subscription (OAuth) providers**, via `/login`: OpenAI Codex (ChatGPT Plus/Pro), Claude Pro/Max (Anthropic — billed from "extra usage," not against normal Claude plan limits, per docs), GitHub Copilot, xAI (Grok/X subscription), OpenRouter (PKCE flow minting a user-controlled, non-expiring API key billed from OpenRouter credits), and "Radius" (a dynamic `pi-messages` gateway with its own OAuth flow).
- **API-key providers** (documented with exact env-var names and `auth.json` keys — 25+ entries): Anthropic, Ant Ling, Azure OpenAI Responses, OpenAI, DeepSeek, NVIDIA NIM, Google Gemini, Amazon Bedrock, Mistral, Groq, Cerebras, Cloudflare AI Gateway, Cloudflare Workers AI, xAI, OpenRouter, Vercel AI Gateway, ZAI Coding Plan (Global/China), OpenCode Zen/Go, Radius, Hugging Face, Fireworks, Together AI, Baseten, Kimi For Coding, MiniMax (+ China), Qwen Token Plan (3 variants), Xiaomi MiMo (+ regional variants).
- **Cloud providers with dedicated configuration docs:** Azure OpenAI, Amazon Bedrock (incl. AWS Profile/IAM keys/bearer token/ECS task roles/IRSA, and a Bedrock-proxy env-var set), Cloudflare AI Gateway (with 4 auth modes: Workers AI native, unified billing, stored BYOK, inline BYOK), Cloudflare Workers AI, Google Vertex AI (via Application Default Credentials or a service-account key file).
- **Local model support:** llama.cpp router server, managed via `/login llama.cpp` and `/llama`; custom Ollama/LM Studio/vLLM endpoints via `models.json` (any provider speaking OpenAI Completions, OpenAI Responses, Anthropic Messages, or Google Generative AI wire formats).
- **Custom/OpenAI-compatible endpoints:** natively supported — this is a first-class, explicitly documented use case (`custom-provider.md`, `models.md`), including a full extension API (`pi.registerProvider()`) for dynamic model discovery (`refreshModels`), custom OAuth flows, and per-provider header/baseUrl overrides. This directly answers the "can it be pointed at a local/self-hosted gateway" question: **yes, natively, with first-party support for `baseUrl` + `apiKey` overrides and dynamic model refresh** — highly relevant for routing through a gateway like Bifrost.
- **Credential resolution order:** CLI `--api-key` flag → `auth.json` entry → environment variable → custom provider keys from `models.json`. `auth.json` is written with `0600` permissions.
- **Key field supports:** shell-command execution (`!command`, cached for process lifetime — e.g. `!op read 'op://vault/item/credential'`), environment interpolation (`$ENV_VAR`, `${ENV_VAR}`), escapes (`$$`, `$!`), and literal values.

`[OFFICIAL SOURCE throughout this section]`

## 7. MCP

**Classification: Not supported natively — Extension/plugin-based only.** `[OFFICIAL SOURCE, cross-corroborated by 3 independent community sources]`

Pi's own documentation and homepage state plainly, under a "What we didn't build" / design-principles framing, that Pi does not ship MCP, sub-agents, permission popups, plan mode, to-dos, or background bash — these are left to extensions or installable packages. The homepage explicitly frames MCP as something users add: *"Build CLI tools with READMEs (see Skills), or build an extension that adds MCP support."* `[OFFICIAL SOURCE — pi.dev homepage]`

This is corroborated independently by three separate community reviews (`dev-ore.com`, `rushis.com`, `explainx.ai`), all of which quote or paraphrase the same "Design principles" section stating Pi does not include built-in MCP. `[COMMUNITY, cross-corroborated, 3 independent sources]`

- **Can it act as an MCP client?** Not natively; achievable by building or installing an extension. The vendor's blog post on the topic reportedly argues MCP servers are "often worse" than simpler primitives for many use cases — a stated design philosophy, not just an omission. `[COMMUNITY, single-sourced summary of a linked vendor blog post — the post itself was not independently fetched in this pass, `[UNKNOWN]` for exact wording/argument]`
- **Can it act as an MCP server?** No evidence found either way; not documented. `[UNKNOWN]`
- **Transports, config, discovery, invocation, auth, permissions:** N/A at the core-product level since MCP is not built in. Community distributions (e.g. `spences10/my-pi`, described as "Composable Pi coding agent with MCP, LSP, agent chains...") demonstrate that third-party MCP integration is achievable via Pi's extension system, but the specific mechanism (which MCP client library, which transport) was not verified from official Pi documentation in this pass. `[COMMUNITY — third-party extension exists; internals `[UNKNOWN]` without inspecting that project directly]`
- **Can Pi expose its own capabilities through MCP?** Not documented; would require a custom extension exposing an MCP server that wraps Pi's `registerTool`/RPC surface. `[INFERRED — architecturally plausible via RPC mode or the extension API, but not a documented/named feature]`
- **Can another master agent control Pi through MCP?** Not directly — but Pi's RPC mode (JSON-over-stdio, fully documented command/event protocol) is a natural, well-specified integration surface a master agent or an MCP-wrapping shim could drive without needing MCP specifically. See Section 9. `[OFFICIAL SOURCE for RPC mode itself; INFERRED for using it as an MCP-adjacent control surface]`
- **One caveat on source reliability:** a lower-quality aggregator blog (`makeronsite.com`) claims a `v0.7.x` "MCP protocol integrated" milestone in a version-history table. This directly contradicts the official docs and three independent community reviews described above. Given the official docs' explicit and repeated "no built-in MCP" framing (last verified against docs current as of this research pass, August 2026), this claim is treated as unreliable/likely inaccurate rather than merged into the "supported" classification. **Disagreement flagged, not silently resolved.** `[COMMUNITY, single low-corroboration source — CONFLICTS with OFFICIAL SOURCE; official source preferred]`

**Practical takeaway for MCP integration architecture:** treat Pi as "MCP-capable only through a purpose-built extension." Any MCP bridge (client or server) must be written as a Pi TypeScript extension using `pi.registerTool()` to expose remote MCP tools as native Pi tools, or built as an external process that drives Pi over RPC mode and separately speaks MCP on the other side.

## 8. Skills / Plugins / Extensions

Pi implements the **[Agent Skills standard](https://agentskills.io/specification)** — the same open specification used by other agent harnesses (compatible with Claude Code / Codex skill directories by pointing `settings.json`'s `skills` array at their folders). `[OFFICIAL SOURCE]`

**Skills:**
- A skill = a directory (or, in some locations, a standalone `.md` file) containing `SKILL.md` with YAML frontmatter (`name`, `description` required; `license`, `compatibility`, `metadata`, `allowed-tools`, `disable-model-invocation` optional) plus freeform scripts/references/assets.
- Discovery locations: `~/.pi/agent/skills/`, `~/.agents/skills/` (global); `.pi/skills/`, `.agents/skills/` (project, trust-gated); package-declared `skills/` dirs or `pi.skills` in `package.json`; `settings.json`'s `skills` array; CLI `--skill <path>` (repeatable).
- Invocation: the system prompt lists available skill descriptions (progressive disclosure); the model can `read` the full `SKILL.md` on its own, or a user can force it with `/skill:<name> [args]`. `enableSkillCommands` toggles this.
- Pi is explicitly **more lenient** than the Agent Skills standard on one point: it does not require a skill's declared `name` to match its parent directory name, specifically to support skill directories shared across multiple agent harnesses.
- Named skill repositories: Anthropic's official `anthropics/skills` repo, and a community `badlogic/pi-skills` repo (web search, browser automation, Google APIs, transcription).

**Extensions** (the deeper, code-level customization layer — see Section 3/9 for API depth): TypeScript modules, loaded via `jiti` (no compile step needed), auto-discovered from `~/.pi/agent/extensions/` (global) or `.pi/extensions/` (project, trust-gated), or loaded ad hoc with `-e <path>`. Extensions can register custom tools, commands, keyboard shortcuts, CLI flags, message/entry renderers, markdown transformers, full custom UI, and can override any built-in tool (`read`, `bash`, `powershell`, `edit`, `write`, `grep`, `find`, `ls`). `[OFFICIAL SOURCE]`

**Prompt Templates:** reusable prompts expanded from slash commands (`prompt-templates.md`, not deeply fetched — `[UNKNOWN]` for exact file format beyond what's inferable from the `get_commands` RPC output showing `source: "prompt"`).

**Themes:** built-in and custom terminal themes (`themes.md`, not deeply fetched — `[UNKNOWN]` for format details).

**Pi Packages:** the sharing/bundling mechanism — a package can bundle extensions, skills, prompts, and themes together and be installed via `pi install npm:<pkg>` or `pi install git:<repo>@<ref>`, declared in `settings.json`'s `packages` array. Runtime dependencies must be listed in `dependencies` (not `devDependencies`) because package installs use `npm install --omit=dev` by default. `[OFFICIAL SOURCE]`

**Distinguishing built-in vs. official vs. third-party vs. custom:** built-in tools/skills ship with the harness itself (documented, small set); "official" extensions/skills would be anything published under `earendil-works` or `badlogic` (e.g. `badlogic/pi-skills`, `badlogic/pi-share-hf`); everything else (e.g. `spences10/my-pi`, Shopify's `pi-autoresearch`, community MCP/LSP bridges) is third-party/community, installed explicitly by the user via `pi install`. `[GITHUB, COMMUNITY]`

## 9. APIs / Integration Surfaces

- **CLI** — the primary surface; four modes as described in Section 4. `[OFFICIAL SOURCE]`
- **RPC (JSON-over-stdin/stdout)** — the most complete external-control surface, extensively documented (`rpc.md`):
  - Strict JSONL framing (LF-only; explicitly warns that Node's `readline` is non-compliant because it also splits on U+2028/U+2029).
  - Commands: `prompt`, `steer`, `follow_up`, `abort`, `clear_queue`, `new_session`, `get_state`, `get_messages`, `set_model`, `cycle_model`, `get_available_models`, `set_thinking_level`, `cycle_thinking_level`, `get_available_thinking_levels`, `set_steering_mode`, `set_follow_up_mode`, `compact`, `set_auto_compaction`, `set_auto_retry`, `abort_retry`, `bash`, `abort_bash`, `get_session_stats`, `export_html`, `switch_session`, `fork`, `clone`, `get_fork_messages`, `get_entries` (cursor-based via `since`), `get_tree`, `get_last_assistant_text`, `set_session_name`, `get_commands`.
  - Events streamed on stdout: `agent_start/_end/_settled`, `turn_start/_end`, `message_start/_update/_end`, `bash_execution_update`, `tool_execution_start/_update/_end`, `queue_update`, `compaction_start/_end`, `auto_retry_start/_end`, summarization-retry events, `extension_error`.
  - **Extension UI protocol over RPC:** dialog methods (`select`, `confirm`, `input`, `editor`) become request/response pairs (`extension_ui_request`/`extension_ui_response`) with optional timeouts; fire-and-forget methods (`notify`, `setStatus`, `setWidget`, `setTitle`, `set_editor_text`) are one-way.
  - This makes RPC mode Pi's de facto "headless control API" — well-suited as the integration point for an external orchestrator (see Section 15).
- **SDK** — `AgentSession`/`createAgentSession` from `@earendil-works/pi-coding-agent`, for embedding the agent runtime directly inside a Node.js/TypeScript application instead of spawning a subprocess. Vendor explicitly recommends this over RPC for Node.js consumers. `[OFFICIAL SOURCE]`
- **JSON event stream mode** (`--mode json` / `-p`) — a simpler print-mode variant with structured events; not deeply researched in this pass. `[UNKNOWN — page not fetched]`
- **TUI component library** (`@earendil-works/pi-tui`) — usable by extensions to build custom terminal UI; also documented as its own reference (`tui.md`, not fetched). `[UNKNOWN — page not fetched]`
- **Provider/model extension API** — `pi.registerProvider()` / `pi.unregisterProvider()`, capable of registering full custom `Provider` objects (native auth flows including OAuth, `refreshModels` for dynamic catalogs, `streamSimple` for non-standard streaming APIs). This is effectively a plugin surface for arbitrary LLM backends. `[OFFICIAL SOURCE]`
- **GitHub/CI integration** — a documented community GitHub Action (`shaftoe/pi-coding-agent-action`) runs Pi as a CI/CD step against GitHub, Codeberg, or self-hosted Forgejo, "inspired by OpenCode's GitHub action." Not an official Earendil product, but explicitly designed around Pi's existing CLI/skills/extensions/AGENTS.md workflow. `[GITHUB, COMMUNITY]`
- **IDE integrations** — none found as an official product; Pi is explicitly *not* an IDE extension by design. `[OFFICIAL SOURCE — by omission/explicit positioning]`
- **A2A / ACP** — no evidence of native support found. `[UNKNOWN]`

## 10. Authentication

- **Subscription/OAuth login:** `/login` (interactive) walks through provider-specific OAuth/PKCE flows for OpenAI Codex, Claude Pro/Max, GitHub Copilot, xAI, OpenRouter, and Radius. `/logout` clears credentials. Tokens auto-refresh and are stored in `~/.pi/agent/auth.json`. `[OFFICIAL SOURCE]`
- **API keys:** via environment variable (provider-specific name, e.g. `ANTHROPIC_API_KEY`) or stored in `auth.json` (0600 permissions) under a provider-specific key (e.g. `"anthropic"`). A large, explicit env-var/`auth.json`-key mapping table is documented for 25+ providers (see Section 6). `[OFFICIAL SOURCE]`
- **Credential resolution order:** CLI `--api-key` flag → `auth.json` → environment variable → `models.json`-declared custom provider keys. `[OFFICIAL SOURCE]`
- **Key field syntax:** supports shell-command execution (`!command`, for pulling from a secrets manager like 1Password: `!op read 'op://vault/item/credential'`), environment interpolation (`$VAR`/`${VAR}`), and literal escaping (`$$`, `$!`). `[OFFICIAL SOURCE]`
- **Cloud-provider-specific auth:** Azure OpenAI (API key + base URL/resource name), Amazon Bedrock (`/login amazon-bedrock`, AWS Profile, IAM keys, bearer token, ECS task roles, IRSA), Cloudflare AI Gateway/Workers AI (API key + account/gateway IDs, 4 upstream-auth modes), Google Vertex AI (Application Default Credentials or a service-account key file). `[OFFICIAL SOURCE]`
- **Custom provider OAuth:** extensions can register a fully custom OAuth flow via `pi.registerProvider()`'s `oauth` config (`login`, `refreshToken`, `getApiKey` callbacks), which then appears in the `/login` menu — e.g. for a corporate SSO-backed AI gateway. `[OFFICIAL SOURCE]`
- **Credential storage location (not values):** `~/.pi/agent/auth.json`, `0600` permissions, JSON keyed by provider id. Never reproduce actual key values (none observed in this research; docs consistently redact with `...`). `[OFFICIAL SOURCE]`
- **Project trust as a quasi-auth gate:** project-local settings/extensions/skills only load after the user grants "project trust" (see Section 11) — this gates *configuration and code loading*, not model/provider credentials, but it's the closest thing Pi has to a permission system. `[OFFICIAL SOURCE]`

## 11. Security / Permissions

- **No built-in permission system.** The repository README states plainly: *"Pi does not include a built-in permission system for restricting filesystem, process, network, or credential access. By default, it runs with the permissions of the user and process that launched it."* `[OFFICIAL SOURCE — GitHub README]`
- **No built-in sandbox**, and the vendor is explicit that this is intentional, not an oversight: *"A partial in-process sandbox would be easy to misunderstand as a security boundary while still depending on the host shell, filesystem, package managers, credentials, and extension code. Real isolation needs to come from the operating system or a virtualization/container boundary."* `[OFFICIAL SOURCE — security.md]`
- **Project Trust** is a distinct, narrower concept from sandboxing: it only gates whether Pi *loads* project-local settings/extensions/skills/prompts/themes/system-prompt files (`.pi/*`, `.agents/skills`) — it does **not** restrict what the model can ask tools to do once a session is running. Trust decisions are stored per-directory in `~/.pi/agent/trust.json`; default behavior is controlled by `defaultProjectTrust` (default `"ask"`); `--approve`/`-a` and `--no-approve`/`-na` override trust for a single run. Context files (`AGENTS.md`, `CLAUDE.md`, `AGENTS.override.md`) load regardless of trust unless context loading is disabled. `[OFFICIAL SOURCE]`
- **Prompt injection** is explicitly named as an accepted, unmitigated local-agent risk: *"Prompt injection from repository files, comments, documentation, context files, or build output is expected local-agent risk and cannot be reliably prevented by pi."* `[OFFICIAL SOURCE]`
- **Extensions run with full permissions** — the docs warn: *"Extensions run with your full system permissions and can execute arbitrary code. Only install from sources you trust."* Same warning is repeated for skills, which "can instruct the model to perform any action and may include executable code the model invokes." `[OFFICIAL SOURCE]`
- **Recommended isolation patterns** (all external to Pi's own core, documented in `containerization.md`): (1) **Gondolin extension** — keep `pi` and provider auth on the host but route built-in tools and `!` commands into a local Linux micro-VM; (2) **Plain Docker** — run the whole `pi` process in a container; (3) **OpenShell** — run the whole `pi` process in a policy-controlled sandbox. Guidance also covers avoiding mounting host `~/.pi/agent` into a container (to keep host sessions/credentials out of the sandbox) and preferring read-only workspace mounts to prevent unintended writes back to the host. `[OFFICIAL SOURCE]`
- **Supply-chain hardening** (documented in the README, unusually detailed for this class of tool): pinned exact versions for direct npm dependencies, `.npmrc` with `save-exact=true` and `min-release-age=2`, lockfile-change protection (`PI_ALLOW_LOCKFILE_CHANGE=1` required to intentionally modify), `npm run check` verification of pinned deps and a generated coding-agent shrinkwrap, `--ignore-scripts` used for installs and self-updates, CI running `npm audit --omit=dev` and `npm audit signatures --omit=dev`, and an explicit allowlist gating any new dependency lifecycle script. `[OFFICIAL SOURCE — GitHub README]`
- **Vulnerability reporting:** via the repo's `SECURITY.md`; the docs explicitly scope out "expected local-agent behavior, lack of a built-in sandbox, prompt injection from untrusted content, and behavior of user-installed extensions/skills" from what counts as a reportable security issue, unless a report demonstrates "a real privilege-boundary bypass" or unauthorized access beyond what the local user already had. `[OFFICIAL SOURCE]`

**HIGH_RISK summary:** unrestricted shell/process/filesystem/network access is the *default* operating mode, not an edge case — this tool is architecturally closer to "give the agent your shell" than to sandboxed coding agents that ship default-on permission prompts.

## 12. Logs / Errors / Observability

- **Session files** (append-only JSONL, one entry per event) are the primary durable record of everything that happened in a run — messages, tool calls/results, compactions, forks, labels. Exportable to HTML via `export_html`. `[OFFICIAL SOURCE]`
- **RPC-mode structured events** (Section 9) give fine-grained, real-time observability into agent/turn/tool/compaction/retry lifecycle for any embedding application. `[OFFICIAL SOURCE]`
- **`extension_error` event** — surfaces uncaught extension exceptions with the extension path and the event that triggered it. `[OFFICIAL SOURCE]`
- **`get_session_stats`** (RPC) — token usage (input/output/cache read/write), cost, tool-call counts, and live context-window usage percentage. `[OFFICIAL SOURCE]`
- **Telemetry package** — `@earendil-works/pi-telemetry` exists in the monorepo as "vendor-neutral telemetry contracts, reference adapter, conformance tests, and typed schemas," implying a pluggable telemetry/observability layer, but this document did not fetch its dedicated documentation. `[GITHUB — package exists; internals `[UNKNOWN]`]`
- **Debug/verbose CLI flags, exit codes, health/status endpoints:** not confirmed in this research pass — a dedicated logs/observability doc page was not found in the navigation fetched. `[UNKNOWN]`
- **No invented error-code taxonomy** — none was found in official docs, so none is reported here.

## 13. Limitations

- **No built-in MCP, sub-agents, plan mode, permission prompts, to-do tracking, or background bash** — all must be added via extensions/packages. This is Pi's single most load-bearing limitation for anyone expecting Claude-Code/Codex-style batteries-included behavior. `[OFFICIAL SOURCE, cross-corroborated]`
- **No built-in sandbox / no built-in permission system** — full local-user privileges by default (see Section 11). `[OFFICIAL SOURCE]`
- **Prompt-injection risk is explicitly unmitigated** by the tool itself. `[OFFICIAL SOURCE]`
- **Global `pi` CLI not installed by the desktop app** — a related community desktop wrapper (`abcwyc/pi-agent-desktop`) notes installing "Pi Agent" (the desktop app) does **not** install a global `pi` command; the CLI must be installed separately. This is a distinct, unofficial companion project, not Earendil's own product, so treat this specific limitation as scoped to that wrapper, not to Pi core. `[GITHUB — third-party project, not Earendil-official]`
- **Model-dependent dynamic tool loading** — the "deferred tool loading" optimization (large tool catalogs without prompt-prefix invalidation) only has native support on specific model families: Anthropic Sonnet/Opus/Fable ≥4.5 (excluding Haiku) and OpenAI `gpt-5.4`+; all other models fall back to sending the full active tool list on every request, which can invalidate provider prompt caching. `[OFFICIAL SOURCE]`
- **Windows support exists but is a documented "platform setup" concern**, not the primary/default target of the *nix-first installer/tooling ecosystem — a dedicated `windows.md` page exists, implying non-trivial platform-specific caveats, but this document did not fetch it in this pass. `[OFFICIAL SOURCE — page exists; specific caveats `[UNKNOWN]` without fetching windows.md]`
- **Output truncation is mandatory but tool-author-enforced, not automatic for custom tools** — the built-in limit is 50KB / 2000 lines for built-in tools; custom tools must explicitly opt into the same truncation utilities or risk overflowing model context. `[OFFICIAL SOURCE]`
- **Experimental features:** `allowed-tools` in skill frontmatter is explicitly marked experimental. `[OFFICIAL SOURCE]`
- **Single-vendor governance risk:** Pi is developed by one company (Earendil Inc.), a relatively young entity in this space (Zechner/Pi joining Earendil reported as recent, ~April 2026); this is a normal open-source-project governance consideration, not a documented technical limitation. `[COMMUNITY]`

## 14. Control Potential

- **READ_ONLY** — via RPC: `get_state`, `get_messages`, `get_available_models`, `get_available_thinking_levels`, `get_session_stats`, `get_entries`/`get_tree` (session inspection, cursor-paginated), `get_fork_messages`, `get_last_assistant_text`, `get_commands`. `[OFFICIAL SOURCE]`
- **CONTROLLED_WRITE** — via RPC/SDK/extensions: `prompt`/`steer`/`follow_up` (queue work with defined delivery semantics), `set_model`/`cycle_model`, `set_thinking_level`, `set_steering_mode`/`set_follow_up_mode`, `compact`/`set_auto_compaction`, `set_auto_retry`/`abort_retry`, `new_session`/`switch_session`/`fork`/`clone` (all cancellable by extension hooks), `set_session_name`, `export_html`; at the extension-API level: `pi.registerTool()`, `pi.registerProvider()`/`unregisterProvider()`, `pi.setActiveTools()`, `pi.setModel()`, `pi.setThinkingLevel()` — all scoped, inspectable, reversible actions. `[OFFICIAL SOURCE]`
- **HIGH_RISK** — the `bash` RPC command and the `bash`/`powershell` built-in tools execute arbitrary shell commands with full user-process privileges and no sandbox; `abort`/`abort_bash` can stop but not prevent execution; any registered extension is equivalently HIGH_RISK because it "can execute arbitrary code" with "your full system permissions" (vendor's own words); overriding built-in tools (`read`/`write`/`edit`/`bash`/etc.) from an extension is likewise unrestricted. `[OFFICIAL SOURCE — vendor explicitly names extensions and bash as full-permission surfaces]`

**Evidence for classification:** drawn directly from the RPC command/event reference (Section 9) and the Security page's explicit "no built-in permission system" / "extensions run with full permissions" statements (Section 11).

## 15. Integration With Other AI Systems

- **Hermes / Jarvis / Omni Router (Mudassir's ecosystem):** `NOT VERIFIED`. No public documentation ties Pi to these specific systems. Architecturally, the most direct integration path is Pi's **RPC mode** (Section 9) — a well-specified JSON-over-stdio protocol that an external orchestrator (Hermes/Omni Router) could drive as a subprocess without needing MCP, since Pi has no native MCP client/server. A secondary path is embedding `AgentSession` via the SDK directly inside a Node.js-based orchestrator layer. Both are `INDIRECTLY POSSIBLE` — they require building the bridge yourself; nothing off-the-shelf connects Pi to a named orchestrator today. `[INFERRED, based on documented RPC/SDK capability — no named integration exists]`
- **OpenCode / Codex / Claude Code / other coding-agent CLIs:** `INDIRECTLY POSSIBLE` at the skill-sharing level — Pi documents explicit compatibility with Claude Code's and Codex's skill directories (point `settings.json`'s `skills` array at `~/.claude/skills` or `~/.codex/skills`). No deeper (tool-level or session-level) interop with those specific products is documented. `[OFFICIAL SOURCE for skill-directory interop; NOT VERIFIED beyond that]`
- **OpenClaw:** named in Pi's own homepage copy as "a real-world integration" example (*"See OpenClaw for a real-world integration"*), but the mechanism (extension, wrapper, or something else) was not independently verified in this pass. `[OFFICIAL SOURCE that the integration exists; mechanism `[UNKNOWN]`]`
- **MCP Generator (a hypothetical future system, per the research standard's own framing):** `REQUIRES ADDITIONAL TOOL`. Since Pi has no native MCP surface, any MCP Generator targeting Pi would need to generate a Pi **extension** (using `pi.registerTool()` to wrap remote MCP tool calls) rather than a native MCP config file. `[INFERRED from Sections 7 and 9]`
- **GitHub Actions / CI systems:** `INDIRECTLY POSSIBLE` today via the third-party `shaftoe/pi-coding-agent-action`, which is explicitly modeled on OpenCode's GitHub Action and reuses Pi's existing CLI/skills/extensions/AGENTS.md conventions inside CI. Not an Earendil-official product. `[GITHUB, COMMUNITY]`
- **Community MCP+LSP distributions** (e.g. `spences10/my-pi`) prove third-party MCP bridging is *achievable*, but that specific project's internals were not inspected in this research pass, so its integration pattern is not documented here beyond "it exists and claims MCP support." `[GITHUB — existence only, `[UNKNOWN]` internals]`

## 16. MVP Relevance

**Strongest MVP use cases for the Jarvis/Hermes ecosystem, based on what's actually documented:**

- **Headless coding-agent worker controlled over RPC.** Pi's RPC protocol is thorough enough (structured commands + streamed events + cancellable session-lifecycle hooks) to drive as a subprocess from an orchestrator without needing to fork or patch Pi itself. This is the lowest-friction integration point.
- **Reuse `pi-ai` as a standalone unified LLM API** if the goal is simply "one client library, many providers" rather than a full coding-agent — it's a separately importable package (`@earendil-works/pi-ai`) with the widest documented provider/model coverage seen in this research pass (25+ API-key providers, 6 OAuth-subscription providers, 5 cloud-provider integrations, llama.cpp, and arbitrary OpenAI/Anthropic/Google-compatible custom endpoints).
- **Reuse the extension system for bounded, auditable tool delegation** — `pi.registerTool()` plus `pi.setActiveTools()`'s dynamic/additive tool-loading model is a clean, already-solved pattern for "give the agent a small tool surface now, expand it on demand" (the documented "search_tools" loader pattern), which is directly relevant to any future MCP-Generator-style capability-injection design.
- **What should be reused:** the provider abstraction (`pi-ai`), the RPC control protocol as a reference design for "how to expose a local agent to an external controller," and the Agent-Skills-standard skill format (already interoperable with Claude Code/Codex skill directories — meaning skills built for this ecosystem's other tools could be pointed at Pi with zero conversion).
- **What should NOT be depended on:** any assumption of built-in MCP, sandboxing, or permission gating — those must be built independently regardless of whether Pi is adopted, since Pi provides none of them natively. Also do not depend on a specific version number or on the `badlogic/pi-mono` repo path remaining canonical — the project has already moved once to `earendil-works/pi` and version numbers move quickly (5,800+ commits, weekly-cadence community "2026 guide" articles).
- **Useful automation surface not yet explored in this pass:** `pi install npm:<pkg>` / `pi install git:<repo>` packaging could let this ecosystem ship a pre-configured "Jarvis-flavored Pi distribution" (bundled extensions + skills + system prompt) the way `spences10/my-pi` does, rather than requiring end-users to hand-configure Pi.

This is a capability assessment, not an implementation plan — no MVP architecture is proposed here per the research standard's scope boundary.

## 17. Evidence / Sources

**Official sources:**
- `https://pi.dev` (homepage/design-principles framing) — `[OFFICIAL SOURCE]`
- `https://pi.dev/docs/latest` (documentation index) — `[OFFICIAL SOURCE]`
- `https://pi.dev/docs/latest/extensions` — `[OFFICIAL SOURCE]`
- `https://pi.dev/docs/latest/security` — `[OFFICIAL SOURCE]`
- `https://pi.dev/docs/latest/rpc` — `[OFFICIAL SOURCE]`
- `https://pi.dev/docs/latest/providers` — `[OFFICIAL SOURCE]`
- `https://pi.dev/docs/latest/skills` — `[OFFICIAL SOURCE]`

**GitHub:**
- `https://github.com/earendil-works/pi` (main monorepo README, permissions/containerization note, supply-chain hardening section) — `[GITHUB]`
- `https://github.com/shaftoe/pi-coding-agent-action` — `[GITHUB]`
- `https://github.com/abcwyc/pi-agent-desktop` — `[GITHUB]` (third-party desktop wrapper, not Earendil-official)
- `https://github.com/spences10/my-pi` — `[GITHUB]` (third-party MCP/LSP-enabled distribution)

**Community (cross-checked, multiple independent sources for the MCP/design-philosophy claim):**
- `https://www.rushis.com/pi-the-coding-agent-built-around-what-it-wont-do/`
- `https://www.dev-ore.com/blog/pi-dev-terminal-coding-harness/`
- `https://explainx.ai/blog/pi-minimal-agent-harness-mario-zechner-guide-2026`
- `https://silenceper.com/en/article/2026-05-27-pi-coding-agent-harness/`
- `https://roman.pt/posts/pi-dev-version/`
- `https://docs.bswen.com/blog/2026-08-10-pi-coding-agent-tutorial-2026/`
- `https://aisoftwaresystems.com/blog/what-is-pi-agent/` (identity/creator confirmation)

**Community, single-sourced / lower confidence (flagged inline where used):**
- `https://makeronsite.com/blog/2026/08/065-pi-coding-agent-2026-guide-en/` — contains a version-history claim ("MCP protocol integrated" at v0.7.x) that **conflicts** with official docs and is treated as unreliable (see Section 7).

**Not independently fetched in this pass (named in docs nav but out of scope for this research budget) — flagged as `[UNKNOWN]` wherever referenced above:** `quickstart.md`, `usage.md`, `containerization.md` (partially covered via search snippets only), `settings.md`, `keybindings.md`, `sessions.md`, `compaction.md`, `prompt-templates.md`, `themes.md`, `packages.md`, `models.md`, `custom-provider.md`, `session-format.md`, `sdk.md`, `json.md`, `tui.md`, `environment-variables.md`, `windows.md`, `termux.md`, `tmux.md`, `terminal-setup.md`, `shell-aliases.md`, `development.md`, `llama-cpp.md`.

**Research method note:** documentation-based research pass, current as of August 30, 2026. Pi ships frequently (5,800+ commits on a young, actively-developed monorepo that recently moved from `badlogic/pi-mono` to `earendil-works/pi`); treat specific version numbers, exact provider lists, and any MCP-related claim as subject to drift — re-verify against `https://pi.dev/docs/latest` before depending on specifics for integration work.
