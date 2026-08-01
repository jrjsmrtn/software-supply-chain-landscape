---
type: Identifier
title: CVE
description: The shared vulnerability identifier namespace, assigned by CNAs within defined scopes.
resource: https://www.cve.org/
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
    at: \'2026-08-01T23:05:00Z\'
stale_after: 2027-08-01
sources:
  - id: cve-program
    title: CVE Program
    resource: https://www.cve.org/
---

The shared namespace everyone cites for a vulnerability. Its value is not the data attached to it —
it is that two tools discussing the same flaw use the same string.[^cve-program]

IDs are assigned by **CNAs** (CVE Numbering Authorities), each authorized within a **defined
scope**: named products, repositories, or a package registry. Anything outside every CNA's scope
falls back to a generalist authority with no domain knowledge of it, which is the mechanism behind
uneven per-ecosystem advisory quality.

# Not a competitor to the others

A CVE ID is an identifier, not a data format. [OSV](osv-ids.md) records carry `aliases` linking to
the CVE and [GHSA](ghsa.md) identifiers for the same issue, and NVD enriches CVE records with
[CPE](cpe.md) applicability and CVSS scores. They are layers, not alternatives.

The traditional CVE + NVD pairing was built to catalogue vulnerabilities in IT products generally,
and it shows: the authoritative content is prose written for humans, the machine-readable part is
CPE with its matching imprecision, and deciding "which versions of this library are actually
affected" often needs a person to read an advisory.

# Related

- [GHSA](ghsa.md) · [OSV IDs](osv-ids.md) — the other namespaces, linked by alias
- [CPE](cpe.md) — how NVD expresses which products a CVE applies to

[^cve-program]: [CVE Program](https://www.cve.org/)
