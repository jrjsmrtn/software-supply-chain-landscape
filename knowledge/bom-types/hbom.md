---
type: BOM Type
title: HBOM
description: Hardware Bill of Materials — physical components and their associated firmware, for embedded and connected devices.
resource: https://cyclonedx.org/capabilities/hbom/
tags:
  - bom-type
  - hbom
  - hardware
  - firmware
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
stale_after: 2027-08-01
sources:
  - id: cdx-hbom
    title: 'CycloneDX: HBOM'
    resource: https://cyclonedx.org/capabilities/hbom/
---

**"Inventory hardware components for IoT, ICS, and other types of embedded and connected
devices."**[^cdx-hbom]

It covers **physical hardware components and associated firmware**, together with configurations
and dependencies.

# Firmware is the part that gets forgotten

An HBOM described as "the physical parts of a device" understates it. The firmware riding on those
parts is software with its own supply chain, its own vulnerabilities, and typically no update path
— which is precisely why the hardware inventory has to carry it.

CycloneDX names **healthcare, manufacturing and critical infrastructure** as the industries where
this matters most: long-lived devices, regulated deployment, and a replacement cycle measured in
years rather than sprints.

# Related

- [MBOM](mbom.md) — the adjacent artifact describing how a product was *made*, not what it contains
- [SBOM](sbom.md) — the software analogue
- [cdxgen](/tools/cdxgen.md) — generates HBOM among the family

[^cdx-hbom]: [CycloneDX: HBOM](https://cyclonedx.org/capabilities/hbom/)
