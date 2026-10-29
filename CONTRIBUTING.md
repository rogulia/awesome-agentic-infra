# Contributing

The list stays useful only if the filter is strict. Read this before opening a pull request.

## A tool is accepted when

1. **It is agent-native.** Resources are created through an API or SDK, with no interactive login, CAPTCHA or manual step to start.
2. **It is alive.** Public repository with activity in the last 12 months. For a commercial service without a public repository, a current pricing page and documentation.
3. **It is accessible.** Public documentation, plus a free tier, trial or open-source release.
4. **It is infrastructure.** Not an agent, not an orchestration framework, not a thin wrapper over an LLM API.
5. **You have used it, or read its documentation in depth.** Say which in the pull request.

## Protocols

Protocols are specifications, so the free-tier criterion does not apply. A protocol must be open (published license), have a public repository with activity in the last 12 months, and be used by more than its author.

## Entry format

```
- [Name](https://example.com) - What it does. Pricing model. Limitation or caveat.
```

- One line, one sentence per part.
- State facts you checked. If a price or limit comes from the vendor’s page, it must match the page today.
- The caveat is required. An entry without a limitation reads as an advertisement.
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

Fill in the checklist in the template. Maintainers may ask for evidence of use and close pull requests that do not meet the criteria without further discussion.
