---
type: Identifier
title: BOM-Link
description: A CycloneDX URN referencing another BOM, or one component inside another BOM.
resource: https://cyclonedx.org/capabilities/bomlink/
tags:
  - identifier
  - cyclonedx
  - linking
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:50:00Z'
stale_after: 2027-08-01
sources:
  - id: cyclonedx-bomlink
    title: 'CycloneDX: BOM-Link'
    resource: https://cyclonedx.org/capabilities/bomlink/
---

A URN that references another BOM, or a single component inside another BOM, so that BOMs form a
**graph of independently maintained documents** rather than one monolith.[^cyclonedx-bomlink]

# Schema

```
urn:cdx:serialNumber/version#bom-ref
```

| Part | Meaning |
|---|---|
| `serialNumber` | the target BOM's serial number |
| `version` | the target BOM's version |
| `#bom-ref` | optional — a specific component within that BOM |

Omitting the fragment references the whole document; including it references one component.

# Why it exists

The alternative to linking is merging, and merging forces a choice about whose document is
canonical. BOM-Link lets a supplier publish a BOM for their own artifact and reference a
dependency's BOM without copying it — so each document stays maintained by whoever knows the truth
about it.

# Related

- [purl](purl.md) — identifies a *component*; BOM-Link identifies a *document* or a component
  within one

[^cyclonedx-bomlink]: [CycloneDX BOM-Link](https://cyclonedx.org/capabilities/bomlink/)
