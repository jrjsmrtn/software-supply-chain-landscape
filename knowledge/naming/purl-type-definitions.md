---
type: Specification
title: purl type definitions
description: The per-type registry that constrains how a purl's segments are interpreted, without altering the grammar.
resource: https://github.com/package-url/purl-spec/tree/main/types
tags:
  - identifier
  - registry
  - naming
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:45:00Z'
  - by: claude/opus-5
    at: '2026-09-09T09:00:00Z'
stale_after: 2027-03-09
sources:
  - id: type-definitions
    title: purl type definitions directory
    resource: https://github.com/package-url/purl-spec/tree/main/types
  - id: swid-definition
    title: 'purl-spec: swid type definition'
    resource: https://github.com/package-url/purl-spec/blob/main/types/swid-definition.json
  - id: ansible-definition-snapshot
    title: 'purl-spec#854: proposed `ansible` type definition (vendored snapshot)'
    resource: https://github.com/package-url/purl-spec/pull/854
    last_modified: '2026-07-31'
---

`type` is the only segment of a [purl](purl.md) that is not free-form: it selects the naming rules
for everything after it. Types are **registered**, in the `package-url/purl-spec`
repository.[^type-definitions]

Each registered type has a machine-readable definition at `types/<type>-definition.json`,
conforming to `purl-type-definition.schema-1.0.json`. A definition declares, per segment, whether
it is required, whether it is case-sensitive, and how it normalises; lists the permitted
qualifiers; and publishes canonical examples.

**It never declares syntax.** The purl grammar is universal, and a type definition cannot alter
it — only constrain how its segments are filled.

The schema identifier and per-segment structure above were checked against a real definition file
rather than taken from prose: the `ansible-definition.json` snapshot vendored in `ansible-bom`
declares `$schema: purl-type-definition.schema-1.0.json`.[^ansible-definition-snapshot]

# Schema

Fields a type definition carries:

| Key | Purpose |
|---|---|
| `type`, `type_name`, `description` | the type's identity |
| `repository` | default repository URL and whether one applies |
| `namespace_definition` | requirement, case sensitivity, native name, normalisation note |
| `name_definition` | as above, for the name segment |
| `version_definition` | as above, for the version segment |
| `qualifiers_definition` | list of permitted qualifiers, each with a requirement |
| `subpath_definition` | as above, for the subpath segment |
| `examples` | canonical purls for the type |
| `note` | free-form remarks about the type |
| `reference_urls` | upstream documentation |

# Why the examples matter

The published `examples` are the useful part for an implementer: they are **executable
expectations rather than prose**, so an implementation can be tested against upstream directly
instead of against someone's reading of upstream. A round-trip test over the examples fails when
either side moves.

**42 types are registered as of 2026-09-09**, unchanged since 2026-08-02 — counted from the
directory listing, discounting its `README.md`. Two matter for this bundle's AI material:
`huggingface` and `mlflow` — models are nameable with a purl, so an [ML-BOM](/bom-types/ml-bom.md)
joins to vulnerability and lifecycle data on the same key as everything else. `ansible` is **not**
among them, which is why [provisional identifiers](provisional-purl-identifiers.md) exists.

A new type arrives by pull request. Review is on human timescales and can stall — see
[Provisional identifiers for unregistered purl types](provisional-purl-identifiers.md).

# `swid`, the type that breaks the mental model

Most purl types identify a package by **namespace, name and version**, resolved against a
repository. `swid` does neither, and it is worth knowing about precisely because it is the
counter-example.[^swid-definition]

It is the purl type for **ISO/IEC 19770-2 Software Identification (SWID) tags**. Its definition
sets `use_repository: false` — *"There is no default package repository"* — and the identifying
information lives in **qualifiers** rather than in the path segments:

```
pkg:swid/Fedora@29?tag_id=org.fedoraproject.Fedora-29
```

`tag_id` is what actually names the thing; `tag_version`, `patch`, `tag_creator_name` and
`tag_creator_regid` complete it. The segments map onto the tag's own fields — namespace onto
`softwareCreator`, name onto `SoftwareIdentity/name`, version onto `SoftwareIdentity/version` —
so a `pkg:swid` purl is a **re-encoding of an existing identifier**, not a coordinate in a registry.

Two consequences follow. There is nothing to resolve it against, so the silent-absence failure
[purl](purl.md) describes has a different shape here: the question is not whether a registry
answers, but whether anyone issued a tag at all. And it means a purl `type` does not imply a
fetchable location — an assumption easy to carry over from `npm` or `pypi` and wrong here.

⚠ **Its standing is contested across this bundle's own sources.** purl registers it and
[TEI](/distribution/tea.md) accepts `swid` as an identifier type, while the
[2026 SBOM minimum elements](/regulation/sbom-minimum-elements.md) **dropped SWID tags** from its
data formats as "not a widely used" format. Both are current. Registered is not the same as
adopted, and this is the clearest case of the gap in the corpus.

# Related

- [purl](purl.md) — the identifier these definitions constrain
- [Provisional identifiers for unregistered purl types](provisional-purl-identifiers.md)

[^type-definitions]: [purl type definitions](https://github.com/package-url/purl-spec/tree/main/types)
[^ansible-definition-snapshot]: [purl-spec#854](https://github.com/package-url/purl-spec/pull/854), vendored snapshot
[^swid-definition]: [purl-spec: `swid` type definition](https://github.com/package-url/purl-spec/blob/main/types/swid-definition.json)
