---
type: Tool
title: model-signing (OMS)
description: Signs a directory tree rather than a single file, by hashing every component into a manifest and signing that — the Sigstore project's answer to multi-file artifacts.
resource: https://github.com/sigstore/model-transparency
tags:
  - tool
  - signing
  - sigstore
  - ai
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T22:13:20Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:13:20Z'
stale_after: 2027-02-01
sources:
  - id: model-transparency
    title: sigstore/model-transparency
    resource: https://github.com/sigstore/model-transparency
    last_modified: '2026-07-27'
  - id: pypi
    title: 'PyPI: model-signing'
    resource: https://pypi.org/project/model-signing/
  - id: nvidia-signing
    title: 'NVIDIA: Signing agent skills'
    resource: https://github.com/NVIDIA/skills/blob/main/docs/signing-agent-skills.mdx
    last_modified: '2026-08-01'
---

From the Sigstore project (`sigstore/model-transparency`, Apache-2.0; PyPI `model-signing`, 1.1.1 at
the time of writing).[^model-transparency][^pypi] It exists because
[cosign](cosign.md) signs *a* thing, and a model is not one thing.

# The unit of signing is a directory

A trained model is weight shards, config, tokenizer files, and more. Signing one of them proves
nothing about the rest; signing an archive of them loses the ability to say *which* file changed.

model-signing hashes **every component** into a **manifest**, then signs the manifest. Verification
therefore covers the whole tree, and detects a modified, added or removed file rather than merely a
different blob.

NVIDIA's description of the format is the clearest one-liner available: OMS
*"extends Sigstore-style bundles so verification can cover a directory tree instead of only a single
file."*[^nvidia-signing]

**OMS — the OpenSSF Model Signing format — is the format; `model-signing` is one
OMS-compatible implementation.** The same separation as [Sigstore](sigstore.md) and
[cosign](cosign.md). (The OMS specification itself was not read for this concept; the
characterisation above is NVIDIA's.)

# Schema

| Command | Purpose |
|---|---|
| `model_signing sign <dir>` | sign, Sigstore keyless by default |
| `model_signing sign key <dir> --private-key key.priv` | sign with a private key |
| `model_signing verify <dir> --signature model.sig --identity <id> --identity-provider <oidc>` | verify against an expected identity |
| `model_signing digest <dir>` | compute the manifest digest without signing |

Four signing methods: **Sigstore keyless** (OIDC, the default), **private key** (EC or RSA),
**certificate**, and **PKCS #11** for HSMs and crypto devices via RFC 7512 URIs.[^model-transparency]

Hashing covers files and file shards, and ignores git paths by default.

# It is not only for models

The directory-tree property generalises to anything shipped as a tree of files. NVIDIA signs its
**agent skills** with it — every published skill carries a detached `skill.oms.sig`, verified
against a published root certificate, and the sync pipeline drops anything
unsigned.[^nvidia-signing]

That is worth noticing: an **OKF knowledge bundle is also a directory tree**, and has no integrity
story of its own. The same tool applies without waiting for a bundle-specific standard.

# What it still does not do

The keyless option removes key management, and PKCS #11 covers the case where you must hold a key.
Neither addresses the failure that matters most: a signature attests **who published**, so a
[compromised maintainer](/threats/maintainer-compromise.md) signs perfectly validly. Verification is
only meaningful pinned to an expected identity — `--identity` and `--identity-provider` are not
optional in spirit, whatever the CLI permits.

# Related

- [cosign](cosign.md) — signs a blob or image; different unit, same trust model
- [Sigstore](sigstore.md) — the keyless flow both rely on
- [ML-BOM](/bom-types/ml-bom.md) · [SPDX AI and Dataset profiles](/formats/spdx-ai-profile.md) —
  what you would sign *alongside*: the signature proves integrity, the BOM says what is inside
- [Maintainer compromise](/threats/maintainer-compromise.md) — what signing does not solve

[^model-transparency]: [sigstore/model-transparency](https://github.com/sigstore/model-transparency)
[^pypi]: [PyPI: model-signing](https://pypi.org/project/model-signing/)
[^nvidia-signing]: [NVIDIA: Signing agent skills](https://github.com/NVIDIA/skills/blob/main/docs/signing-agent-skills.mdx)
