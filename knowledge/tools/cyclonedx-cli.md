---
type: Tool
title: cyclonedx-cli
description: The BOM manipulation tool — convert, merge, diff, validate and sign CycloneDX documents.
resource: https://github.com/CycloneDX/cyclonedx-cli
tags:
  - tool
  - cyclonedx
  - bom
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:33:36Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:33:36Z'
stale_after: 2027-02-01
sources:
  - id: cyclonedx-cli-repo
    title: CycloneDX/cyclonedx-cli
    resource: https://github.com/CycloneDX/cyclonedx-cli
    last_modified: '2026-07-23'
---

Apache-2.0. Not a generator — it operates on BOMs that already exist.[^cyclonedx-cli-repo]

# Schema

| Subcommand | Purpose |
|---|---|
| `add files` | add files to a BOM |
| `analyze` | analyze a BOM file |
| `convert` | convert between BOM formats |
| `diff` | generate a BOM diff |
| `merge` | merge two or more BOMs |
| `validate` | validate a BOM |
| `keygen` | generate an RSA key pair for BOM signing |
| `sign bom` / `sign file` | sign a whole BOM, or an arbitrary file (PKCS1 RSA SHA256) |
| `verify all` / `verify file` | verify signatures |

Formats: `autodetect | csv | json | protobuf | spdxjson | xml`.
Spec versions: `v1_0` – `v1_7`, with `validate` defaulting to **v1.7**.

# Two things to know before using it

**Conversion is lossy.** Upstream says plainly that "converting between SPDX and CycloneDX formats
can result in the loss of some information", and notes limitations on CSV too. This is the concrete
cost behind treating SPDX as an *export target* rather than a second canonical representation:
convert at publish time for a consumer who requires it, rather than storing both and having to
decide which one is authoritative when they disagree.

**Its signing is not [Sigstore](/provenance/sigstore.md).** `keygen`/`sign`/`verify` here are
classic PKCS1 RSA with a key you generate and keep. That is a different trust model from keyless
signing bound to an OIDC identity, with different key-management obligations. Choose deliberately;
do not assume "signed" means the same thing across the two.

`merge` is the tooling half of [merging BOMs](/formats/bom-merging.md), and `diff` is what makes a
stored BOM corpus answerable over time.

# Related

- [Merging BOMs](/formats/bom-merging.md) — flat versus hierarchical, and why linking often beats merging
- [CycloneDX](/formats/cyclonedx.md) · [SPDX](/formats/spdx.md)
- [cosign](/provenance/cosign.md) — the other, keyless, signing path

[^cyclonedx-cli-repo]: [CycloneDX/cyclonedx-cli](https://github.com/CycloneDX/cyclonedx-cli)
