---
type: BOM Type
title: SaaSBOM
description: SaaS Bill of Materials — services, endpoints, data flows and their classifications across a cloud-native application.
resource: https://cyclonedx.org/capabilities/saasbom/
tags:
  - bom-type
  - saasbom
  - services
  - cloud-native
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
stale_after: 2027-08-01
sources:
  - id: cdx-saasbom
    title: 'CycloneDX: SaaSBOM'
    resource: https://cyclonedx.org/capabilities/saasbom/
---

**"Inventory services, endpoints, and data flows and classifications that power cloud-native
applications."**[^cdx-saasbom]

It captures service endpoints, dependencies, data flows and **classifications**, describing the
dynamic relationships within a distributed application.

# Data classification is the unusual field

Most of this landscape inventories *code*. A SaaSBOM inventories **runtime relationships between
services**, and attaches a classification to what flows between them — which makes it the one BOM
type that speaks directly to data-protection questions rather than only vulnerability ones.

The practical difficulty follows from the same property: services are discovered, not compiled.
There is no manifest to parse, so a SaaSBOM is closer to an architecture document with a schema
than to a generated artifact — expect it to be authored and verified rather than emitted.

# Related

- [OBOM](obom.md) — the other deployment-time inventory; OBOM describes the stack, SaaSBOM the services
- [cdxgen](/tools/cdxgen.md) — generates SaaSBOM

[^cdx-saasbom]: [CycloneDX: SaaSBOM](https://cyclonedx.org/capabilities/saasbom/)
