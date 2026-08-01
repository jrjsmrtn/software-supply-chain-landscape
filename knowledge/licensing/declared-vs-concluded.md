---
type: Practice
title: Declared versus concluded licences
description: What a package claims about its licence versus what analysis of its files determined — and why generators emit the former.
tags:
  - licensing
  - practice
  - provenance
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:55:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:12:00Z\'
stale_after: 2027-08-01
sources:
  - id: cyclonedx-licensing
    title: 'CycloneDX: Legal and Compliance Use Case — Open Source Licensing'
    resource: https://cyclonedx.org/use-cases/open-source-licensing/
    last_modified: '2026-08-01'
---

Both major BOM formats distinguish these, and the distinction is the difference between a licence
field you can act on and one you cannot.[^cyclonedx-licensing]

| | Declared | Concluded |
|---|---|---|
| Source | what the package's own metadata claims | what analysis of the actual files determined |
| Trust | author-supplied, unverified at publication | evidence-based |
| Cost to produce | free — read a manifest field | requires scanning file contents |

**They diverge routinely.** The ordinary case is a permissively-licensed package that vendored one
copyleft file; the other is metadata that was correct once and was never updated after the code
moved on.

# Why this matters more than it looks

Most generators emit **declared** by default, because concluding requires reading every file. So a
licence column in a generated SBOM is a *starting point for review*, not a compliance answer — and
it does not announce which it is unless the format's declared/concluded marker is populated.

This is the same weakness that afflicts every author-supplied manifest field: nothing validates it
at publication. A registry that accepts `license: MIT` accepts it from a package that contains no
MIT-licensed file at all.

The mitigation upstream of the SBOM is [REUSE](reuse.md), which turns the declared licence from a
manifest claim into a per-file fact — so a generator reads evidence rather than a promise.

# Related

- [REUSE](reuse.md) — makes the declared value worth declaring
- [SPDX licence expression](spdx-license-expression.md) — where the marker lives in each format
- [Copyleft floor](copyleft-floor.md) — the consequence of getting this wrong on a bundled artifact

[^cyclonedx-licensing]: [CycloneDX open-source licensing use case](https://cyclonedx.org/use-cases/open-source-licensing/)
