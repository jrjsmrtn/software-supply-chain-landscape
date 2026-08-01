---
type: Identifier
title: GHSA
description: GitHub Advisory Database identifiers, frequently issued before a CVE exists for the same issue.
resource: https://github.com/advisories
tags:
  - identifier
  - vulnerability
  - namespace
  - github
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:50:00Z'
stale_after: 2027-02-01
sources:
  - id: github-advisories
    title: GitHub Advisory Database
    resource: https://github.com/advisories
---

Identifiers issued by GitHub for advisories in the **GitHub Advisory
Database**.[^github-advisories]

The operationally useful property: a GHSA is **often issued before a CVE exists** for the same
issue. A tool that keys only on CVE will therefore miss recently-disclosed problems that are
already actionable, which is why scanners generally consume both namespaces.

GHSA identifiers also appear inside [OSV](osv-ids.md) — the GitHub Advisory Database is one of the
sources osv.dev aggregates, so a `GHSA-` prefixed record can arrive through either channel.

# Related

- [CVE](cve.md) — the shared namespace a GHSA usually acquires an alias in
- [OSV IDs](osv-ids.md) — GHSA is both a namespace of its own and an OSV source

[^github-advisories]: [GitHub Advisory Database](https://github.com/advisories)
