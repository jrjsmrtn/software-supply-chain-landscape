---
type: Specification
title: SLSA
description: Graded requirements for build provenance — measuring the integrity of the build and delivery process, not the code.
resource: https://slsa.dev/
tags:
  - provenance
  - specification
  - openssf
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:30:00Z'
stale_after: 2027-08-01
sources:
  - id: slsa
    title: SLSA
    resource: https://slsa.dev/
---

**Supply-chain Levels for Software Artifacts.** Graded requirements for build provenance, organised
into tracks — the Build track being the one most projects mean when they cite a
level.[^slsa]

Provenance answers *how was this built*: which source, which builder, which parameters. The grading
is about how hard that record would be to forge.

> **Level numbering changed between v0.1 and v1.0 and is not restated here.** Cite a level only
> alongside the specification version it refers to, or the claim is ambiguous.

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
