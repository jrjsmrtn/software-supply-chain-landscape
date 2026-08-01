---
type: Tool
title: Renovate
description: The forge-agnostic dependency-update bot — AGPL-3.0, self-hostable, and the only option for a self-hosted forge.
resource: https://docs.renovatebot.com/
tags:
  - tool
  - update-bot
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:20:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T22:52:00Z\'
stale_after: 2027-02-01
sources:
  - id: renovate
    title: Renovate documentation
    resource: https://docs.renovatebot.com/
  - id: renovate-min-age
    title: 'Renovate: minimum release age'
    resource: https://docs.renovatebot.com/key-concepts/minimum-release-age/
---

AGPL-3.0, maintained by Mend, and **forge-agnostic** — which is usually why it is
chosen.[^renovate]

| | |
|---|---|
| Licence / owner | AGPL-3.0, maintained by Mend |
| Forges | GitHub, GitLab, Bitbucket, Azure DevOps, Gitea, Forgejo — hosted or self-hosted |
| Configuration | `renovate.json` / preset inheritance |
| Infrastructure | hosted app, or self-hosted runner |
| Managers | language package ecosystems, `github-actions`, `docker`, plus Dockerfiles, Kubernetes manifests, Terraform, and more |
| Grouping | extensive rule-based grouping |
| Automerge | policy-driven |
| Dashboard | dependency dashboard issue |
| Advisory source | OSV and ecosystem sources |

Two things it buys beyond forge coverage: **preset inheritance**, so a fleet of repositories shares
one policy, and a **dependency dashboard** issue that makes the backlog visible without opening
every pull request.

The cost is infrastructure — the hosted app or a self-hosted runner — where
[Dependabot](dependabot.md) needs none.

It satisfies the OpenSSF [Scorecard](scorecard.md) `Dependency-Update-Tool` check.

**Configure a [cooldown](update-cooldown.md)** via `minimumReleaseAge`.[^renovate-min-age]

# Related

- [Dependabot](dependabot.md) — the alternative; the comparison lives in
  [the landscape explanation](/landscape.md#dependabot-and-renovate--closing-the-loop)
- [Update cooldown](update-cooldown.md) · [Scorecard](scorecard.md)

[^renovate]: [Renovate documentation](https://docs.renovatebot.com/)
[^renovate-min-age]: [Renovate: minimum release age](https://docs.renovatebot.com/key-concepts/minimum-release-age/)
