---
type: Data Source
title: NVD
description: NIST's enrichment layer over CVE records, adding CPE applicability and CVSS scores.
resource: https://nvd.nist.gov/
tags:
  - vulnerability
  - data-source
  - nist
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
stale_after: 2027-02-01
sources:
  - id: nvd
    title: National Vulnerability Database
    resource: https://nvd.nist.gov/
---

The **National Vulnerability Database** — NIST's enrichment layer over the
[CVE](/naming/cve.md) namespace. It does not issue identifiers; it adds
[CPE](/naming/cpe.md) applicability data and CVSS scores to records that already
exist.[^nvd]

It is listed among "identifier namespaces" often enough to be worth correcting: **NVD is a data
source, not a namespace.**

# Where it is still the answer

[osv.dev](osv-dev.md) is scoped to open-source packages. For **operating systems, appliances, and
commercial products**, NVD and CPE remain the data you have. That is not a transitional state — it
is the segment purl was never designed to name.

# The known weakness

The pairing was built to catalogue vulnerabilities in IT products generally, and it shows:

- The authoritative content is **prose written for humans**.
- The machine-readable part is **CPE**, with its matching imprecision — fuzzy, producing both false
  positives and silent misses.
- Deciding which versions of a library are actually affected often requires a person to read an
  advisory and decide.

Treating a CPE match as authoritative for an open-source dependency is how false positives enter a
triage queue.

# Related

- [CVE](/naming/cve.md) — the namespace NVD enriches
- [CPE](/naming/cpe.md) — the identifier NVD keys applicability on
- [osv.dev](osv-dev.md) — the alternative where the component is an open-source package

[^nvd]: [National Vulnerability Database](https://nvd.nist.gov/)
