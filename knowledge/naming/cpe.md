---
type: Identifier
title: CPE (Common Platform Enumeration)
description: NIST's identifier for IT products — vendor, product, version — assigned from a controlled dictionary rather than derived.
resource: https://nvd.nist.gov/products/cpe
tags:
  - identifier
  - naming
  - nist
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:50:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:12:00Z\'
stale_after: 2027-08-01
sources:
  - id: nvd-cpe
    title: 'NVD: Official Common Platform Enumeration Dictionary'
    resource: https://nvd.nist.gov/products/cpe
---

The older component identifier, stewarded by **NIST** and designed to name IT *products* — vendor,
product, version — rather than published packages. Current specification **CPE 2.3**, with NIST
publishing the official dictionary.[^nvd-cpe]

The defining difference from [purl](purl.md) is **derivation**. A purl is computed from the
package's own coordinates; a CPE is *assigned* from a controlled dictionary. That makes CPE
workable for commercial software with a clear vendor, and poor for an open-source dependency graph,
where matching is fuzzy and produces both false positives and silent misses.

It remains load-bearing for one reason: **CPE is the key into NVD data**. BOMs commonly carry both
identifiers, and that is sensible. Treating a CPE match as authoritative for an open-source
dependency is how false positives enter a triage queue.

Practical stance: purl as the primary identifier, CPE where an upstream data source forces it.

# Related

- [purl](purl.md) — the package-oriented identifier; the two are not mutually exclusive
- [CVE](cve.md) — the vulnerability namespace CPE applicability data is attached to

[^nvd-cpe]: [NVD Common Platform Enumeration](https://nvd.nist.gov/products/cpe)
