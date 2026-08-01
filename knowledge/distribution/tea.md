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
stale_after: 2026-11-01
sources:
  - id: tea-spec
    title: 'Transparency Exchange API: specification site'
    resource: https://tc54.org/tea/
  - id: tea-repo
    title: CycloneDX/transparency-exchange-api
    resource: https://github.com/CycloneDX/transparency-exchange-api
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
| **Product** | optional higher-level grouping for a product line or family |
| **Component** | a lineage — a collection of component releases |
| **Collection** | a versioned list of artifacts for one release |
| **Artifact** | the files themselves; one artifact may appear in multiple collections |

**The Collection level is the interesting one.** It versions the *set of documents about a release*
independently of the release itself, so republishing — a new VEX for an unchanged binary — is an
explicit, observable event rather than a silent file swap. That is the property a consumer needs,
because the useful VEX is usually written months after the artifact stopped changing.

# Status

**Beta 2 as of 2026-07**, consumer-side first. Governed by OWASP and being standardized through
Ecma International TC54 (task group TG1); the Ecma specification is in development with no
publication date.[^tea-repo][^ecma-tc54]

This is the **least settled layer** in the landscape. Anything built on it now is a bet on a moving
specification. The pragmatic near-term posture is to produce artifacts in stable formats and keep
the publishing mechanism replaceable.

# Not another BOM format

TEA is a **transport and discovery API**, deliberately format-agnostic. Adopting it does not change
what you generate — only how consumers find it.

> **Name collision worth knowing.** `tea` is also the Forgejo/Gitea command-line client. Same four
> letters, no relationship.

# Related

- [TEI](tei.md) — the identifier a consumer resolves to reach a release
- [VEX](/intelligence/vex.md) — the artifact whose late publication motivates the Collection level

[^tea-spec]: [Transparency Exchange API specification site](https://tc54.org/tea/)
[^tea-repo]: [CycloneDX/transparency-exchange-api](https://github.com/CycloneDX/transparency-exchange-api)
[^ecma-tc54]: [Ecma TC54](https://ecma-international.org/technical-committees/tc54/)
