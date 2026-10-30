# Contributing

The list stays useful only if the filter is strict. Read this before opening a pull request.

## A tool is accepted when

1. **It is agent-native.** Resources are created through an API or SDK. A one-time human step at the start (signing up, copying an API key) is fine and goes into the `Setup:` sentence. After it, no interactive login, CAPTCHA or manual step is needed to create or use a resource.
2. **It is alive.** Public repository with activity in the last 12 months. For a commercial service without a public repository, a current pricing page and documentation.
3. **It is accessible.** Public documentation, plus a free tier, trial or open-source release.
4. **It is infrastructure.** Not an agent, not an orchestration framework, not a thin wrapper over an LLM API.
5. **You have used it, or read its documentation in depth.** Say which in the pull request.

## Protocols

Protocols are specifications, so the free-tier criterion does not apply. A protocol must be open (published license), have a public repository with activity in the last 12 months, and be used by more than its author.

## Entry format

```
- [Name](https://example.com) - What it does. Pricing model. Limitation or caveat. Setup: no card, human once (verify email code).
```

- One line, one sentence per part.
- State facts you checked. If a price or limit comes from the vendor’s page, it must match the page today.
- The caveat is required. An entry without a limitation reads as an advertisement.
- The final `Setup:` sentence is required for every entry outside Protocols. It answers two questions for the free tier, trial or open-source path an agent would use first:
  - Card: `card required`, `no card` or `card not stated`. Use `card not stated` when the vendor’s pages do not say. Do not guess.
  - Human: `no human step` (the agent can create the account or resource through an API or CLI), `human once (<step>)` (a person does something before the first call, for example registers a phone number), `human every time (<step>)` (a person is needed again per session or use) or `human step not stated`. Signing up in a dashboard and copying an API key counts as `human once (sign up in dashboard)`.
- No marketing language, no superlatives, no emoji.
- Alphabetical order within a category.

## Not accepted

- Agents and agent products, orchestration frameworks, LLM providers.
- Tools without public documentation or with a waitlist only.
- Archived or unmaintained projects.
- Referral or affiliate links.
- Pull requests that add several unrelated tools at once. One tool per pull request.

## Links

- Link to the official site or the repository, not to a third-party review.
- Use HTTPS and the shortest working URL. No URL shorteners, tracking parameters or referral codes.
- Do not link to a cached or archived copy.

## Pull request

- Title: `Add <Tool>`. One tool per pull request.
- Add the entry at its alphabetical position in the category.
- Run `pnpm install && pnpm typography:fix` before pushing. The `typography` check fails the pull request if quotes, dashes, ellipses or no-break spaces are not normalized by [polytypo](https://polytypo.dev) (`en-GB`).

No time for a pull request? Open a [suggestion issue](https://github.com/rogulia/awesome-agentic-infra/issues/new?template=suggest-a-tool.md) instead.

Fill in the checklist in the template. Maintainers may ask for evidence of use and close pull requests that do not meet the criteria without further discussion.
