---
type: Specification
title: SBOM Minimum Elements (2026)
description: The floor for what counts as an SBOM in US federal procurement — 17 data fields as of the 2026 edition, which replaced the 2021 NTIA original.
resource: https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom
tags:
  - regulation
  - us
  - sbom
  - procurement
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-02T08:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-02T08:05:00Z'
stale_after: 2027-02-01
sources:
  - id: cisa-2026
    title: 2026 Minimum Elements for a Software Bill of Materials (SBOM)
    resource: https://www.cisa.gov/sites/default/files/2026-07/2026_cisa_sbom_minimum_elements_508c.pdf
---

**2026 Minimum Elements for a Software Bill of Materials (SBOM)**, published 2026-07-29 by CISA with
the NSA, FBI and sixteen international partner agencies.[^cisa-2026]

> **This is guidance, not law.** It defines what a document must contain to count as an SBOM; it
> does not itself oblige anyone to produce one. Its force is procurement — it is the successor
> guidance to the 2021 NTIA minimum elements that OMB memorandum M-22-18 designated CISA to
> produce.[^cisa-2026] Whether it binds you is a contractual question, not one this corpus answers.

**It replaced the 2021 NTIA document.** If you have a reference to "the NTIA minimum elements", it
points at a superseded edition. The 2026 document states it "updated the Minimum Elements … to
reflect current SBOM needs, while preserving the core principles of the document published in 2021
by the National Telecommunications and Information Administration".[^cisa-2026]

# The 17 data fields

Split into SBOM metadata — facts about the document — and component data, facts about what it
describes.[^cisa-2026]

| About the document | About each component |
|---|---|
| SBOM Author | Component Name |
| SBOM Author Signature | Component Producer |
| SBOM Data Format Name | Component Version |
| SBOM Data Format Version | Component Identifiers |
| SBOM Generation Context | Component License |
| SBOM Timestamp | Component Hash Algorithm |
| SBOM Tool Name | Component Hash Value |
| SBOM Tool Version | Component Dependency Relationship |
| SBOM Version | |

**Component License** should carry [SPDX license identifiers](/licensing/spdx-license-list.md) where
possible, or otherwise indicate where full licence details can be found — including the existence of
proprietary conditions.[^cisa-2026]

# Practices and processes

Six named elements, covering "how an entity engages with and documents the SBOM
data":[^cisa-2026] Frequency, Depth, Known Unknowns, Distribution and Delivery, Accommodation of
Mistakes, and Machine-Processable Data.

The document is explicit that these do not map one-to-one onto format fields: "an implemented data
field may satisfy one or more of the minimum elements", and "SBOM data formats may also use
different field names".[^cisa-2026] Conformance is a property of the information present, not of
field names matching.

# What changed from 2021

The count roughly doubled — the 2021 edition named seven data fields. Beyond additions, three
changes alter meaning rather than coverage:[^cisa-2026]

- **Supplier Name became Component Producer.** The document says plainly why: Supplier Name "has
  proven ambiguous in practice, particularly around distributors of software", and that "some
  ambiguity will remain until there is a consensus methodology for identifying entities". An
  admission, not a fix.
- **Automation Support became Machine-Processable Data** and moved out of the data fields into
  practices, with **SWID tags dropped** from the list of data formats as "not a widely used" format.
- **Access Controls was removed as an element**, its considerations folded into Distribution and
  Delivery.

# The instruction worth carrying elsewhere

On Component Producer, where no producer can be determined:

> the SBOM author should explicitly indicate that the component is of unknown provenance to
> acknowledge the lack of traceability[^cisa-2026]

**A gap must be declared, not left implied.** An SBOM that silently omits a producer is
indistinguishable from one whose producer is known, and the reader cannot tell which they hold. The
same principle appears as [BOM completeness](/formats/bom-completeness.md) in CycloneDX and as
[declared versus concluded](/licensing/declared-vs-concluded.md) licensing — absence of a finding is
not a finding of absence, and a document that cannot say so is misleading by construction.

# Related

- [SBOM](/bom-types/sbom.md) — the artifact this sets a floor for
- [EU Cyber Resilience Act](cra.md) — the other side of the same demand, and a *lower* content floor: top-level dependencies only
- [purl](/naming/purl.md) · [CPE](/naming/cpe.md) — what Component Identifiers are drawn from
- [SPDX license list](/licensing/spdx-license-list.md) — the recommended source for Component License

[^cisa-2026]: [2026 Minimum Elements for a Software Bill of Materials (SBOM)](https://www.cisa.gov/sites/default/files/2026-07/2026_cisa_sbom_minimum_elements_508c.pdf)
