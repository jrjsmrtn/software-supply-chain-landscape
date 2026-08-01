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
stale_after: 2026-11-01
sources:
  - id: tea-spec
    title: 'Transparency Exchange API: specification site'
    resource: https://tc54.org/tea/
  - id: tea-repo
    title: CycloneDX/transparency-exchange-api
    resource: https://github.com/CycloneDX/transparency-exchange-api
    last_modified: '2026-05-20'
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
| **Product Release** | **the primary entry point** — what a [TEI](tei.md) resolves to. May optionally belong to a Product |
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

So the asymmetry is deliberate and worth planning around: **a consumer can be built now; a publisher
cannot**, and publishing is the side most projects would need. Governed by OWASP and being
standardized through Ecma International TC54 (task group TG1), with no publication date
announced.[^ecma-tc54]

Only `0.1.0-beta.1` is tagged as a release, and the repository was last updated 2026-05-20 — the
beta designation lives in the README rather than in tags, so do not infer the status from the
release list.

This is the **least settled layer** in the landscape. Anything built on it now is a bet on a moving
specification. The pragmatic near-term posture is to produce artifacts in stable formats and keep
the publishing mechanism replaceable.

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
