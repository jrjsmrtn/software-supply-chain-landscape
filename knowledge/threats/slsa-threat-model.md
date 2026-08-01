---
type: Specification
title: SLSA supply-chain threat model
description: SLSA v1.1's A–H threat taxonomy, what it leaves unaddressed, and the fact that v1.1 reassigned the letters.
resource: https://slsa.dev/spec/v1.1/threats-overview
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
stale_after: 2027-08-01
sources:
  - id: slsa-threats-11
    title: 'SLSA v1.1: Threats overview'
    resource: https://slsa.dev/spec/v1.1/threats-overview
  - id: slsa-threats-11-detail
    title: 'SLSA v1.1: Supply chain threats'
    resource: https://slsa.dev/spec/v1.1/threats
  - id: slsa-threats-10
    title: 'SLSA v1.0: Supply chain threats (superseded)'
    resource: https://slsa.dev/spec/v1.0/threats
---

SLSA publishes a labelled taxonomy of where a supply chain can be attacked. It is the most useful
spine available for this subject, because it is lettered, finite, and states its own
coverage.[^slsa-threats-11]

# Schema

**Read the version before citing a letter.** SLSA **v1.1** reassigned them, so the same label means
different things in v1.0 and v1.1 material — `D` was *use compromised dependency* and is now
*External Build Parameters*.[^slsa-threats-11][^slsa-threats-10]

v1.1, current:

| | Threat | Group |
|---|---|---|
| **A** | Producer — malicious software from the creator | source |
| **B** | Authoring & Reviewing — unauthorized commits during review | source |
| **C** | Source Code Management — compromised version control | source |
| **D** | External Build Parameters — tampering with build inputs | build |
| **E** | Build Process — compromised build platforms | build |
| **F** | Artifact Publication — malicious uploads to distribution | build |
| **G** | Distribution Channel — attacks on mirrors and registries | build |
| **H** | **Package Selection — typosquatting and naming confusion** | usage |

Dependency threats ("recursive" attacks) and availability threats are described but **carry no
letter**.

# The part that matters most

SLSA v1.1 states its own gaps plainly:[^slsa-threats-11-detail]

- **Source threats (A–C)**: *"SLSA does not yet address source threats, but we anticipate doing so
  in a future version."*
- **Dependency threats**: *"This version of SLSA does not explicitly address dependency threats,
  but we expect that a future version will."*
- **Package selection (H)**, including typosquatting: *"This threat is not currently addressed by
  SLSA."*
- **Availability**: not currently addressed.
- **(G) Distribution Channel** *is* partially addressed in v1.1, through consumer verification —
  a change from v1.0, where registry compromise had no mitigation.

That is not a criticism; SLSA is a *build integrity* framework and says so. But it means a
"SLSA Level 3" claim answers the build threats and is silent about how the dependency got into the
build, or whether the package you selected was the one you meant.

Bluntly: **provenance proves how an artifact was built, not that what went into it was
trustworthy.** [Dependency confusion](dependency-confusion.md), [typosquatting](typosquatting.md)
and [maintainer compromise](maintainer-compromise.md) live in exactly the categories SLSA leaves
open — and v1.1 now names typosquatting explicitly, which is as clear a statement as one could ask
for that this subdirectory covers ground SLSA does not.

# Related

- [SLSA](/provenance/slsa.md) — the framework this taxonomy belongs to
- [Dependency confusion](dependency-confusion.md) · [Typosquatting](typosquatting.md) ·
  [Maintainer compromise](maintainer-compromise.md) — the categories SLSA leaves open, in practice

[^slsa-threats-11]: [SLSA v1.1: Threats overview](https://slsa.dev/spec/v1.1/threats-overview)
[^slsa-threats-11-detail]: [SLSA v1.1: Supply chain threats](https://slsa.dev/spec/v1.1/threats)
[^slsa-threats-10]: [SLSA v1.0: Supply chain threats](https://slsa.dev/spec/v1.0/threats)
