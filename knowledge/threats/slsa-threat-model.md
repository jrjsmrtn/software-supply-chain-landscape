---
type: Specification
title: SLSA supply-chain threat model
description: SLSA v1.2's A–I threat taxonomy, what it leaves unaddressed, and the fact that the letters have moved twice.
resource: https://slsa.dev/spec/v1.2/threats
tags:
  - threat
  - slsa
  - taxonomy
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T21:35:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T23:05:00Z'
  - by: claude/opus-5
    at: '2026-08-02T12:30:00Z'
stale_after: 2027-02-01
sources:
  - id: slsa-threats-12
    title: 'SLSA v1.2: Supply chain threats'
    resource: https://slsa.dev/spec/v1.2/threats
  - id: slsa-threats-12-overview
    title: 'SLSA v1.2: Threats overview'
    resource: https://slsa.dev/spec/v1.2/threats-overview
  - id: slsa-threats-11
    title: 'SLSA v1.1: Threats overview (retired)'
    resource: https://slsa.dev/spec/v1.1/threats-overview
  - id: slsa-threats-10
    title: 'SLSA v1.0: Supply chain threats (superseded)'
    resource: https://slsa.dev/spec/v1.0/threats
---

SLSA publishes a labelled taxonomy of where a supply chain can be attacked. It is the most useful
spine available for this subject, because it is lettered, finite, and states its own
coverage.[^slsa-threats-12]

# Schema

**Read the version before citing a letter. They have moved twice.** v1.1 reassigned them — `D` was
*use compromised dependency* in v1.0 and became *External build parameters*.[^slsa-threats-11][^slsa-threats-10]
**v1.2 then added a ninth letter and renamed a second.**[^slsa-threats-12]

v1.2, current:

| | Threat | Group |
|---|---|---|
| **A** | Producer — malicious software from the creator | source |
| **B** | **Modifying the source** — renamed in v1.2 from *Authoring & Reviewing* | source |
| **C** | Source code management — compromised version control | source |
| **D** | External build parameters — tampering with build inputs | build |
| **E** | Build process — compromised build platforms | build |
| **F** | Artifact publication — malicious uploads to distribution | build |
| **G** | Distribution channel — attacks on mirrors and registries | build |
| **H** | **Package selection — typosquatting and naming confusion** | usage |
| **I** | **Usage — "the consumer uses a package in an unsafe manner"** (new in v1.2) | usage |

Dependency threats ("recursive" attacks) and availability threats are described but **carry no
letter**.

> **The spec's own overview lags its detail page.** The overview still describes dependency threats
> as "`A-H`, recursively" while the detail page enumerates `A` through
> `I`.[^slsa-threats-12-overview][^slsa-threats-12] Prefer the detail page.

# The part that matters most

SLSA states its own gaps plainly:[^slsa-threats-12]

- **Source threats (A–C)**: **this gap closed in v1.2.** v1.1's *"SLSA does not yet address source
  threats, but we anticipate doing so in a future version"* is gone from the specification, and a
  [Source track](/provenance/slsa.md) now grades them across four levels.
- **Dependency threats**: *"This version of SLSA does not explicitly address dependency threats, but
  we expect that a future version will."* Unchanged — a Dependency track exists only in the Working
  Draft.
- **Package selection (H)**, including typosquatting: *"This threat is not currently addressed by
  SLSA."*
- **Usage (I)**: *"not addressed by SLSA"* — the new letter arrives already marked out of scope.
- **Availability**: *"SLSA does not currently address availability threats, though future versions
  might."*
- **(G) Distribution Channel** *is* partially addressed, through consumer verification — a change
  made in v1.1, where v1.0 left registry compromise unmitigated.
- **Within (B)**, collusion between two reviewers, "bugdoor" changes that look benign, and rubber
  stamping are each *"not currently addressed by SLSA"* — worth knowing before treating two-party
  review as a solved control.

That is not a criticism; SLSA says what it covers. But it means a "SLSA Level 3" claim — which
almost always means *Build* L3 — answers the build threats and is silent about how the dependency
got into the build, or whether the package you selected was the one you meant. **Since v1.2 a bare
"Level 3" is also ambiguous between tracks**, and worth pinning when you read it.

Bluntly: **provenance proves how an artifact was built, not that what went into it was
trustworthy.** [Dependency confusion](dependency-confusion.md), [typosquatting](typosquatting.md)
and [maintainer compromise](maintainer-compromise.md) live in exactly the categories SLSA leaves
open — and the specification names typosquatting explicitly as unaddressed, which is as clear a statement
as one could ask for that this subdirectory covers ground SLSA does not.

# Related

- [SLSA](/provenance/slsa.md) — the framework this taxonomy belongs to
- [Dependency confusion](dependency-confusion.md) · [Typosquatting](typosquatting.md) ·
  [Maintainer compromise](maintainer-compromise.md) — the categories SLSA leaves open, in practice

[^slsa-threats-12]: [SLSA v1.2: Supply chain threats](https://slsa.dev/spec/v1.2/threats)
[^slsa-threats-12-overview]: [SLSA v1.2: Threats overview](https://slsa.dev/spec/v1.2/threats-overview)
[^slsa-threats-11]: [SLSA v1.1: Threats overview](https://slsa.dev/spec/v1.1/threats-overview)
[^slsa-threats-10]: [SLSA v1.0: Supply chain threats](https://slsa.dev/spec/v1.0/threats)
