# Awesome Agentic Infra [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Infrastructure that autonomous AI agents use to act in the world: an email address, a browser, memory, a wallet, a sandbox. Every entry is built for agents, not adapted from a tool made for humans.

Each entry says what the tool does, how you get access, where it falls short, and what setup costs an agent: whether a card is needed and whether a person has to do something once or every time. Only tools that someone has used or read in depth are listed.

**To add a tool:**

1. Read [CONTRIBUTING.md](CONTRIBUTING.md): criteria, entry format, what is not accepted.
2. Add one line at its alphabetical position in the right category:

   ```
   - [Name](https://example.com) - What it does. Pricing model. Limitation or caveat. Setup: no card, human once (verify email code).
   ```

3. Run `pnpm install && pnpm typography:fix`, then open a pull request. The template has the checklist; the CI checks format, order, typography and links.

No time for a pull request? [Suggest a tool](https://github.com/rogulia/awesome-agentic-infra/issues/new?template=suggest-a-tool.md) with an issue instead.

Pull requests that skip the checklist are closed.

A tool belongs here when it meets all of these:

- **Agent-native.** Resources are created through an API or SDK. After a one-time human step at the start (for example signing up and copying an API key), no interactive login, CAPTCHA or manual step is needed to create or use a resource. Say which human step in the `Setup:` sentence.
- **Alive.** Public product or repository with activity in the last 12 months.
- **Accessible.** Public documentation and a free tier, trial or open-source release.
- **Infrastructure.** Not an agent, not an orchestration framework, not a thin wrapper over an LLM API.

## Contents

- [Identity and Communication](#identity-and-communication)
- [Web Access](#web-access)
- [Payments](#payments)
- [Memory](#memory)
- [Execution and Sandboxes](#execution-and-sandboxes)
- [Observability and Evals](#observability-and-evals)
- [Security and Guardrails](#security-and-guardrails)
- [Authentication and Secrets](#authentication-and-secrets)
- [Data and Retrieval](#data-and-retrieval)
- [Protocols](#protocols)

## Identity and Communication

Email, phone and meeting presence for agents that need their own address.

- [AgentCall](https://agentcall.dev/) - Lets an agent join Google Meet, Zoom or Teams calls to listen, transcribe, speak and chat. Free trial, then pay-as-you-go. Supports only those three platforms and English transcription. Setup: no card, human once (sign up in dashboard).
- [AgentMail](https://www.agentmail.to/) - Programmatic inboxes with threads, webhooks and semantic search over mail. Free tier, with custom domains on paid plans. Built for receiving codes and holding conversations, and the free tier caps sending at 100 emails per day. Setup: no card, human once (verify email OTP code).
- [AgentPhone](https://agentphone.ai/) - Phone number for an agent with voice and SMS delivered to one webhook. No free tier, only a one-time credit. Numbers are US and Canada only. Setup: card not stated, human step not stated.
- [Inkbox](https://www.inkbox.ai/) - Agent identity with email inbox, iMessage, optional phone number and a public URL; the agent can sign itself up by API. Free plan, with phone and SMS on paid plans. Until a human verifies by email code, the agent can email only its owner. Setup: card not stated, human once (verify email 6-digit code).
- [MailSlurp](https://www.mailslurp.com/) - Email API that creates inboxes on demand for testing and automation. Free plan. A testing tool, not agent-specific, and the free plan has no custom domains. Setup: card not stated, human step not stated.
- [Resend Inboxes](https://resend.com/products/inboxes) - Inboxes that send and receive on your domain, managed through an API, CLI or MCP server, with a built-in triage agent. Free tier with 3 inboxes, then $1 per extra inbox. Announced 22 October 2026; the built-in agent only drafts replies and never sends them. Setup: no card, human once (create a Resend account and API key).

## Web Access

Browsers, search and scraping built for agents.

- [Browserbase](https://www.browserbase.com) - Cloud headless browsers via API, plus Search and Fetch endpoints. Free plan. The free plan has no captcha solving or stealth mode. Setup: card not stated, human once (sign up in dashboard).
- [Browserless](https://www.browserless.io) - Hosted headless Chrome, WebKit and Firefox over WebSocket and REST. Free plan. Billed in units, and a captcha solve costs 10 units. Setup: card not stated, human once (sign up in dashboard).
- [Cloudflare Browser Rendering](https://developers.cloudflare.com/browser-rendering/) - Headless browser sessions and REST endpoints running on Cloudflare Workers. Free plan with a daily browser-time cap. Extra concurrent browsers are billed separately. Setup: card not stated, human once (create account and API token).
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Open-source crawler (Apache-2.0) that turns pages into Markdown or structured JSON, with a hosted cloud. Free to self-host. The cloud SERP API is in beta. Setup: no card, no human step.
- [Exa](https://exa.ai) - Search API with content retrieval for AI applications. Free monthly credits. Rate limits are not published. Setup: no card, human once (sign up in dashboard).
- [Firecrawl](https://www.firecrawl.dev) - API that scrapes, crawls, maps and searches the web and returns Markdown or JSON. Free plan. A page that returns 403 or 404 still costs a credit. Setup: no card, human once (authorize in browser).
- [Hyperbrowser](https://www.hyperbrowser.ai) - Cloud browsers, sandboxes and web APIs for agents. Free plan. Free plans cannot buy top-ups, so you upgrade when credits run out. Setup: card not stated, human once (sign up in dashboard).
- [Jina Reader](https://jina.ai/reader/) - Turns a URL into Markdown when you prefix it with r.jina.ai, and returns search results through s.jina.ai. Free tokens with an API key. It does not bypass anti-bot systems or log in, and search needs a key. Setup: card not stated, human once (get API key on site).
- [Kernel](https://www.kernel.sh) - Managed browsers with live view, stealth mode, browser pools and managed auth connections. Free plan with monthly credits. The free plan has no configurable proxies or regional browsers. Setup: card not stated, human once (give agent email code).
- [Parallel](https://parallel.ai) - Web Search and Extract APIs returning ranked URLs and page excerpts. Free monthly requests. Live extraction takes 60-90 seconds against 1-3 seconds for cached pages. Setup: card not stated, human once (sign up, create API key).
- [Steel](https://steel.dev) - Browser sessions API with a self-hostable open-source Steel Browser (Apache-2.0). Free plan with one-time credits. The stealth browser is Enterprise-only. Setup: no card, human once (sign up in dashboard).
- [Tavily](https://www.tavily.com) - Search, extract and crawl API built for LLM applications. Free plan. Per-operation credit costs and rate limits are not published. Setup: no card, human once (sign up in dashboard).

## Payments

Wallets and payment rails that an agent can operate within limits.

- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - Open-source toolkit that gives an agent a crypto wallet and onchain actions, with CDP, Privy or Viem as wallet providers. Free to use. It does not enforce spend caps or destination allowlists, and the README warns that prompt injection can trigger transfers. Setup: card not stated, human once (create CDP Secret API key in portal).
- [Coinbase CDP x402 Facilitator](https://docs.cdp.coinbase.com/x402/core-concepts/facilitator) - Hosted service that verifies and settles x402 stablecoin payments for sellers. Free monthly transaction allowance, then a per-transaction fee. Solana supports only the `exact` and `upto` schemes. Setup: card not stated, human once (create CDP API key in portal).
- [Crossmint](https://www.crossmint.com/solutions/ai-agents) - Wallet API for agents with API-created wallets and a Policy Engine. Free monthly wallet allowance. Agentic Cards pricing is not published, and card use needs sales-gated access. Setup: card not stated, human once (sign up in console, create API key).
- [Nevermined](https://nevermined.ai/pricing) - Payment layer where agents buy services within spend mandates and sellers charge per call, via MCP server, SDK or API. Free tier for one developer, and sellers pay a settlement fee. The free tier is single-user. Setup: card not stated, human once (sign up in dashboard, get API key).
- [Privy](https://www.privy.io/) - Wallet infrastructure with an API, also usable as an AgentKit wallet provider. Free for small user counts. Signup is through a dashboard, and no separate agent pricing is published. Setup: card not stated, human once (sign up in dashboard, copy app secret).

## Memory

Persistent state and long-term memory for agents.

- [Basic Memory](https://github.com/basicmachines-co/basic-memory) - Stores agent memory as Markdown files with a local SQLite index and MCP access. Open source (AGPL-3.0) with an optional paid cloud. Syncing across devices is manual unless you use the cloud. Setup: no card, no human step.
- [Cognee](https://www.cognee.ai) - Memory engine for agents, open source (Apache-2.0) and also hosted. Free hosted tier. Data-source integrations and code indexing are not in Free. Setup: no card, human once (sign up in platform dashboard).
- [Hindsight](https://hindsight.vectorize.io) - Long-term memory service with retain, recall and reflect operations on PostgreSQL with pgvector. Open source (MIT) with a hosted cloud. Hosted rates are not published, and the benchmark numbers are the vendor’s own. Setup: no card, no human step.
- [Mem0](https://mem0.ai) - Memory layer with an API and SDK, plus an open-source edition (Apache-2.0). Free plan. Graph memory and user profiles are only on the custom-priced plan. Setup: card not stated, human once (sign up in dashboard).
- [Memori](https://github.com/MemoriLabs/Memori) - Memory layer that records conversations and tool calls as structured state, with Python and TypeScript SDKs and an MCP server. Developer use is free and pricing is not published. It needs an entity ID and a process ID to create memories, and GitHub does not recognise its license. Setup: card not stated, human once (sign up in dashboard, get API key).
- [Memvid](https://github.com/memvid/memvid) - Single-file memory format holding data, embeddings and search index, as a Rust crate with Node and Python SDKs. Open source (Apache-2.0), no hosted offering. An index built with one embedding model fails with another. Setup: no card, no human step.
- [Supermemory](https://supermemory.ai) - Memory and retrieval API that keeps a memory graph per user. Free monthly credits with no rollover. No credits means no usage, and rate limits are not stated. Setup: card not stated, human once (sign up in console, create API key).
- [Zep](https://www.getzep.com) - Hosted context graph for agent memory, built on the open-source Graphiti library. Free monthly credits with no rollover. One credit covers 350 bytes of an episode, so large payloads use credits fast. Setup: card not stated, human once (sign up in dashboard).

## Execution and Sandboxes

Isolated environments for running code and tools.

- [Blaxel](https://blaxel.ai) - Sandboxes that suspend after about 5 seconds idle and resume from saved memory state. Pay-as-you-go with free credits. Agent Drive and the egress gateway have no published price. Setup: card not stated, human once (create account, workspace, API key in console).
- [Daytona](https://www.daytona.io) - Sandboxes created through an SDK and API, with filesystem, process and snapshot control. Pay-as-you-go with free credit and no card required. The free tier has a resource cap until a card is linked. Setup: no card, human once (sign up in dashboard, create API key).
- [E2B](https://e2b.dev) - Cloud sandboxes for agent code, created via SDK. Free Hobby plan with a one-time credit. CPU only, no GPU sandboxes. Setup: no card, human once (sign up in console, copy API key).
- [Fly.io Sprites](https://sprites.dev) - Persistent Linux machines for agents with checkpoints and a wake-on-request HTTPS URL. Billed hourly with a trial credit. Pay-as-you-go can create only 10 Sprites per minute. Setup: card not stated, human once (sign up and approve browser login (or create token in dashboard)).
- [microsandbox](https://github.com/superradcompany/microsandbox) - Local-first microVM runtime with a CLI and SDKs for TypeScript, Rust, Python, Go and Ruby. Open source (Apache-2.0). The README calls it beta software, and it needs KVM on Linux or Apple Silicon on macOS. Setup: no card, no human step.
- [Modal Sandboxes](https://modal.com) - Sandboxes created from the Modal Python and JS SDKs, with optional GPUs. Free Starter plan with monthly compute. Sandboxes are billed at 3x the list price, and containers stay alive 60 seconds after last input. Setup: card not stated, human once (sign up, run modal setup).
- [Runloop](https://runloop.ai) - Devboxes with snapshots and suspend and resume, created via API. Trial credit with no card. The trial is limited to 3 running devboxes. Setup: no card, human once (sign up, create API key in dashboard).
- [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) - Firecracker microVMs created with `Sandbox.create()` from the SDK. Free Hobby plan with a monthly allowance. Hobby caps sessions at 45 minutes and 10 concurrent sandboxes. Setup: card not stated, human once (Vercel account and project link).

## Observability and Evals

Tracing, monitoring and testing of agent behaviour.

- [Braintrust](https://www.braintrust.dev) - Tracing, datasets and evals for LLM and agent apps, with scoring and experiment comparison. Free Starter plan. Self-hosting is Enterprise-only. Setup: no card, human once (sign up in dashboard).
- [Laminar](https://laminar.sh) - Open-source (Apache-2.0) tracing and evals for agents, with a hosted version. Free plan. The free hosted tier is limited to 1 seat and 7-day data access. Setup: card not stated, human once (sign up, create project and API key).
- [Langfuse](https://langfuse.com) - Open-source tracing, prompt management and evals for LLM apps and agents. Free Hobby plan and free self-hosting. Hobby is capped at 2 users. Setup: no card, human once (create account and API keys in project settings).
- [LangSmith](https://www.langchain.com/langsmith) - Tracing, monitoring and evals for LLM and agent apps from LangChain. Free Developer plan. Self-hosting is Enterprise-only. Setup: no card, human once (sign up, create API key in Settings).
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry instrumentation for LLM frameworks, agent frameworks and MCP, sending traces to any OTel backend. Free (Apache-2.0). A library, not a backend, so you supply storage and UI. Setup: no card, no human step.
- [Opik](https://www.comet.com/site/products/opik/) - Open-source (Apache-2.0) tracing and evaluation for LLM apps and agents, from Comet. Free cloud tier and free self-hosting. Newer features are trial-only on the free tier. Setup: card not stated, human step not stated.
- [Phoenix](https://phoenix.arize.com) - Local-first tracing and evals for LLM apps from Arize; Arize AX is the hosted product. AX has a free plan. AX Free has no custom monitors or dashboards. Setup: no card, no human step.

## Security and Guardrails

Protection against prompt injection, permission control, policy enforcement.

- [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) - Library from Microsoft that checks agent tool calls against YAML, OPA or Cedar-style policy rules, with identity, audit logs and an MCP gateway. Free (MIT). Labelled Public Preview, with possible breaking changes before GA. Setup: no card, no human step.
- [agentgateway](https://github.com/agentgateway/agentgateway) - Proxy for agent-to-LLM, agent-to-tool (MCP) and agent-to-agent (A2A) traffic with JWT and OAuth auth, RBAC, rate limits and guardrail hooks. Free (Apache-2.0), a Linux Foundation project. Still in active development. Setup: card not stated, human step not stated.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Python framework that runs input and output validators and enforces structured output on LLM calls, with a Hub of validators. Free (Apache-2.0). Hosted remote inference for validators was discontinued, so validators run locally. Setup: no card, no human step.
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - Rule engine and gateway that checks and can block tool calls and messages in LLM and MCP agent flows. Free (Apache-2.0). Detection depends on rules you write, and the last push was January 2026. Setup: no card, no human step.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - NVIDIA toolkit that adds input, dialog, retrieval, tool-execution and output rails to LLM apps, with flows written in Colang. Free (Apache-2.0). Telemetry is on by default and must be disabled before startup. Setup: no card, no human step.
- [ToolHive](https://github.com/stacklok/toolhive) - Runs each MCP server in an isolated container and applies authentication, authorization policy and audit logging through a gateway. Free (Apache-2.0). Needs Docker, Podman or Kubernetes, and enforcement applies only after you configure an auth source. Setup: card not stated, human step not stated.

## Authentication and Secrets

Credentials, OAuth delegation and agent identity.

- [Aembit](https://aembit.io) - Gives each AI agent its own identity and issues short-lived scoped credentials after a policy check, in front of MCP servers and APIs. Free Starter plan for 3 agents. Free log retention is 24 hours. Setup: card not stated, human once (request free tenant).
- [Arcade](https://www.arcade.dev) - Runtime that handles per-user OAuth and runs tools for agents. Free plan. Free support is community-only. Setup: no card, human once (create Arcade account).
- [Auth0 Token Vault](https://auth0.com/ai) - Stores users’ third-party access and refresh tokens so an agent can exchange them for provider tokens, with CIBA for user approval. Free plan. Token Vault is limited to 2 connections on the free plan, and unlimited needs an add-on. Setup: no card, human once (sign up for Auth0).
- [Composio](https://composio.dev) - Managed OAuth and tool execution for agents across 1,500+ toolkits, with MCP support. Free Hobby plan, hard-capped with no overage. Composio-managed OAuth apps count for a smaller share of the free calls. Setup: no card, human once (sign up in dashboard).
- [Descope](https://www.descope.com) - Authentication service with Outbound Apps for third-party tokens, MCP auth and agent token exchange. Free plan with no overages. Audit retention is one week. Setup: card not stated, human step not stated.
- [Nango](https://www.nango.dev) - Hosted OAuth and API-auth layer that stores connection credentials and syncs data for agent tools. Free plan, hard-capped at 10 connections. Self-hosting is an Enterprise feature. Setup: card not stated, human once (sign up, copy API key).
- [Pipedream Connect](https://pipedream.com/connect) - Managed auth for 3,000+ APIs, with MCP servers and a proxy. Free plan for development only. Serving external users needs a paid plan. Setup: no card, human step not stated.

## Data and Retrieval

Storage and retrieval layers designed for agent workloads.

- [Chroma](https://www.trychroma.com) - Open-source (Apache-2.0) vector, full-text and metadata search database, with a hosted cloud. Starter plan with free credits. Service pauses when a usage limit is hit. Setup: card not stated, human once (sign up in dashboard).
- [LanceDB](https://lancedb.com) - Open-source (Apache-2.0) embedded and cloud vector database. Free-tier limits are not published. Agent use rests on the vendor’s blog posts, not on dedicated agent docs. Setup: card not stated, human step not stated.
- [Neon](https://neon.com) - Serverless PostgreSQL; an agent can create a temporary project with the `neon claim create` CLI and no signup. The project expires after 72 hours unless a human claims it, with 100 MB storage. Only PostgreSQL, the Data API and Managed Better Auth work in claimable mode. Setup: no card, human once (claim the project within 72 hours to keep it).
- [TiDB Cloud Starter](https://www.pingcap.com/tidb-cloud-starter/) - Serverless distributed SQL with vector search, positioned for agents with per-agent isolation. Free tier per organization. Overage rates are not on the page, and PostgreSQL compatibility is in Public Preview. Setup: card not stated, human step not stated.
- [Turso](https://turso.tech) - SQLite-compatible databases pitched as one database per agent, plus the AgentFS SDK for agent files and state. Free plan. Agent-specific features are not described on the pricing page. Setup: no card, human once (sign up via browser).
- [Upstash Redis for agents](https://upstash.com/blog/redis-database-for-agents) - One HTTP POST returns a Redis endpoint and token with no signup. Unclaimed databases are deleted after 3 days. Until claimed, anyone with the database ID can view or edit its data. Setup: no card, human once (claim the database within 3 days to keep it).

## Protocols

Open standards that let agents connect to tools, to each other and to payments. Protocols are specifications, so the free-tier criterion does not apply; they must be open and actively maintained.

- [A2A](https://github.com/a2aproject/A2A) - Protocol for agents built on different frameworks to discover each other through Agent Cards and exchange tasks over JSON-RPC. Open (Apache-2.0), a Linux Foundation project. Authorization schemes in the AgentCard are still being formalized.
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) - Event-based protocol connecting agent backends to user-facing apps. Open (MIT). No versioning guarantees, and many SDKs are community-maintained.
- [Agent Payments Protocol (AP2)](https://github.com/google-agentic-commerce/AP2) - Protocol and reference code for agent-initiated payments. Open (Apache-2.0). No releases, the Python package is not published, and the samples need Google credentials.
- [Agent Skills](https://github.com/agentskills/agentskills) - Open format where a skill is a folder with a `SKILL.md` that agents load on demand, originally developed by Anthropic. Open (Apache-2.0 code, CC-BY-4.0 docs). The full spec lives on a separate page.
- [Agentic Commerce Protocol (ACP)](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol) - Spec from OpenAI and Stripe for agents to buy from merchants. Open (Apache-2.0). The spec is in beta and governed by the two founding maintainers.
- [AGENTS.md](https://github.com/agentsmd/agents.md) - Plain-Markdown convention for giving coding agents project instructions in a predictable file. Open (MIT). There is no formal specification, only a description and a sample.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) - Specification for connecting agents and LLM apps to tools, resources and prompts. Open (MIT). Only collaborators can open pull requests against the spec repository.
- [OASF](https://github.com/agntcy/oasf) - Schema for describing agent capabilities with skill and domain taxonomies, used for agent discovery, from the AGNTCY project. Open (Apache-2.0). Taxonomies are still expanding and adoption is modest.
- [x402](https://www.x402.org/) - Standard where a server answers HTTP 402 and the client pays in stablecoin and retries, with no account or API key. Open (Apache-2.0). The public facilitator is testnet-only.

## Contributing

Last verified: 29 October 2026.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding a tool. Steps are at the top of this page.

Maintained by [Iurii Rogulia](https://iurii.rogulia.fi).
