---
type: BOM Type
title: SBOM
description: Software Bill of Materials — components, services, and the dependency relationships between them.
resource: https://cyclonedx.org/capabilities/sbom/
tags:
  - bom-type
  - sbom
  - software
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
stale_after: 2027-02-01
sources:
  - id: cdx-sbom
    title: 'CycloneDX: SBOM'
    resource: https://cyclonedx.org/capabilities/sbom/
---

The original, and the one every other variant generalises from.

CycloneDX's definition: **"Inventory software components and services and the dependency
relationships between them."**[^cdx-sbom]

It covers first-party and third-party libraries, their versions, and their **hierarchical
interconnections** — the relationships, not merely the list.

# The relationships are the point

A flat inventory answers "is this package present somewhere?" The dependency graph answers "am I
affected, and through what path?" — which is the question that makes a BOM actionable, and the
reason [CycloneDX](/formats/cyclonedx.md) foregrounds the graph.

An SBOM is an inventory, not a defense. It changes nothing on its own; it makes the next question
answerable. What that next question is, and why the family exists at all, is in
[the landscape explanation](/landscape.md#the-xbom-family--whats-in-the-box).

# Related

- [Declaring BOM completeness](/formats/bom-completeness.md) — a partial SBOM is indistinguishable from a complete one unless it says so
- [purl](/naming/purl.md) — how the components inside are named
- [syft](/tools/syft.md) · [cdxgen](/tools/cdxgen.md) — what generates one

[^cdx-sbom]: [CycloneDX: SBOM](https://cyclonedx.org/capabilities/sbom/)
