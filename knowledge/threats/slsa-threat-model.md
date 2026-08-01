---
type: Specification
title: SLSA supply-chain threat model
description: SLSA's A–H taxonomy of supply-chain threats, and the two it explicitly leaves unaddressed.
resource: https://slsa.dev/spec/v1.0/threats
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
    at: '2026-08-01T21:35:00Z'
stale_after: 2027-02-01
sources:
  - id: slsa-threats
    title: 'SLSA v1.0: Supply chain threats'
    resource: https://slsa.dev/spec/v1.0/threats
---

SLSA publishes a labelled taxonomy of where a supply chain can be attacked. It is the most useful
spine available for this subject, because it is lettered, finite, and states its own
coverage.[^slsa-threats]

# Schema

| | Threat |
|---|---|
| **A** | Submit unauthorized change — through source control, without special privileges |
| **B** | Compromise source repo — administrative access or infrastructure compromise |
| **C** | Build from modified source — source that does not match the official repository |
| **D** | **Use compromised dependency** — malicious code injected into a build or runtime dependency |
| **E** | Compromise build process — unauthorized changes to output, or false provenance |
| **F** | Upload modified package — package uploaded without going through the build process |
| **G** | **Compromise package registry** — registry modified via administrative or infrastructure compromise |
| **H** | Use compromised package — modified after leaving the registry, or the user misdirected |

Plus availability threats (denial of access to source or build) and verification threats (tampering
with the expectations or metadata used to verify).

# The part that matters most

**SLSA v1.0 does not address threats A, B, C, D or G.** Dependency threats are stated as "out of
scope of SLSA v1.0"; registry compromise receives no mitigation.[^slsa-threats]

That is not a criticism — SLSA is a *build integrity* framework and says so. But it means a
"SLSA Level 3" claim answers threats E and F and is silent about how the dependency got into the
build in the first place.

Bluntly: **provenance proves how an artifact was built, not that what went into it was
trustworthy.** [Dependency confusion](dependency-confusion.md), [typosquatting](typosquatting.md)
and [maintainer compromise](maintainer-compromise.md) all sit in D, G and H, where SLSA's guarantees
do not reach.

# Related

- [SLSA](/provenance/slsa.md) — the framework this taxonomy belongs to
- [Dependency confusion](dependency-confusion.md) · [Typosquatting](typosquatting.md) ·
  [Maintainer compromise](maintainer-compromise.md) — threats D/G/H in practice

[^slsa-threats]: [SLSA v1.0: Supply chain threats](https://slsa.dev/spec/v1.0/threats)
