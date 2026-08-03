---
type: Format
title: OpenVEX
description: OpenSSF's minimal standalone VEX format — JSON-LD documents, deliberately small.
resource: https://openvex.dev/
tags:
  - vex
  - format
  - openssf
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:45:00Z'
stale_after: 2027-02-01
sources:
  - id: openvex
    title: OpenVEX
    resource: https://openvex.dev/
  - id: openvex-spec
    title: OpenVEX specification
    resource: https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md
---

The OpenSSF VEX format: **minimal, standalone JSON-LD documents**.[^openvex][^openvex-spec]

Specification **v0.2.0**, released under CC0-1.0. Its status vocabulary — `not_affected`,
`affected`, `fixed`, `under_investigation` — is the one CISA uses, and is documented with
[VEX](vex.md) alongside the CycloneDX values it does not match.

Its design position is that a VEX statement should be small enough to publish continuously and
independently of any BOM. That matters because the useful VEX is often written months after the
artifact stopped changing — a finding arrives, the supplier adjudicates it, and the statement has
to reach consumers without republishing the SBOM.

Its status and justification vocabularies are documented with [VEX](vex.md), alongside the
CycloneDX ones they do not match.

# Choosing between the formats

| | Reach for it when |
|---|---|
| **OpenVEX** | you want standalone statements, published independently and often |
| [**CycloneDX VEX**](/formats/cyclonedx.md) | the VEX travels with the BOM, embedded or alongside |
| [**CSAF VEX**](csaf-vex.md) | a large-vendor or regulated consumer requires CSAF |

# Related

- [VEX](vex.md) — the concept and the state vocabularies
- [CSAF VEX](csaf-vex.md) · [CycloneDX](/formats/cyclonedx.md)

[^openvex]: [OpenVEX](https://openvex.dev/)
[^openvex-spec]: [OpenVEX specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md)
