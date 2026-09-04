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
    at: '2026-08-01T22:37:22Z'
  - by: claude/opus-5
    at: '2026-09-04T14:00:00Z'
stale_after: 2027-01-04
sources:
  - id: endoflife-date
    title: endoflife.date
    resource: https://endoflife.date/
  - id: eol-api
    title: 'endoflife.date: API v1 documentation'
    resource: https://endoflife.date/docs/api/v1/
---

Community-maintained support-lifecycle database — **470 products as of 2026-09-04**, counted from
the v1 API's own `total` field: operating systems, language runtimes, frameworks, databases,
devices.[^endoflife-date] It was 462 five weeks earlier, which is the drift rate this tier exists
for.

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

Free, **v1**, and responding as of 2026-09-04, at schema version 1.2.1. The *beta* label recorded
when this concept was written, and left unconfirmed at the last review, **is no longer present**:
the OpenAPI contract carries no beta marker anywhere.[^eol-api] Whether it was dropped or the
earlier reading was wrong is not recoverable, so this records the observation and not a story about
it. Lists products, release cycles and dates,
and supports [purl](/naming/purl.md) and [CPE](/naming/cpe.md) mapping, so lifecycle data joins to
a BOM on the same key as vulnerability data.

# Limits

Volunteer-curated; dates get revised; coverage skews to widely-used products. Strong on runtimes,
operating systems and databases. It does **not** attempt the long tail of ordinary libraries, where
"is this maintained" remains a judgement call informed by commit activity and Scorecard signals
rather than a published date.

The product count above is the perishable part of this concept. **Its own `total` field makes it
countable rather than estimable** — quote the field, with the date you read it.

# Related

- [purl](/naming/purl.md) — the shared join key
- [osv.dev](osv-dev.md) — the lagging indicator this complements

[^endoflife-date]: [endoflife.date](https://endoflife.date/)
[^eol-api]: [endoflife.date API v1](https://endoflife.date/docs/api/v1/)
