---
type: BOM Type
title: VDR
description: Vulnerability Disclosure Report — the product's whole vulnerability picture, disclosed outward, as opposed to VEX's per-finding adjudication.
tags:
  - vdr
  - vulnerability
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
stale_after: 2027-02-01
sources:
  - id: cyclonedx-vdr
    title: 'CycloneDX: VDR capability'
    resource: https://cyclonedx.org/capabilities/vdr/
---

**Vulnerability Disclosure Report.** A supplier's standing, outward disclosure of a product's whole
vulnerability picture — *what is wrong* — with a lineage in NIST and EO 14028.

It is routinely conflated with [VEX](vex.md), and they share a schema in CycloneDX, but they answer
different questions. VDR **enumerates**; VEX **adjudicates**. Producing a VDR does not discharge
the obligation to tell consumers which findings actually apply to them.

In CycloneDX both are built from the same `vulnerabilities` array; **intent** distinguishes them,
not structure.[^cyclonedx-vdr]

The comparison between the two lives in
[the landscape explanation](/landscape.md#vex-and-vdr--does-it-actually-matter),
because it is a typed relationship and OKF links are untyped.

# Related

- [VEX](vex.md)
- [CycloneDX](/formats/cyclonedx.md) — the shared `vulnerabilities` array

[^cyclonedx-vdr]: [CycloneDX VDR capability](https://cyclonedx.org/capabilities/vdr/)
