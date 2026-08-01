---
type: Identifier
title: OSV IDs
description: Per-source ecosystem advisory identifiers, normalised into one schema and aggregated by osv.dev.
resource: https://osv.dev/
tags:
  - identifier
  - vulnerability
  - namespace
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:50:00Z'
stale_after: 2027-02-01
sources:
  - id: osv-dev
    title: OSV — Open Source Vulnerabilities
    resource: https://osv.dev/
---

Not one namespace but a family of them, each owned by the ecosystem that issues it and normalised
into the OSV schema by osv.dev.[^osv-dev]

| Prefix | Source |
|---|---|
| `PYSEC-` | Python / PyPA |
| `RUSTSEC-` | RustSec advisory database |
| `GO-` | Go vulnerability database |
| `GHSA-` | GitHub Advisory Database |

The list is not exhaustive — osv.dev aggregates roughly two dozen upstream sources, and the prefix
set grows as ecosystems adopt it.

# Why per-source identifiers rather than one namespace

Advisories are authored by whoever actually owns the package, so affected version ranges are
*accurate rather than inferred*. Keeping the issuing source visible in the identifier preserves
that provenance: `RUSTSEC-2021-0001` says who decided what "affected" means.

An OSV record carries `aliases` linking to the [CVE](cve.md) and [GHSA](ghsa.md) identifiers for
the same issue, so these namespaces are layers rather than competitors.

Records key on [purl](purl.md), which is what makes joining "what I have" to "what is known bad" a
lookup rather than a heuristic.

# Related

- [purl](purl.md) — the join key OSV records use
- [CVE](cve.md) · [GHSA](ghsa.md) — linked by alias

[^osv-dev]: [OSV — Open Source Vulnerabilities](https://osv.dev/)
