---
type: Specification
title: Sigstore
description: Keyless signing — short-lived certificates bound to an OIDC identity, with every signing event recorded in a public transparency log.
resource: https://www.sigstore.dev/
tags:
  - signing
  - provenance
  - openssf
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:30:00Z'
stale_after: 2027-08-01
sources:
  - id: sigstore
    title: Sigstore
    resource: https://www.sigstore.dev/
---

Signing without owning a key. The problem it removes is **key management** — historically the
reason artifact signing stayed a minority practice, because a long-lived private key has to be
stored, rotated, and kept off developer laptops.[^sigstore]

# Components

| Component | Role |
|---|---|
| **Fulcio** | certificate authority issuing short-lived certificates bound to an OIDC identity |
| **Rekor** | public append-only transparency log of signing events |
| [**cosign**](cosign.md) | the client — signs and verifies artifacts and attestations |

Fulcio and Rekor are described here rather than as separate concepts: each is one role, and
neither is meaningful outside the flow below.

# The keyless flow

1. Authenticate via OIDC — a personal account, or a CI workload identity.
2. Fulcio issues a certificate valid for **minutes**.
3. Sign within that window.
4. The private key is **discarded**.
5. The event is recorded in Rekor.

The certificate binds the signature to an *identity* rather than to a key you keep. That is what
makes CI signing safe: the workflow's own identity signs, and there is no secret to leak because
nothing outlives the run.

# What signing does not do

**Signing establishes who published an artifact.** It says nothing about whether that publisher
was compromised, or whether the signed contents are trustworthy — a compromised maintainer signs
malicious releases perfectly validly.

Verification is only meaningful when it is **pinned to an expected identity**. A valid Sigstore
signature by itself tells you that *somebody* signed this.

# Related

- [cosign](cosign.md) — the client, and how to pin verification to an identity
- [SLSA](slsa.md) · [in-toto](in-toto.md) — what gets signed at release time

[^sigstore]: [Sigstore](https://www.sigstore.dev/)
