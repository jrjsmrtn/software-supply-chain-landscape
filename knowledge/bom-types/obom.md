---
type: BOM Type
title: OBOM
description: Operations Bill of Materials — a full-stack inventory of runtime environments, configurations and their dependencies.
resource: https://cyclonedx.org/capabilities/obom/
tags:
  - bom-type
  - obom
  - operations
  - runtime
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
stale_after: 2027-08-01
sources:
  - id: cdx-obom
    title: 'CycloneDX: OBOM'
    resource: https://cyclonedx.org/capabilities/obom/
---

**"Full-stack inventory of runtime environments, configurations, and additional
dependencies."**[^cdx-obom]

It captures configurations, **operating systems, hardware, and software dependencies active in
staging or production environments**, and gives insight into staging, deployment and operational
states.

# It describes what is running, not what was built

That is the distinction from an [SBOM](sbom.md), and it is the whole reason the type exists. An
SBOM describes an artifact; an OBOM describes a *deployment* — the same artifact plus the operating
system under it, the configuration applied to it, and the environment it sits in.

"Full-stack" is upstream's word and is doing real work: the scope reaches down to the OS and the
hardware, which an artifact-scoped inventory never sees.

Note the consequence: an OBOM is **environment-specific and short-lived**. Staging and production
produce different documents, and both go stale on the next deploy, where an SBOM for a released
artifact does not.

# Related

- [SBOM](sbom.md) — the artifact-scoped counterpart
- [cdxgen](/tools/cdxgen.md) — generates an OBOM, by querying osquery rather than by scanning an
  artifact; the scope, platforms and privilege requirements are recorded there

[^cdx-obom]: [CycloneDX: OBOM](https://cyclonedx.org/capabilities/obom/)
