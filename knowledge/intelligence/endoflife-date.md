---
type: Data Source
title: endoflife.date
description: Community-maintained support-lifecycle database — the leading indicator vulnerability scanners are blind to.
resource: https://endoflife.date/
tags:
  - lifecycle
  - data-source
  - eol
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T22:37:22Z\'
stale_after: 2026-12-01
sources:
  - id: endoflife-date
    title: endoflife.date
    resource: https://endoflife.date/
  - id: eol-api
    title: 'endoflife.date: API v1 documentation'
    resource: https://endoflife.date/docs/api/v1/
---

Community-maintained support-lifecycle database — **462 products as of 2026-08-02**, counted from
the v1 API: operating systems, language runtimes, frameworks, databases, devices.[^endoflife-date]

Vulnerability data is a *lagging* indicator: it reports what has already been found and published.
Lifecycle status is the *leading* one, and no scanner reports it. A component with zero known
vulnerabilities that reached end of life two years ago should not be read as "no problems found"
but as "nobody is looking, and when something is found there will be no fix."

# Schema

Per release cycle:

| Field | Meaning |
|---|---|
| release date | when the cycle was first released |
| latest | most recent patch version in the cycle |
| LTS | whether this is a long-term-support line |
| **end of active support** | no further bug fixes or features |
| **end of security support (EOL)** | no further patches of any kind |

**The two end dates are distinct and often years apart.** The security date is the one that
converts a dependency into a liability; treating "supported" as a single boolean discards the
information you need for planning.

# API

Free, **v1**, and responding as of 2026-08-02. It was documented as *beta* when this concept was
written and **that status was not re-confirmed** at the last review — treat the stability of the
contract as unverified rather than assuming either way.[^eol-api] Lists products, release cycles and dates,
and supports [purl](/naming/purl.md) and [CPE](/naming/cpe.md) mapping, so lifecycle data joins to
a BOM on the same key as vulnerability data.

# Limits

Volunteer-curated; dates get revised; coverage skews to widely-used products. Strong on runtimes,
operating systems and databases. It does **not** attempt the long tail of ordinary libraries, where
"is this maintained" remains a judgement call informed by commit activity and Scorecard signals
rather than a published date.

The product count and beta API status above are the perishable parts of this concept.

# Related

- [purl](/naming/purl.md) — the shared join key
- [osv.dev](osv-dev.md) — the lagging indicator this complements

[^endoflife-date]: [endoflife.date](https://endoflife.date/)
[^eol-api]: [endoflife.date API v1](https://endoflife.date/docs/api/v1/)
