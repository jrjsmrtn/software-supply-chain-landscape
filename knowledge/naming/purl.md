---
type: Identifier
title: purl (Package URL)
description: The canonical identifier for a software package, derived from where the artifact came from rather than negotiated.
resource: https://github.com/package-url/purl-spec
tags:
  - identifier
  - join-key
  - ecma-427
  - naming
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:27:17Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:05:00Z\'
stale_after: 2027-08-01
sources:
  - id: purl-spec
    title: Package URL specification
    resource: https://github.com/package-url/purl-spec
  - id: ecma-427
    title: 'ECMA-427: Package URL (purl) specification'
    resource: https://www.ecma-international.org/publications-and-standards/standards/ecma-427/
  - id: tc54-tg2
    title: Ecma TC54-TG2
    resource: https://ecma-international.org/task-groups/tc54-tg2
  - id: type-definitions
    title: purl type definitions
    resource: https://github.com/package-url/purl-spec/tree/main/types
  - id: ansible-definition-snapshot
    title: Vendored snapshot of a proposed purl type definition (purl-spec#854)
    resource: https://github.com/package-url/purl-spec/pull/854
    last_modified: '2026-07-31'
---

A BOM lists components, but a component must be *named*. `django 4.2` is not an identifier —
which registry, which distribution, which architecture, the PyPI package or a Debian rebuild of
it? purl is the string that settles it, and it is **derivable** from the package coordinates
rather than assigned from a dictionary.[^purl-spec]

This is the join key. An SBOM records purls, vulnerability databases key on purls, and a scanner
joining "what I have" to "what is known bad" performs a lookup instead of fuzzy string matching.
Nothing else in the supply-chain landscape composes without it.

# Schema

```
pkg:type/namespace/name@version?qualifiers#subpath
```

| Segment | Required | Notes |
|---|---|---|
| `type` | yes | the package ecosystem — selects the naming rules for everything after it |
| `namespace` | no | type-specific: group, org, distro vendor |
| `name` | yes | package name |
| `version` | no | version string, or a digest for content-addressed types |
| `qualifiers` | no | `key=value` pairs — architecture, repository URL, distro |
| `subpath` | no | path within the package |

The grammar is **universal**: a per-type definition constrains which segments are required, how
they normalise, and which qualifiers are permitted, but cannot alter the syntax
above.[^type-definitions]

# Examples

```
pkg:pypi/django@4.2
pkg:npm/lodash@4.17.21
pkg:hex/phoenix@1.7.14
pkg:cargo/serde@1.0.197
pkg:golang/github.com/gorilla/mux@v1.8.0
pkg:maven/org.apache.commons/commons-lang3@3.14.0
pkg:deb/debian/curl@7.50.3-1?arch=i386
pkg:oci/postgres@sha256:abc123?repository_url=docker.io/library
pkg:github/jrjsmrtn/c4-skills@v0.1.0
```

# Standardization

**ECMA-427**, via Ecma TC54 task group TG2.[^ecma-427][^tc54-tg2] ISO standardization was in
progress at the time this concept was written — the status is the perishable part of this
document and the reason for its `stale_after` date.

# Types are registered; the grammar does not enforce that

`type` is the only segment that is not free-form. Types are registered in the purl-spec
repository, each as a machine-readable definition (`types/<type>-definition.json`, conforming to
`purl-type-definition.schema-1.0.json`) declaring per-segment requirement and case-sensitivity,
permitted qualifiers, and canonical examples.[^type-definitions][^ansible-definition-snapshot]

The schema name above was checked against a real definition file rather than taken from prose: the
`ansible-definition.json` snapshot vendored in `ansible-bom` declares
`$schema: purl-type-definition.schema-1.0.json`, confirming both the schema identifier and the
per-segment structure.[^ansible-definition-snapshot]

**The trap is that the grammar accepts any type string.** `pkg:whatever/foo@1.0` parses cleanly
and passes BOM schema validation; nothing rejects it. Consumers that key on type then return an
**empty result rather than an error** — a component with an unregistered type reports no known
vulnerabilities, indistinguishable in the output from one that genuinely has none. This is the
concrete reason a BOM with wrong identifiers is worse than no BOM.

Producing identifiers for an ecosystem with no registered type is a distinct practice — see
[Provisional identifiers for unregistered purl types](/naming/provisional-purl-identifiers.md).

# Related

- [CPE](/naming/cpe.md) — the older identifier, naming IT *products* rather than packages
- [purl type definitions](/naming/purl-type-definitions.md) — the registry mechanics
- [OSV IDs](/naming/osv-ids.md) — OSV records key on purl
- [osv.dev](/intelligence/osv-dev.md) — keys its records on purl
- [endoflife.date](/intelligence/endoflife-date.md) — maps purl and CPE, so lifecycle data joins on
  the same key

[^purl-spec]: [Package URL specification](https://github.com/package-url/purl-spec)
[^ecma-427]: [ECMA-427](https://www.ecma-international.org/publications-and-standards/standards/ecma-427/)
[^tc54-tg2]: [Ecma TC54-TG2](https://ecma-international.org/task-groups/tc54-tg2)
[^type-definitions]: [purl type definitions](https://github.com/package-url/purl-spec/tree/main/types)
[^ansible-definition-snapshot]: [purl-spec#854](https://github.com/package-url/purl-spec/pull/854), vendored snapshot
