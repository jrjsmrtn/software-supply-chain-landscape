---
type: Practice
title: Declaring BOM completeness (`compositions`)
description: CycloneDX's mechanism for saying a BOM is not exhaustive — without it, a partial BOM is indistinguishable from a complete one.
resource: https://cyclonedx.org/use-cases/compositions-dependencies/
tags:
  - bom
  - cyclonedx
  - practice
  - completeness
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:00:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:05:00Z\'
stale_after: 2027-08-01
sources:
  - id: cyclonedx-compositions
    title: 'CycloneDX: Compositions and Dependencies'
    resource: https://cyclonedx.org/use-cases/compositions-dependencies/
---

**Partial BOMs lie by default.** A BOM that omits transitive dependencies is byte-indistinguishable
from one that has none — both are just a list. `compositions` is the CycloneDX field that lets a
document say which it is.[^cyclonedx-compositions]

If you generate partial BOMs and leave it unset, you are publishing a false claim of completeness.
That is not a nuance; it is the difference between an inventory and a misleading one.

# Schema

`aggregate` values:

| Value | Meaning |
|---|---|
| `complete` | every component is accounted for |
| `incomplete` | known to be missing components |
| `incomplete_first_party_only` | first-party components enumerated, third-party not |
| `incomplete_first_party_proprietary_only` | first-party proprietary only |
| `incomplete_first_party_opensource_only` | first-party open-source only |
| `incomplete_third_party_only` | third-party components enumerated, first-party not |
| `incomplete_third_party_proprietary_only` | third-party proprietary only |
| `incomplete_third_party_opensource_only` | third-party open-source only |
| `unknown` | completeness not determined |
| `not_specified` | no assertion made |

Read from `bom-1.7.schema.json`. An earlier revision listed six of the ten and omitted the
proprietary/open-source splits, which are what let a BOM say *we enumerated our open-source
dependencies and not our commercial ones* — a common and honest position.

Note that `unknown` and `not_specified` are different claims: the first says nobody determined it,
the second declines to assert anything. Neither is the same as `complete`, and a consumer that
treats a missing `compositions` block as `complete` is making that mistake on your behalf.

# Practice

Set it whenever the generator cannot see the whole graph — vendored trees, a scanner run against a
built artifact rather than a source tree, or an ecosystem the cataloguer does not cover. A
generator that cannot enumerate something should say so rather than omit silently.

This is the format-level companion to declaring vulnerability-coverage status in scan output: in
both cases, the failure mode is an absence that reads as an assurance.

# Related

- [CycloneDX](cyclonedx.md) — the format this belongs to
- [Merging BOMs](bom-merging.md) — merging partial BOMs is the other half of this problem
- [BOM-Link](/naming/bom-link.md) — referencing rather than inlining, which sidesteps it

[^cyclonedx-compositions]: [CycloneDX compositions and dependencies](https://cyclonedx.org/use-cases/compositions-dependencies/)
