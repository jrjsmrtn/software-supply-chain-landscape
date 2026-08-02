---
type: Regulation
title: EU Cyber Resilience Act
description: Regulation (EU) 2024/2847 — the first instrument to make an SBOM a legal obligation, with a floor lower than most readers assume and no duty to publish it.
resource: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
tags:
  - regulation
  - eu
  - sbom
  - support-period
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-02T07:40:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-02T07:40:00Z'
stale_after: 2026-09-01
sources:
  - id: cra
    title: Regulation (EU) 2024/2847 (Cyber Resilience Act)
    resource: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
---

**Regulation (EU) 2024/2847**, on horizontal cybersecurity requirements for products with digital
elements. It is the instrument that turns "you should have an SBOM" into "you must produce
one".[^cra]

> **This describes what the Regulation requires of a document. It does not say whether the
> Regulation applies to you** — that depends on the product, the role you occupy in the supply
> chain, and where it is placed on the market. Those are legal questions and this is not legal
> advice.

# What it requires

An SBOM is defined in Article 3(39) as "a formal record containing details and supply chain
relationships of components included in the software elements of a product with digital
elements".[^cra]

The obligation itself is in **Annex I, Part II, point (1)** — the vulnerability-handling
requirements. Manufacturers shall:

> identify and document vulnerabilities and components contained in products with digital elements,
> including by drawing up a software bill of materials in a commonly used and machine-readable
> format covering **at the very least the top-level dependencies** of the products[^cra]

**That floor is lower than most readers expect.** The Regulation mandates top-level dependencies,
not the transitive graph. Everything the rest of this corpus says about deep dependency analysis is
good practice, not CRA compliance — and a document that satisfies the Regulation may say very little
about where a vulnerability actually entered.

The format is **not fixed yet**. Article 13(24) empowers the Commission to specify "the format and
elements" of the SBOM by implementing act, taking account of European or international standards.
Until one is adopted, "a commonly used and machine-readable format" is the only constraint — which
[CycloneDX](/formats/cyclonedx.md) and [SPDX](/formats/spdx.md) both plainly meet.

# Mandated, not published

Three separate provisions govern who sees the document, and they do not add up to disclosure:

| Recipient | Provision | Obligation |
|---|---|---|
| Technical documentation | Annex VII | The SBOM is part of the vulnerability-handling information the manufacturer must hold |
| Market surveillance authority | Annex VIII, point 8 | Provided **on reasoned request**, where necessary to check compliance |
| The user | Annex II, point 9 | **Only if the manufacturer chooses to.** If they do, they must say where it can be accessed |

So the CRA compels an SBOM to *exist* and to be *producible on demand*. It does not compel
publication to customers, and Annex II point 9 makes that explicitly optional. A reader expecting
the Regulation to make SBOMs generally available will not find that here.

# The support period

Article 13(8) requires manufacturers to handle vulnerabilities "for the support period", defined in
Article 3 as the period during which the manufacturer must handle vulnerabilities in accordance with
Annex I Part II.[^cra]

It is determined by how long the product "is expected to be in use", accounting for reasonable user
expectations and the nature of the product — and then floored: **"the support period shall be at
least five years"**. With a carve-out that is routinely dropped in summaries: where the product is
expected to be in use for *less* than five years, the support period matches the expected use
time.[^cra]

This is the provision that converts [end-of-life dates](/intelligence/endoflife-date.md) from a
planning signal into a declared, bounded commitment.

# Dates

Article 71 states the rule for entry into force rather than the date, and gives the application
dates directly.[^cra] **These are the perishable part of this concept**, and this concept's
`stale_after` is set to expire *before* the next milestone rather than after it — an expiry that
fires once a date has already passed is checking the wrong thing.

| Milestone | Date | Basis |
|---|---|---|
| Published in the Official Journal | 2024-11-20 | OJ reference |
| Entry into force | 2024-12-10 | **derived**: Article 71(1), the twentieth day following publication |
| Chapter IV — notification of conformity assessment bodies (Articles 35–51) | 2026-06-11 | Article 71(2) |
| Article 14 — reporting obligations of manufacturers | 2026-09-11 | Article 71(2) |
| General application | 2027-12-11 | Article 71(2) |

Only entry into force is derived rather than read; Article 71(1) states the twenty-day rule and the
date follows from the publication date.

**The ordering is the interesting part.** Reporting obligations bite over a year before the
Regulation applies generally, so the CRA's first practical effect on a manufacturer is *disclosure*,
not SBOM production.

# Related

- [SBOM](/bom-types/sbom.md) — what the document is, independent of who requires it
- [CycloneDX](/formats/cyclonedx.md) · [SPDX](/formats/spdx.md) — both meet "commonly used and machine-readable"
- [endoflife.date](/intelligence/endoflife-date.md) — support periods as data, which this makes obligatory to declare
- [HBOM](/bom-types/hbom.md) — "products with digital elements" is a hardware-inclusive scope

[^cra]: [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)
