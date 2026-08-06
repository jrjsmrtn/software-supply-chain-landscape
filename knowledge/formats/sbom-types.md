---
type: Practice
title: The six SBOM types
description: Design, Source, Build, Analyzed, Deployed and Runtime — where an SBOM's data came from, which decides what it can be trusted to say. Two SBOMs for one artifact can disagree and both be correct.
resource: https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf
tags:
  - sbom
  - provenance
  - tooling
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-06T21:40:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-06T21:40:00Z'
stale_after: 2027-08-01
sources:
  - id: cisa-types
    title: 'Types of Software Bill of Material (SBOM) Documents (CISA, 2023-04-21)'
    resource: https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf
  - id: cdx-schema
    title: 'CycloneDX bom-1.6.schema.json — metadata.lifecycles'
    resource: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.6.schema.json
---

An SBOM says what a thing is made of. **How the data was obtained decides what that claim is worth**,
and a 2023 document facilitated by CISA names six ways it is obtained.[^cisa-types] This is a
different axis from the [xBOM family](/bom-types/index.md): those distinguish *what is inventoried*,
these distinguish *where the inventory came from*.

# The six types

| Type | Data comes from | Also called |
|---|---|---|
| **Design** | a design specification, RFP or initial concept — components that may not yet exist | |
| **Source** | the development environment and source files, typically via SCA tooling | |
| **Build** | the build process itself, from source, dependencies and build-time ephemeral data | |
| **Analyzed** | inspection of the finished artifact — executables, packages, containers, VM images | **3rd party** |
| **Deployed** | what is installed on a system, including configuration | |
| **Runtime** | instrumenting the running system, capturing dynamically loaded components and external call-outs | **Instrumented**, **Dynamic** |

**A document may combine several.** The specification says so explicitly for Build, which "may consist
of integrated intermediate Build and Source SBOMs for a final release artifact SBOM".[^cisa-types] So
"which type is this?" can have more than one answer.

# It is not a lifecycle taxonomy, and the document says so

The ordering above invites reading these as stages of a pipeline. The document forecloses that in its
second paragraph:

> This list of SBOM types is **not intended to be tightly tied to the software lifecycle**. Some SBOM
> types may be available and useful across multiple lifecycle phases, while others may be available
> only in one lifecycle phase.[^cisa-types]

The distinction is not pedantry. If the types were lifecycle stages, a later one would supersede an
earlier one and you would keep the newest. They are not, so **a Runtime SBOM does not replace a Source
SBOM** — it answers a different question, and the Source SBOM still answers its own.

# What each type cannot tell you

The limitations are the operationally useful half, and each is a specific way a technically-correct
SBOM misleads:[^cisa-types]

- **Source** can list components "that never run or are compiled out in deployed code", and depending
  on the ecosystem may omit runtime, plugin or dynamic components entirely. A vulnerability in a
  compiled-out component is a finding you will spend time on for nothing.
- **Build** "may not contain the correct versions of dynamically linked dependencies, as they may be
  replaced at runtime". The build knows what it linked against, not what will load.
- **Analyzed** "may be prone to omissions, errors, or approximations if the tool is unable to
  decompose or recognize the software components precisely", and "may depend on heuristics". This is
  the type produced when you scan someone else's binary — the common case, and the least reliable.
- **Deployed** "may not accurately reflect the software's runtime environment, as components may
  reside in inaccessible code".
- **Runtime** sees only what has actually executed: detail "may be available only after the system has
  run for a period of time until the complete functionality has been exercised". An unexercised code
  path is an absent component.
- **Design** is "very difficult to generate" and "unlikely to identify as much detail" than the rest.

**So two SBOMs for the same artifact can disagree while both being accurate.** A Source SBOM listing a
component the Runtime SBOM omits is not a contradiction to reconcile — it is one document reporting
what was available to link and the other reporting what was loaded. Treating the difference as an
error, and "fixing" it, destroys the information.

# Declaring the type in a CycloneDX document

The taxonomy is prose; **CycloneDX carries a field for it**. `metadata.lifecycles` exists to
"communicate the stage(s) in which data in the BOM was captured", and takes either a predefined
`phase` or a custom `name` with an optional `description`.[^cdx-schema] It is an array, which matches
the CISA document's point that one SBOM may combine types.

**The two vocabularies do not align, and neither is a subset of the other:**

| CISA type | Nearest `phase` |
|---|---|
| Design | `design` |
| Source | `pre-build` |
| Build | `build` |
| Analyzed | `post-build` |
| **Deployed** | `operations` |
| **Runtime** | `operations` — *the same value* |
| — | `discovery`, `decommission` — no CISA equivalent |

Seven phases, six types, and **the distinction that matters most collapses**: Deployed and Runtime
both land on `operations`. A Deployed SBOM lists what is installed; a Runtime SBOM lists what actually
loaded — which is precisely the difference a consumer needs when deciding whether an unexercised
component counts. `phase` cannot express it.

Where that precision matters, use the custom form instead:

```json
"metadata": {
  "lifecycles": [
    { "name": "Runtime", "description": "Captured by instrumenting the running system (CISA SBOM type)" }
  ]
}
```

**Declaring nothing is the common case and the worst one.** A document with no `lifecycles` leaves the
consumer to infer the type from the tool that produced it, which requires knowing the tool. Emitting
even the approximate `phase` is better than silence — and unlike
[`compositions`](/formats/bom-completeness.md), which says what a BOM *left out*, this says how what
it *contains* was obtained. The two answer different halves of "how much should I trust this".

# Provenance of the document itself

Worth knowing before citing it as authority:

- **"It is not an official US government document."**[^cisa-types] It was drafted by a community-led
  working group on SBOM Tooling and Implementation that CISA *facilitated*, with drafting led by Kate
  Stewart (Linux Foundation) and Melissa Rhodes (Medtronic). "CISA says" overstates it; "CISA
  published" is right.
- It is **TLP:CLEAR**, so it may be redistributed without restriction.
- Its footnote 1 anchors "minimum content" to the **2021 NTIA minimum elements** — an edition since
  replaced. See [the 2026 minimum elements](/regulation/sbom-minimum-elements.md); this taxonomy rests
  on a baseline that has moved beneath it, without invalidating the six types themselves.
- It anticipates its own expansion, naming VEX, service dependencies and "SBOM of SBOMs" as pressures
  that "may require additional types of SBOMs".

# Related

- [SBOM](/bom-types/sbom.md) — what the document inventories, independent of how it was produced
- [Minimum elements](/regulation/sbom-minimum-elements.md) — what it must *contain*, a separate axis again
- [BOM completeness](/formats/bom-completeness.md) — how a document declares what it left out, which
  is how a type's limitation gets stated inside the document rather than assumed by the reader

[^cdx-schema]: [CycloneDX bom-1.6.schema.json](https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.6.schema.json)
[^cisa-types]: [Types of Software Bill of Material (SBOM) Documents (CISA, 2023-04-21)](https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf)
