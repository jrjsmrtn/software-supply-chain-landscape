---
type: Specification
title: SLSA
description: Graded requirements for provenance across two tracks as of v1.2 — measuring the integrity of the build and source processes, not the code.
resource: https://slsa.dev/
tags:
  - provenance
  - specification
  - openssf
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:30:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T23:05:00Z'
  - by: claude/opus-5
    at: '2026-08-02T12:30:00Z'
stale_after: 2027-02-01
sources:
  - id: slsa
    title: SLSA
    resource: https://slsa.dev/
  - id: slsa-v12
    title: SLSA specification v1.2
    resource: https://slsa.dev/spec/v1.2/
  - id: slsa-source
    title: 'SLSA v1.2: Source requirements'
    resource: https://slsa.dev/spec/v1.2/source-requirements
---

**Supply-chain Levels for Software Artifacts.** Graded requirements for provenance, organised into
tracks — the Build track being the one most projects mean when they cite a level.[^slsa]

Build provenance answers *how was this built*: which source, which builder, which parameters. The
grading is about how hard that record would be to forge.

**v1.2 is current; v1.1 is retired.**[^slsa-v12] It defines **two tracks**:

| Track | Grades | Levels |
|---|---|---|
| **Build** | how an artifact was produced from its sources | `Build L1`–`Build L3` |
| **Source** | "how a source revision was created" — version control, retained history, enforced controls, two-party review | `Source L1`–`Source L4`[^slsa-source] |

The Source track matters beyond compiled software: for an artifact that is never built, it is the
only track with anything to say. Build Environment and Dependency tracks exist in the **Working
Draft**, not in v1.2.

> **Version numbering has moved repeatedly, and so have the threat letters.** Cite a level or a
> threat letter only alongside the specification version it refers to — see
> [the threat model](/threats/slsa-threat-model.md), where `D` means different things in v1.0 and
> v1.1, and where v1.2 added a ninth letter and renamed a second.

# The misreading to avoid

**SLSA levels do not measure how secure the code is.** They measure the integrity of the *build and
delivery process*. A high-level artifact can be thoroughly insecure software, faithfully and
verifiably built from thoroughly insecure source.

Code quality is a different axis entirely, and conflating them is how a provenance badge becomes a
substitute for review rather than an addition to it.

# How it travels

SLSA provenance is carried **inside an [in-toto](in-toto.md) attestation envelope**, and signed —
in practice via [Sigstore](sigstore.md). The three are a stack rather than alternatives: SLSA says
*what to record*, in-toto says *how to wrap it*, Sigstore says *how to sign it*.

# Practice

A generator that produces provenance only on a tag push will not run on a manual dispatch, so the
first real verification often happens after a release rather than before it. Exercise the release
path on a throwaway tag rather than discovering the gap on a version you intend to keep.

# Related

- [in-toto](in-toto.md) — the envelope
- [Sigstore](sigstore.md) · [cosign](cosign.md) — the signing layer

[^slsa]: [SLSA](https://slsa.dev/)
[^slsa-v12]: [SLSA specification v1.2](https://slsa.dev/spec/v1.2/)
[^slsa-source]: [SLSA v1.2: Source requirements](https://slsa.dev/spec/v1.2/source-requirements)
