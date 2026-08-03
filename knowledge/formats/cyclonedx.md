---
type: Format
title: CycloneDX
description: OWASP's security-first BOM format — the whole xBOM family in one schema, with a dependency graph and native VEX.
resource: https://cyclonedx.org/
tags:
  - format
  - bom
  - owasp
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:00:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:45:00Z'
stale_after: 2027-02-01
sources:
  - id: cyclonedx
    title: CycloneDX
    resource: https://cyclonedx.org/
  - id: cyclonedx-licensing
    title: 'CycloneDX: Legal and Compliance Use Case — Open Source Licensing'
    resource: https://cyclonedx.org/use-cases/open-source-licensing/
    last_modified: '2026-08-01'
---

A BOM has to be written down in something. CycloneDX is the OWASP answer, **designed security-first**,
and standardized as **ECMA-424**.[^cyclonedx]

| | |
|---|---|
| Steward | OWASP |
| Origin | vulnerability management |
| Standardization | Ecma (ECMA-424) |
| Current specification | **1.7.1**, released 2026-06-02 |
| Serializations | JSON, XML, Protocol Buffers |
| xBOM coverage | SBOM, HBOM, OBOM, SaaSBOM, ML-BOM, CBOM — one format |
| VEX / VDR | native, via the `vulnerabilities` array |
| Typical audience | security |

Three properties follow from the security-first origin and are the reason to pick it:

- **The dependency graph, not a flat list.** Which component pulled in which — so "am I affected,
  and through what path?" is answerable, rather than only "is this package present somewhere?"
- **The whole xBOM family in one schema**, rather than a different format per BOM type.
- **VEX and VDR are native**, sharing the `vulnerabilities` array with the BOM rather than living
  in a separate document and toolchain. Triage is the bottleneck, so this matters more than it
  sounds.

Licence data is recorded per component in `components[].licenses[]`, accepting an SPDX identifier,
an SPDX expression, or a free-text name.[^cyclonedx-licensing]

# The two are complementary, not rivals

Treating this as a either/or is the common mistake, and 3.0 made it a costlier one. The scopes
overlap heavily and diverge at the edges — and the edges are where the choice actually gets made.

| Question | Better served by |
|---|---|
| What is in this build, and what reached what through which path? | **CycloneDX** — the dependency graph is first-class |
| Is this finding exploitable here? | **Either** — both carry VEX natively as of SPDX 3.0 |
| Is this BOM complete? | **CycloneDX** — [`compositions`](bom-completeness.md) states it explicitly |
| What is this model, how much energy did it cost, what bias is known? | **SPDX** — the [AI and Dataset profiles](spdx-ai-profile.md) have no CycloneDX equivalent |
| What exactly is each component licensed under, declared versus concluded? | **SPDX** — distinct fields, and the ISO reference procurement asks for |
| One document across hardware, crypto, operations and services? | **CycloneDX** — the whole xBOM family in one schema |

A project shipping a model inside a container has a defensible reason to emit **both**: SPDX for the
model and its training data, CycloneDX for the application and its dependency graph. That is not
duplication — the two documents describe different things.

The failure mode to avoid is emitting both for the *same* content and leaving no answer to which is
authoritative when they disagree.

# Related

- [SPDX](spdx.md) — the other dominant format; the comparison lives in
  [the landscape explanation](/landscape.md#cyclonedx-and-spdx--the-file-formats)
- [Declaring BOM completeness](bom-completeness.md) — the `compositions` mechanism
- [Merging BOMs](bom-merging.md)
- [BOM-Link](/naming/bom-link.md) — referencing another BOM instead of merging it
- [SPDX licence expression](/licensing/spdx-license-expression.md) — what the licence field carries

[^cyclonedx]: [CycloneDX](https://cyclonedx.org/)
[^cyclonedx-licensing]: [CycloneDX open-source licensing use case](https://cyclonedx.org/use-cases/open-source-licensing/)
