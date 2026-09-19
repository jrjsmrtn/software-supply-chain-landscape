---
type: Tool
title: cosign
description: The Sigstore client — signs and verifies artifacts and attestations, most commonly container images.
resource: https://docs.sigstore.dev/cosign/signing/overview/
tags:
  - tool
  - signing
  - sigstore
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:30:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:37:22Z'
  - by: claude/opus-5
    at: '2026-09-20T11:00:00Z'
stale_after: 2027-01-20
sources:
  - id: cosign
    title: 'Sigstore: cosign'
    resource: https://docs.sigstore.dev/cosign/signing/overview/
---

The [Sigstore](sigstore.md) client. Signs and verifies artifacts and attestations, most commonly
container images.[^cosign]

# The identity is the point, not the ceremony

Verification without an expected identity proves only that *somebody* signed the artifact. cosign
enforces this rather than leaving it to the user: **omitting the identity flag fails**, in keyless
mode, with

```
--certificate-identity or --certificate-identity-regexp is required
for verification in keyless mode
```

A signature made by anyone else is then rejected by name, which is the property worth having:

```
expected SAN value to match regex "^https://github.com/someone-else/evil/",
got "https://github.com/<owner>/<repo>/.github/workflows/release.yml@refs/tags/v1.2.3"
```

# Version note that breaks scripts

**cosign v3 uses the Sigstore bundle format.** The v2 pair of `--output-signature` and
`--output-certificate` fails there with `create bundle file: open : no such file or directory`.
v3 emits a single bundle file carrying the signature, the signing certificate and the Rekor
inclusion proof together.

This was hit in a real release pipeline rather than read off a changelog, which is why it is
recorded here rather than left to be rediscovered. Verify the installed binary's major version
before copying any signing snippet.

The v3 line remains current — **3.1.3 as of 2026-08-06** — and the bundle format is unchanged since
3.0. **Both error texts above were re-reproduced against 3.1.3** on 2026-09-20, and
`cosign sign --help` no longer lists `--output-signature` or `--output-certificate` at all.

⚠ **v2 has not been retired, which is why checking the major version still matters.** `v2.6.5`
shipped on **2026-08-06, the same day as v3.1.3**, and `v2.6.4` a fortnight before it. Two major
lines are being released in parallel, so "cosign is on v3 now" is not a safe assumption about any
particular machine — the installed binary decides which flags exist.

# Practice

**Verify the signature you just produced, in the same pipeline that produced it.** Producing a
signature is not the same as producing a verifiable one, and shipping an unverifiable signature is
worse than shipping none — it invites a check that silently passes for the wrong reason.

# Related

- [Sigstore](sigstore.md) — Fulcio, Rekor, and the keyless flow
- [model-signing (OMS)](model-signing.md) — the sibling for **directory trees**: cosign signs a blob
  or an image, model-signing signs a manifest over every file in a tree
- [SLSA](slsa.md) — provenance is the other half of a signed release

[^cosign]: [Sigstore: cosign](https://docs.sigstore.dev/cosign/signing/overview/)
