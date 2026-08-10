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
stale_after: 2026-12-01
sources:
  - id: syft-repo
    title: anchore/syft
    resource: https://github.com/anchore/syft
    last_modified: '2026-07-31'
---

The SBOM generator most of this landscape's tooling assumes. Apache-2.0, from Anchore.[^syft-repo]

| | |
|---|---|
| Scans | container images, filesystems, archives |
| Image formats | OCI, Docker, Singularity, "and more" |
| Emits | [CycloneDX](/formats/cyclonedx.md), [SPDX](/formats/spdx.md), Syft JSON |
| Also does | conversion between SBOM formats |

# On the ecosystem count

syft's own README says it handles **"dozens of packaging ecosystems"** — apk, dpkg, RPM, Go,
Python, Java, JavaScript, Ruby, Rust, PHP, .NET "and many more" — and **publishes no exact
number**.[^syft-repo]

Recorded explicitly because a specific figure circulates in secondary sources and is not upstream's
claim. Cite "dozens" or count the catalogers yourself; do not repeat a number whose provenance you
cannot name.

# Why the cataloger boundary matters

Coverage is per-ecosystem, and an ecosystem syft does not catalog produces **no components**, not
an error. A BOM generated over an uncatalogued tree is therefore empty rather than wrong-looking —
the same silent-absence failure as an unregistered [purl](/naming/purl.md) type, arriving one layer
earlier.

Adding coverage means contributing a cataloger. That is a real path rather than a theoretical one,
and it is why the parser boundary is worth knowing before trusting a generated inventory.

# Related

- [grype](grype.md) — consumes what syft emits; same authors
- [cdxgen](cdxgen.md) — the alternative generator, CycloneDX-native and broader across the xBOM family
- [Declaring BOM completeness](/formats/bom-completeness.md) — what a partial catalog should say about itself

[^syft-repo]: [anchore/syft](https://github.com/anchore/syft)
