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
verified:
  - by: claude/opus-5
    at: \'2026-08-01T22:45:00Z\'
stale_after: 2027-02-01
sources:
  - id: osv-dev
    title: OSV — Open Source Vulnerabilities
    resource: https://osv.dev/
  - id: ossf-malicious
    title: 'OpenSSF: Detecting Malicious Packages Using the OSV API'
    resource: https://openssf.org/blog/2026/05/20/detecting-malicious-packages-using-the-osv-api/
    last_modified: '2026-05-20'
---

Not one namespace but a family of them, each owned by the ecosystem that issues it and normalised
into the OSV schema by osv.dev.[^osv-dev]

| Prefix | Source |
|---|---|
| `PYSEC-` | Python / PyPA |
| `RUSTSEC-` | RustSec advisory database |
| `GO-` | Go vulnerability database |
| `GHSA-` | GitHub Advisory Database |
| `MAL-` | OpenSSF malicious-packages — **not a vulnerability namespace** |

The list is not exhaustive — osv.dev aggregates roughly two dozen upstream sources, and the prefix
set grows as ecosystems adopt it.

# `MAL-` is a different kind of claim

`MAL-` records come from OpenSSF's **malicious-packages** repository — "the first open source system
for collecting and publishing cross-ecosystem reports of malicious packages" — and are served
through the same API as everything else, e.g. `https://api.osv.dev/v1/vulns/MAL-2025-6812`, and
matched by the same `/query` and `/querybatch` endpoints.[^ossf-malicious]

The distinction is worth holding onto. A `PYSEC-` or `GHSA-` record says *this version has a flaw*.
A `MAL-` record says *this package is hostile* — there is no fixed version to upgrade to, and the
remedy is removal rather than a bump. A scanner that surfaces both without distinguishing them
invites exactly the wrong response.

They are the machine-readable channel for [typosquatting](/threats/typosquatting.md) and
[maintainer compromise](/threats/maintainer-compromise.md), which no vulnerability feed covers.

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
[^ossf-malicious]: [OpenSSF: Detecting Malicious Packages Using the OSV API](https://openssf.org/blog/2026/05/20/detecting-malicious-packages-using-the-osv-api/)
