---
type: Tool
title: syft
description: Anchore's SBOM generator — catalogs container images, filesystems and archives, emitting CycloneDX, SPDX or its own JSON.
resource: https://github.com/anchore/syft
tags:
  - tool
  - sbom
  - generation
  - anchore
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:33:36Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:33:36Z'
  - by: claude/opus-5
    at: '2026-09-04T13:00:00Z'
stale_after: 2027-01-04
sources:
  - id: syft-repo
    title: anchore/syft
    resource: https://github.com/anchore/syft
    last_modified: '2026-08-07'
  - id: syft-all-packages
    title: 'Syft docs — Supported package ecosystems'
    resource: https://oss.anchore.com/docs/capabilities/all-packages/
    last_modified: '2026-09-04'
---

The SBOM generator most of this landscape's tooling assumes. Apache-2.0, from Anchore.[^syft-repo]

| | |
|---|---|
| Scans | container images, filesystems, archives |
| Image formats | OCI, Docker, Singularity, "and more" |
| Emits | [CycloneDX](/formats/cyclonedx.md), [SPDX](/formats/spdx.md), Syft JSON, "and more" — the three named are not the whole list |
| Also does | conversion between SBOM formats; **signed SBOM attestations** |

# On the ecosystem count

syft's own README says it handles **"dozens of packaging ecosystems"** — apk, dpkg, RPM, Go,
Python, Java, JavaScript, Ruby, Rust, PHP, .NET "and many more" — and **publishes no exact
number**.[^syft-repo]

Recorded explicitly because a specific figure circulates in secondary sources and is not upstream's
claim. Cite "dozens" or count the catalogers yourself; do not repeat a number whose provenance you
cannot name.

**Counting them yourself is now a real option**: upstream publishes a *Supported package
ecosystems* table.[^syft-all-packages] It enumerates without totalling — the page states no
number anywhere — so it makes the count derivable while leaving the concept's rule intact. Derive
it against a named page and a date, or keep saying "dozens".

# Why the cataloger boundary matters

Coverage is per-ecosystem, and an ecosystem syft does not catalog produces **no components**, not
an error. A BOM generated over an uncatalogued tree is therefore empty rather than wrong-looking —
the same silent-absence failure as an unregistered [purl](/naming/purl.md) type, arriving one layer
earlier.

Adding coverage means contributing a cataloger. That is a real path rather than a theoretical one,
and it is why the parser boundary is worth knowing before trusting a generated inventory.

# It also signs what it generates

Beyond emitting a BOM, syft creates **signed SBOM attestations using the
[in-toto](/provenance/in-toto.md) specification**.[^syft-repo] That puts it on both sides of a
boundary this corpus otherwise keeps apart: the inventory and the signed statement *about* the
inventory. cdxgen's CDXA attestations are the counterpart in the other generator, so the choice
between them is not only about BOM-type breadth.

# Related

- [grype](grype.md) — consumes what syft emits; same authors
- [cdxgen](cdxgen.md) — the alternative generator, CycloneDX-native and broader across the xBOM family
- [Declaring BOM completeness](/formats/bom-completeness.md) — what a partial catalog should say about itself

[^syft-repo]: [anchore/syft](https://github.com/anchore/syft)
[^syft-all-packages]: [Syft docs — Supported package ecosystems](https://oss.anchore.com/docs/capabilities/all-packages/)
