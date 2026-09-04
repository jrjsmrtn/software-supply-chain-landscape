---
type: Practice
title: Update cooldown
description: Delaying a proposed release until it has existed for a configured period — what makes an automerging update bot net-positive.
tags:
  - practice
  - update-bot
  - supply-chain
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:52:00Z'
  - by: claude/opus-5
    at: '2026-09-04T13:30:00Z'
stale_after: 2027-09-04
sources:
  - id: renovate-min-age
    title: 'Renovate: minimum release age'
    resource: https://docs.renovatebot.com/key-concepts/minimum-release-age/
  - id: dependabot
    title: Dependabot documentation
    resource: https://docs.github.com/en/code-security/dependabot
---

Delays proposing a release until it has existed for a configured period.

**This is the control that makes automated updates safe**, and it is not on by default.
Automated dependency updates are *not* strictly safer than not updating: a bot with automerge and
no cooldown will adopt a compromised release faster than any human would, which is precisely the
window a registry-account takeover exploits.

| Tool | Mechanism |
|---|---|
| [Renovate](renovate.md) | `minimumReleaseAge`[^renovate-min-age] |
| [Dependabot](dependabot.md) | cooldown option, introduced in 2025[^dependabot] |

**Neither delays security fixes.** For Dependabot this is structural rather than a default:
*"The `cooldown` option is only available for **version** updates, not **security**
updates."*[^dependabot] Renovate exempts them by configuration.

That is what makes the trade-off acceptable rather than merely conservative — you are delaying
feature churn, not patches.

# Choosing a period

The useful question is how long a malicious release typically survives before someone notices.
Days rather than hours; the published incidents were caught by humans reading diffs and by
registries acting on reports, neither of which happens in minutes.

# Related

- [Renovate](renovate.md) · [Dependabot](dependabot.md)

[^renovate-min-age]: [Renovate: minimum release age](https://docs.renovatebot.com/key-concepts/minimum-release-age/)
[^dependabot]: [Dependabot documentation](https://docs.github.com/en/code-security/dependabot)
