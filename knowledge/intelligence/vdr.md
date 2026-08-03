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
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:52:00Z'
stale_after: 2027-02-01
sources:
  - id: cyclonedx-vdr
    title: 'CycloneDX: VDR capability'
    resource: https://cyclonedx.org/capabilities/vdr/
---

**Vulnerability Disclosure Report.** A supplier's standing, outward disclosure of a product's whole
vulnerability picture — *what is wrong*. CycloneDX frames it as the ability to *"communicate known
and unknown vulnerabilities affecting components and services"*, carrying vulnerability sources,
severity, affected components and recommended mitigations.[^cyclonedx-vdr]

> **A sourcing correction.** Earlier revisions of this concept, and the comparison table in
> `landscape.md`, gave VDR "a lineage in NIST and EO 14028". **The CycloneDX VDR page does not say
> that** — it references **ISO/IEC 29147:2018** as the relevant standard for vulnerability
> disclosure and mentions neither NIST nor the Executive Order. The NIST framing is common in US
> policy discussion, but it was attributed here to a source that does not carry it.

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
