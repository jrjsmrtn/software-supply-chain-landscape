---
type: Specification
title: TEA (Transparency Exchange API)
description: A format-agnostic API for automated discovery and retrieval of supply-chain artifacts for a product release.
resource: https://tc54.org/tea/
tags:
  - distribution
  - specification
  - owasp
  - ecma
status: draft
generated:
  by: claude/opus-5
  at: '2026-08-01T12:40:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:58:00Z'
  - by: claude/opus-5
    at: '2026-09-20T10:00:00Z'
stale_after: 2026-12-20
sources:
  - id: tea-spec
    title: 'Transparency Exchange API: specification site'
    resource: https://tc54.org/tea/
  - id: tea-repo
    title: CycloneDX/transparency-exchange-api
    resource: https://github.com/CycloneDX/transparency-exchange-api
    last_modified: '2026-09-18'
  - id: tea-openapi
    title: 'TEA consumer OpenAPI specification (spec/openapi.yaml)'
    resource: https://github.com/CycloneDX/transparency-exchange-api/blob/main/spec/openapi.yaml
    last_modified: '2026-09-18'
  - id: tea-publisher
    title: 'TEA publisher API specification (spec/publisher)'
    resource: https://github.com/CycloneDX/transparency-exchange-api/blob/main/spec/publisher/README.md
    last_modified: '2026-01-16'
  - id: tea-implementations
    title: 'TEA implementations'
    resource: https://github.com/CycloneDX/transparency-exchange-api/blob/main/doc/tea-implementations.md
    last_modified: '2026-09-18'
  - id: ecma-428
    title: 'ECMA-428: Common Lifecycle Enumeration (CLE), 1st edition'
    resource: https://ecma-international.org/publications-and-standards/standards/ecma-428/
    last_modified: '2025-12'
  - id: ecma-tc54
    title: Ecma TC54
    resource: https://ecma-international.org/technical-committees/tc54/
---

A format-agnostic API for **automated discovery and retrieval** of supply-chain artifacts — SBOM,
[VEX](/intelligence/vex.md), vulnerability reports, attestations — for a product
release.[^tea-spec]

It answers the question the rest of the landscape assumed away. Every other specification describes
a document; none of them says how a consumer *obtains* one. In practice that still means a portal,
a release-page attachment, or an email — a decade of standardizing documents that travel as
attachments.

# Schema

Object model:

| Level | Definition |
|---|---|
| **Product Release** | **the primary entry point** — what a [TEI](tei.md) resolves to. Upstream now states it **belongs to** a Product, where an earlier revision of this concept recorded the relationship as optional |
| **Product** | optional higher-level grouping for a product line or family; releases via `/product/{uuid}/releases` |
| **Component** | a lineage — a collection of Component Releases, via `/component/{uuid}/releases` |
| **Release** | a Component Release; each may carry its own Collection |
| **Collection** | a versioned list of artefacts for a Product Release or a Component Release |
| **Artifact** | the files themselves; one artifact may appear in multiple collections |

An earlier revision of this concept listed four levels and omitted **Product Release** and
**Release** — which mattered, because Product Release is the entry point the whole discovery flow
resolves to.

**The Collection level is the interesting one.** It versions the *set of documents about a release*
independently of the release itself, so republishing — a new VEX for an unchanged binary — is an
explicit, observable event rather than a silent file swap. That is the property a consumer needs,
because the useful VEX is usually written months after the artifact stopped changing.

# Status

**Beta 2**, confirmed 2026-08-02 against the specification repository, which states plainly:
*"TEA is now in beta 2. This beta focuses on ready-to-implement consumer side of the API. Work on
the publisher API will start after the 1.0 release."*[^tea-repo]

The asymmetry is deliberate, but **"a publisher cannot be built" — which this concept previously
said — is too strong.** A publisher specification exists at `spec/publisher/`, and what it says
about itself is the point: *"This specification **will be** a recommended TEA publisher API. The TEA
specification is focused on the consumption API, which is the base of
conformance."*[^tea-publisher] It declares version **0.0.2** against the consumer spec's 0.5.0, and
has not been touched since 2026-01-16 while the consumer side moved.

So the honest form: **a publisher can be built, against a draft that carries no conformance
standing.** Upstream lists three open-source servers — Oolong, ReARM and sbomify — and a client
claiming *"Full compliance of TEA Consumer and Producer OpenAPI specs"*, alongside commercial
endpoints serving `.well-known/tea`.[^tea-implementations] Publishing is happening ahead of the
specification that will govern it, which is a different risk from not being able to publish at all.

