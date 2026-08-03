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
  - by: claude/opus-5
    at: '2026-08-03T11:20:00Z'
stale_after: 2027-02-01
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

The format is **not fixed yet**. Article 13(24) empowers the Commission, "by means of implementing
acts taking into account European or international standards and best practices", to "specify the
format and elements of the software bill of materials referred to in Part II, point (1), of
Annex I", under the examination procedure of Article 62(2).[^cra] Note *implementing* acts — the
delegated-act power in Article 13 concerns the support period, not the SBOM format.

Until one is adopted, "a commonly used and machine-readable format" is the only constraint — which
[CycloneDX](/formats/cyclonedx.md) and [SPDX](/formats/spdx.md) both plainly meet. **No implementing
act had been adopted as of 2026-08-03**, with the underlying European standard still in development
at CEN/CENELEC. That negative is the one claim here checked against secondary sources rather than
the enacting text, which cannot report its own absence — treat it as the item most likely to go
stale.

# Mandated, not published

The obligation to *draw up* an SBOM and the question of who *sees* it are separate, and the second
does not add up to disclosure:

| Recipient | Provision | Obligation |
|---|---|---|
| Nobody in particular | Annex I, Part II(1) | The SBOM must **exist**, as part of vulnerability handling |
| Market surveillance authority | **Annex VII, point 8** | Enters the technical documentation "where applicable, **further to a reasoned request** from a market surveillance authority provided that it is necessary in order for that authority to be able to check compliance"[^cra] |
| Market surveillance authority | Article 53 | A broader access-to-data route, also **upon a reasoned request**, covering design, development, production and vulnerability handling |
| The user | Annex II, point 9 | **Only if the manufacturer chooses to**: "If the manufacturer decides to make available the software bill of materials to the user, information on where the software bill of materials can be accessed"[^cra] |

Note that Annex VII is the *content of the technical documentation*, and its point 8 is where the
SBOM appears — conditioned on the request. Annex VIII is *Conformity Assessment Procedures* and says
nothing about SBOMs.

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

Article 71 states the rule for entry into force rather than the date, and gives the three
application dates directly — general application, then two exceptions, one for Article 14 and one
for Chapter IV (Articles 35 to 51).[^cra] All three are quoted in ISO form below; the Regulation
writes them day-then-month.

| Milestone | Date | Basis |
|---|---|---|
| Published in the Official Journal | 2024-11-20 | OJ reference |
| Entry into force | 2024-12-10 | **derived**: Article 71(1), the twentieth day following publication |
| Chapter IV — notification of conformity assessment bodies (Articles 35–51) | 2026-06-11 | Article 71(2) |
| Article 14 — reporting obligations of manufacturers | 2026-09-11 | Article 71(2) |
| General application | 2027-12-11 | Article 71(2) |

Only entry into force is derived rather than read; Article 71(1) states the twenty-day rule and the
date follows from the publication date.

These were once the perishable part of this concept, and its `stale_after` was set to fire before
the next milestone so a date would be re-checked before it passed. **That rule has done its job.**
All three dates are now verified against the enacting text and are fixed law; nothing about them
will change as 2026-09-11 passes. The volatility that remains is the **implementing act on SBOM
format**, which can land at any time, so the expiry now follows that instead.

**The ordering is the interesting part.** Reporting obligations bite over a year before the
Regulation applies generally, so the CRA's first practical effect on a manufacturer is *disclosure*,
not SBOM production.

# Related

- [SBOM](/bom-types/sbom.md) — what the document is, independent of who requires it
- [CycloneDX](/formats/cyclonedx.md) · [SPDX](/formats/spdx.md) — both meet "commonly used and machine-readable"
- [endoflife.date](/intelligence/endoflife-date.md) — support periods as data, which this makes obligatory to declare
- [HBOM](/bom-types/hbom.md) — "products with digital elements" is a hardware-inclusive scope

[^cra]: [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)
