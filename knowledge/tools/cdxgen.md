---
type: Tool
title: cdxgen
description: The CycloneDX-native generator, and the only tool here that emits the whole xBOM family — HBOM, CBOM, OBOM, SaaSBOM and AI-BOM included. Each type has its own scope, and two of them only inspect the live host.
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
  - by: claude/opus-5
    at: '2026-09-04T12:40:00Z'
stale_after: 2027-01-04
sources:
  - id: cdxgen-repo
    title: cdxgen/cdxgen
    resource: https://github.com/cdxgen/cdxgen
    last_modified: '2026-09-04'
  - id: cdxgen-readme
    title: 'cdxgen/cdxgen — README: supported BOM formats, HBOM and OBOM generation'
    resource: https://github.com/cdxgen/cdxgen/blob/master/README.md
    last_modified: '2026-09-04'
---

Apache-2.0, CycloneDX-native.[^cdxgen-repo] The reason to reach for it over
[syft](syft.md) is coverage of the **whole xBOM family**, not merely SBOM.

| | |
|---|---|
| Generates | SBOM, **HBOM**, **CBOM**, **OBOM**, **SaaSBOM**, **AI-BOM**, CDXA attestations, and [VDR](/intelligence/vdr.md) in combination with OWASP depscan |
| Emits | CycloneDX JSON (primary native format); SPDX 3.0.1 JSON-LD |
| Spec versions | targets CycloneDX **1.6, 1.7 and 2.0**; output downgradable to 1.4 or 1.5 for legacy consumers |
| Inputs | a local filesystem path; a **git URL** it clones first; a **[purl](/naming/purl.md)** it resolves to source and then scans; for two types, **the live host** |

Resolving a purl straight to a scan is the unusual input. It makes the identifier an *address*
rather than only a label, which is closer to what [TEA](/distribution/tea.md) is reaching for at
the release level.

Accepted purl types for that path include `npm`, `pypi`, `gem`, `cargo`, `pub`, `github`,
`bitbucket`, `maven`, `composer` and `generic`.

# Each BOM type has its own scope, and the list is not uniform

"Generates the whole family" is true and misleading on its own. Each type is supported over a
different, narrower input set, and two of them do not scan an artifact at all.[^cdxgen-readme]

| Type | What it is generated from |
|---|---|
| SBOM | "many languages and container images" |
| HBOM | **supported live hosts only** — "Apple Silicon macOS and Linux amd64/arm64 systems" |
| OBOM | **Linux container images, and VMs running Linux or Windows** |
| CBOM | Java keystores and certificates; JavaScript and TypeScript source-level algorithm inventory |
| SaaSBOM | Java, Python, JavaScript, TypeScript and PHP projects |
| AI-BOM | prompt files, AI services, MCP configs and model metadata |

The practical consequence: **you cannot ask cdxgen for an HBOM of an arbitrary repository or
image.** Hardware inventory is host introspection, so the machine you run it on is the machine you
get an answer about — and on Intel macOS or Windows you get none.

# How the host-scoped types are actually generated

Neither is a flag on the main scanner. Each is its own subcommand.[^cdxgen-readme]

```shell
hbom -o hbom.json                                     # the current host
obom -o obom.json --deep --bom-audit                  # a live system or VM
```

`obom` is **an alias for `cdxgen -t os`**, so OBOM is a project *type* rather than a separate
engine. `hbom` carries its own diagnostics: `hbom --dry-run` previews read-only, `hbom
diagnostics` reports missing utilities before a full collection, and `hbom --include-runtime`
merges the hardware view with runtime evidence. Elevated privileges may be required.

**OBOM is powered by [osquery](https://www.osquery.io/)**, installed alongside the binary
plugins — which is the answer to how a JavaScript tool inventories an operating system. It does
not: it queries osquery with platform-specific default queries and enriches the result. An
optional `trustinspector` helper adds macOS code-signing, team ID and notarization metadata, and
Windows Authenticode signer and timestamp metadata. On macOS "some macOS tables require elevated
privileges and Full Disk Access".[^cdxgen-readme]

That dependency is worth recording for its own sake: an OBOM's completeness is bounded by
osquery's coverage and by the privileges the collector was granted, not by cdxgen alone.

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
- [HBOM](/bom-types/hbom.md) and [OBOM](/bom-types/obom.md) — the two types whose scope is a host

[^cdxgen-repo]: [cdxgen/cdxgen](https://github.com/cdxgen/cdxgen)
[^cdxgen-readme]: [cdxgen/cdxgen — README](https://github.com/cdxgen/cdxgen/blob/master/README.md)
