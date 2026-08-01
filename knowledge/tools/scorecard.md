---
type: Tool
title: OpenSSF Scorecard
description: Automated assessment of a repository's security practices, scored per check — grading the process rather than any single release.
resource: https://scorecard.dev/
tags:
  - tool
  - openssf
  - posture
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:20:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T22:45:00Z\'
stale_after: 2027-02-01
sources:
  - id: scorecard
    title: OpenSSF Scorecard
    resource: https://scorecard.dev/
---

Automated assessment of a repository's security *practices*, scored per check and
aggregated.[^scorecard]

It is the odd one out in this bundle: everything else describes an artifact or a finding, while
Scorecard grades **the process that produced them**, continuously and independently of any single
release.

Checks that intersect the rest of this bundle:

| Check | What it looks for |
|---|---|
| `Dependency-Update-Tool` | [Dependabot](dependabot.md) or [Renovate](renovate.md) configured |
| `Pinned-Dependencies` | lockfiles committed, actions and images pinned |
| `Signed-Releases` | release artifacts carry signatures |
| `Security-Policy` | a `SECURITY.md` with a disclosure route |
| `Branch-Protection` | review and status-check requirements on the default branch |
| `Token-Permissions` | least-privilege CI token scopes |
| `SBOM` | whether a release publishes one — the check most directly about this bundle's subject |

# Detection is positional, and that bites

Scorecard locates update-bot configuration in several places, including Renovate config in a
`.gitlab` directory. **A passing or failing result can therefore hinge on config placement rather
than on whether a bot is actually running.**

Treat an unexpected score as a question about detection before treating it as a question about
practice. The inverse also holds: a passing check is evidence a file exists in an expected
location, not that the control works.

# Related

- [Dependabot](dependabot.md) · [Renovate](renovate.md) — what `Dependency-Update-Tool` detects

[^scorecard]: [OpenSSF Scorecard](https://scorecard.dev/)
