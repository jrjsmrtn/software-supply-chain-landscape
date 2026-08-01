---
type: BOM Type
title: MBOM
description: Manufacturing Bill of Materials — declared and observed formulations, workflows and processes for reproducibility.
resource: https://cyclonedx.org/capabilities/mbom/
tags:
  - bom-type
  - mbom
  - manufacturing
  - reproducibility
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
stale_after: 2027-02-01
sources:
  - id: cdx-mbom
    title: 'CycloneDX: MBOM'
    resource: https://cyclonedx.org/capabilities/mbom/
---

**"Declared and observed formulation for reproducibility throughout the product
lifecycle."**[^cdx-mbom]

It documents declared formulations, workflows and **observed** processes for production — how a
product is created, transformed, validated and deployed — enabling traceability from design through
deployment.

# Declared versus observed, again

The pairing is the same distinction that separates
[declared from concluded licences](/licensing/declared-vs-concluded.md): what the process was
*specified* to be, against what a run actually did. An MBOM carrying both makes the gap
inspectable.

That also makes it the family member closest in spirit to
[SLSA provenance](/provenance/slsa.md) — both are claims about *how something was produced* rather
than *what it contains*. MBOM describes the formulation; SLSA grades how hard the record would be
to forge.

# Not the same as HBOM

[HBOM](hbom.md) inventories the components a device *contains*. MBOM describes the process that
*produced* it. A regulated hardware product plausibly needs both, and they answer to different
audiences.

# Related

- [HBOM](hbom.md) — contents rather than process
- [SLSA](/provenance/slsa.md) — the software-build analogue of a production record

[^cdx-mbom]: [CycloneDX: MBOM](https://cyclonedx.org/capabilities/mbom/)
