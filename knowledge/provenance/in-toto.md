---
type: Specification
title: in-toto
description: A signed recipe for how software was built — layout, per-step link metadata, and the attestation envelope that carries provenance.
resource: https://in-toto.io/
tags:
  - provenance
  - attestation
  - specification
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:30:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:12:00Z\'
stale_after: 2027-08-01
sources:
  - id: in-toto
    title: in-toto
    resource: https://in-toto.io/
---

A framework for stating, and then proving, that software was produced the way it was supposed to
be.[^in-toto]

| Piece | What it defines |
|---|---|
| **Layout** | the expected steps, and who is authorized to perform each |
| **Link metadata** | signed evidence that a given step actually ran, and what it consumed and produced |
| **Attestation envelope** | the signed wrapper that carries a claim about an artifact |

The layout is the recipe; the link metadata is the evidence each cook actually followed it.

# Why the envelope matters most in practice

Most projects encounter in-toto not through layouts but through the **attestation envelope**,
because that is what [SLSA](slsa.md) provenance travels inside.

The envelope is deliberately generic. A Statement carries a **`subject`** — a required array of
ResourceDescriptor objects, so one attestation can cover several artifacts — plus a
**`predicateType`** URI naming the kind of claim, and the **`predicate`** itself. Provenance is one predicate type; SBOM references, test
results and review attestations are others. That generality is why "attestation" is worth keeping
distinct from "provenance" — provenance is a kind of attestation, not a synonym for it.

# Related

- [SLSA](slsa.md) — the predicate most commonly carried in the envelope
- [Sigstore](sigstore.md) — what signs it

[^in-toto]: [in-toto](https://in-toto.io/)
