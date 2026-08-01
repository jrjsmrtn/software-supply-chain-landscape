---
type: Tool
title: Dependabot
description: GitHub's hosted dependency-update bot — zero infrastructure, GitHub only.
resource: https://docs.github.com/en/code-security/dependabot
tags:
  - tool
  - update-bot
  - github
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:20:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T22:52:00Z\'
stale_after: 2027-02-01
sources:
  - id: dependabot
    title: Dependabot documentation
    resource: https://docs.github.com/en/code-security/dependabot
---

GitHub's dependency-update bot: proprietary, hosted, and **requires no infrastructure at
all**.[^dependabot]

| | |
|---|---|
| Licence / owner | GitHub (proprietary, hosted) |
| Forges | GitHub only — no clean path to self-hosted GitLab CE, Gitea, or Forgejo |
| Configuration | `.github/dependabot.yml` |
| Infrastructure | none |
| Managers | language package ecosystems, `github-actions`, `docker` |
| Grouping | supported |
| Automerge | limited |
| Advisory source | [GitHub Advisory Database](/naming/ghsa.md) |

The forge constraint is the deciding factor more often than any feature. A project on a
self-hosted forge cannot use it, and one considering a move away from GitHub is choosing a
migration cost along with the bot.

It satisfies the OpenSSF [Scorecard](scorecard.md) `Dependency-Update-Tool` check.

**Configure a [cooldown](update-cooldown.md).** On default settings an update bot is not
unambiguously safer than not updating. Dependabot's `cooldown` block takes `default-days` plus
per-bump `semver-major-days` / `semver-minor-days` / `semver-patch-days`, and `include` / `exclude`
lists of up to 150 entries — so a long delay on majors can coexist with a short one on
patches.[^dependabot]

Note the hard boundary: *"The `cooldown` option is only available for **version** updates, not
**security** updates."*[^dependabot] Security fixes cannot be delayed by it even by
misconfiguration.

# Related

- [Renovate](renovate.md) — the alternative; the comparison lives in
  [the landscape explanation](/landscape.md#dependabot-and-renovate--closing-the-loop)
- [Update cooldown](update-cooldown.md) · [Scorecard](scorecard.md)

[^dependabot]: [Dependabot documentation](https://docs.github.com/en/code-security/dependabot)
