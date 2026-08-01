---
type: Tool
title: cdxgen
description: The CycloneDX-native generator, and the only tool here that emits the whole xBOM family — HBOM, CBOM, OBOM, SaaSBOM and AI-BOM included.
resource: https://github.com/cdxgen/cdxgen
tags:
  - tool
  - sbom
  - generation
  - cyclonedx
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:33:36Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:33:36Z'
stale_after: 2026-12-01
sources:
  - id: cdxgen-repo
    title: cdxgen/cdxgen
    resource: https://github.com/cdxgen/cdxgen
    last_modified: '2026-08-01'
---

Apache-2.0, CycloneDX-native.[^cdxgen-repo] The reason to reach for it over
[syft](syft.md) is coverage of the **whole xBOM family**, not merely SBOM.

| | |
|---|---|
| Generates | SBOM, **HBOM**, **CBOM**, **OBOM**, **SaaSBOM**, **AI-BOM**, and CDXA attestations |
| Emits | CycloneDX JSON (primary native format); SPDX 3.0.1 JSON-LD |
| Spec versions | CycloneDX 1.5 – 1.7 |
| Inputs | a local filesystem path; a **git URL** it clones first; a **[purl](/naming/purl.md)** it resolves to source and then scans |

Resolving a purl straight to a scan is the unusual input. It makes the identifier an *address*
rather than only a label, which is closer to what [TEA](/distribution/tea.md) is reaching for at
the release level.

Accepted purl types for that path include `npm`, `pypi`, `gem`, `cargo`, `pub`, `github`,
`bitbucket`, `maven`, `composer` and `generic`.

# It moved organisation

The repository is now **`cdxgen/cdxgen`**; `CycloneDX/cdxgen` redirects. Recorded because a
redirect works today and pinned references do not always survive one — check any SHA-pinned action
or vendored URL that still names the old org.

# On the language count

Upstream states support for "many languages and container images" and **publishes no exact
count**.[^cdxgen-repo] As with [syft](syft.md), quote the qualitative claim rather than a number
whose source you cannot name.

# Related

- [syft](syft.md) — the alternative generator; narrower in BOM type, broader in image formats
- [CycloneDX](/formats/cyclonedx.md) — the format it is native to
- [Dependency-Track](dependency-track.md) — the usual destination for what it emits

[^cdxgen-repo]: [cdxgen/cdxgen](https://github.com/cdxgen/cdxgen)