Governed by OWASP and being standardized through Ecma International TC54 (task group TG1), with no
publication date announced.[^ecma-tc54]

⚠ **Four version signals disagree, and the useful one is in none of the obvious places.** Checked
2026-09-20:

| Where | What it says |
|---|---|
| the only git release | `0.1.0-beta.1`, published 2025-05-22 |
| the README | **Beta 2** |
| `spec/openapi.yaml` `info.version` | **0.5.0** — *"the OWASP Transparency Exchange API specification for consumers"*[^tea-openapi] |
| the implementations upstream lists | **TEA v0.4.0**[^tea-implementations] |

The advice this concept already gave — *do not infer the status from the release list* — holds and
is stronger than it was: the release tag is sixteen months old while the consumer spec has moved to
0.5.0. **The OpenAPI `info.version` is the number implementations track.** The repository itself was
last pushed 2026-09-18, not the 2026-05-20 this concept recorded.

This is the **least settled layer** in the landscape. Anything built on it now is a bet on a moving
specification. The pragmatic near-term posture is to produce artifacts in stable formats and keep
the publishing mechanism replaceable.

# It now carries lifecycle events, via a ratified standard

Beyond xBOM, CDXA attestations and VDR/VEX, TEA transports **CLE — Common Lifecycle Enumeration**,
standardised as **ECMA-428**, 1st edition 2025-12, defining CLE 1.0.0.[^ecma-428] The events it
enumerates are product rebranding, repackaging, mergers and acquisitions, and milestones including
**end-of-life and end-of-support**.[^tea-spec]

That matters here for a reason the rest of the landscape makes visible:
[endoflife.date](/intelligence/endoflife-date.md) exists because lifecycle status is the *leading*
indicator no scanner reports, and it is community-curated by necessity. CLE is the vendor-published
counterpart of the same fact, arriving over an API — so the question stops being *has anyone
recorded that this is dead* and becomes *did the vendor say so*.

⚠ Two limits stated upstream: inclusion is **optional**, and the CLE endpoints return a *projection*
of CLE content rather than a full CLE 1.0.0 document — a publisher needing the bit-identical
document publishes it as an artifact of type `OTHER` until a dedicated type exists.[^tea-spec]

**Two capabilities are deferred past 1.0**: the publisher API above, and *Insights* — a query
language for "limited transparency", answering questions like *are any of my licensed products from
this vendor vulnerable to this* without the consumer ingesting and converting whole
BOMs.[^tea-spec]

> **VEX carriage is format-limited at the start.** Upstream is format-agnostic in principle, but
> notes that *CSAF has its own distribution requirements that may not be compatible with APIs*, so
> the initial focus is CycloneDX VDR/VEX and [OpenVEX](/intelligence/openvex.md) — which makes
> [CSAF VEX](/intelligence/csaf-vex.md) the one VEX flavour this transport does not yet carry.

# Not another BOM format

TEA is a **transport and discovery API**, deliberately format-agnostic. Adopting it does not change
what you generate — only how consumers find it.

> **Name collision worth knowing.** `tea` is also the Forgejo/Gitea command-line client. Same four
> letters, no relationship.

# Related

- [TEI](tei.md) — the identifier a consumer resolves to reach a Product Release; its syntax and
  DNS-plus-`.well-known` resolution are now documented
- [VEX](/intelligence/vex.md) — the artifact whose late publication motivates the Collection level

[^tea-spec]: [Transparency Exchange API specification site](https://tc54.org/tea/)
[^tea-repo]: [CycloneDX/transparency-exchange-api](https://github.com/CycloneDX/transparency-exchange-api)
[^ecma-tc54]: [Ecma TC54](https://ecma-international.org/technical-committees/tc54/)
[^tea-openapi]: [TEA consumer OpenAPI specification](https://github.com/CycloneDX/transparency-exchange-api/blob/main/spec/openapi.yaml)
[^tea-publisher]: [TEA publisher API specification](https://github.com/CycloneDX/transparency-exchange-api/blob/main/spec/publisher/README.md)
[^tea-implementations]: [TEA implementations](https://github.com/CycloneDX/transparency-exchange-api/blob/main/doc/tea-implementations.md)
[^ecma-428]: [ECMA-428: Common Lifecycle Enumeration (CLE)](https://ecma-international.org/publications-and-standards/standards/ecma-428/)
