---
type: Specification
title: OSV schema
description: The record format that expresses affectedness as version-range boundaries rather than prose a human must interpret.
resource: https://ossf.github.io/osv-schema/
tags:
  - vulnerability
  - schema
  - openssf
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:05:00Z\'
stale_after: 2027-08-01
sources:
  - id: osv-schema
    title: OSV Schema
    resource: https://ossf.github.io/osv-schema/
---

The schema half of OSV. Separated from [osv.dev](osv-dev.md) deliberately: the schema is stable on
a scale of years, while the database's coverage claims move in months.[^osv-schema]

# Schema

| Field | Purpose |
|---|---|
| `id` | the record's own identifier |
| `aliases` | equivalent identifiers in other namespaces (CVE, GHSA, …) |
| `summary` / `details` | human-readable description |
| `severity` | severity scores (e.g. CVSS vectors) |
| `affected[]` | one entry per affected package — the core of the record |
| `affected[].package` | ecosystem, name, and **purl** |
| `affected[].ranges[].events` | `introduced` / `fixed` / `last_affected` boundaries |
| `affected[].versions` | explicit affected versions, where ranges do not apply |
| `references` | advisories, patches, issues |
| `published` / `modified` | record timestamps |
| `withdrawn` | **set when a record is retracted** — a withdrawn advisory is not a finding |
| `schema_version` | which version of the schema the record follows |
| `related` / `upstream` | links to related and upstream records |

`affected[].ranges[].type` takes `GIT`, `SEMVER` or `ECOSYSTEM` — which is how one record
expresses affectedness for a tagged release and for a commit range.

# Why the events model matters

`withdrawn` deserves attention: a scanner that ignores it keeps reporting an advisory the upstream
database has retracted — a false positive with its own authoritative retraction sitting in the
same record.

`events` is what makes a record machine-actionable. Affectedness is expressed as **version-range
boundaries** rather than as prose a person must read and interpret.

Compare the traditional route: a CVE's authoritative content is written for humans, and deciding
"which versions of this library are actually affected" needs someone to read an advisory and form a
judgement. An `introduced` / `fixed` pair is a comparison.

Records key on [purl](/naming/purl.md), so joining "what I have" to "what is known bad" is a
lookup rather than a heuristic.

# Related

- [osv.dev](osv-dev.md) — the database that aggregates records in this schema
- [OSV IDs](/naming/osv-ids.md) — the identifier namespaces records carry
- [purl](/naming/purl.md) — the join key

[^osv-schema]: [OSV Schema](https://ossf.github.io/osv-schema/)
