---
type: Organization
title: CISA
description: The US agency behind KEV, the SBOM minimum elements and the VEX status justifications — and the reason "CISA published" and "CISA requires" are different claims about the same body.
resource: https://www.cisa.gov/
tags:
  - organization
  - us
  - vulnerability
  - sbom
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-06T22:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-06T22:05:00Z'
stale_after: 2027-02-01
sources:
  - id: bod-22-01
    title: 'BOD 22-01: Reducing the Significant Risk of Known Exploited Vulnerabilities'
    resource: https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities
  - id: cisa-types
    title: 'Types of Software Bill of Material (SBOM) Documents (CISA, 2023-04-21)'
    resource: https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf
  - id: kev-schema
    title: 'CISA Catalog of Known Exploited Vulnerabilities — JSON Schema'
    resource: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities_schema.json
---

The **Cybersecurity and Infrastructure Security Agency**, a US federal body whose outputs this corpus
depends on in four separate places. It is named here not for what it is but because **its documents
carry very different weight from one another**, and citing them interchangeably is a common error.

# The authority gradient

The single most useful thing to know about a CISA artifact is which of these it is:

| Artifact | What CISA did | Binding on whom |
|---|---|---|
| **[KEV catalog](#kev-the-known-exploited-vulnerabilities-catalog)** (BOD 22-01) | issued a directive and manages the catalog | **US federal civilian executive branch agencies**, with deadlines[^bod-22-01] |
| **[SBOM minimum elements](/regulation/sbom-minimum-elements.md)** | authored the 2026 edition, designated to do so by OMB M-22-18 | procurement, indirectly |
| **[VEX status justifications](/intelligence/vex.md)** | published community working-group output | nobody — it is a vocabulary |
| **[The six SBOM types](/formats/sbom-types.md)** | *facilitated* a community working group | nobody, and it says so |

That last row is the sharp one. The SBOM types document states outright: **"It is not an official US
government document."**[^cisa-types] It was drafted by a community-led working group that CISA
convened, with drafting led by people from the Linux Foundation and Medtronic. **"CISA published" is
accurate; "CISA requires" is true only of the first row.**

# KEV: the Known Exploited Vulnerabilities catalog

Established by **Binding Operational Directive 22-01**. It is not a severity ranking — it is a list of
vulnerabilities with evidence that someone is *actually using them*.

**Three criteria, all required:**[^bod-22-01]

1. a **CVE ID** assigned,
2. **reliable evidence** the exploit "is being actively used to exploit public or private
   organizations",
3. **clear remediation guidance**.

The third is why the catalog is smaller than the set of exploited vulnerabilities: a flaw under active
exploitation with no fix available does not qualify. Absence from KEV is therefore not evidence of
safety.

**Deadlines**, for federal civilian executive branch agencies:[^bod-22-01]

| CVE assigned | Remediate within |
|---|---|
| before 2021 | **6 months** |
| 2021 or later | **two weeks** |

"These default timelines may be adjusted in the case of grave risk to the Federal Enterprise."
Scope is "all software and hardware found on federal information systems", including systems operated
by third parties on an agency's behalf.[^bod-22-01]

**Why it matters outside the US federal government**, where it binds nobody: it is the highest-signal
triage input available. A CVSS score says how bad a flaw could be in principle; KEV membership says
someone is exploiting it in practice. That is why scanners such as [grype](/tools/grype.md) list it
alongside EPSS as a prioritisation source, and why "is it in KEV" is usually a better first question
than "what is its score".

## The catalog is a published feed with a schema

KEV is consumable as data, not only as a web page:

| Artifact | |
|---|---|
| JSON feed | `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` |
| JSON Schema | `…/feeds/known_exploited_vulnerabilities_schema.json` |
| CSV | `https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv` |

The envelope requires `catalogVersion`, `dateReleased`, `count` and `vulnerabilities`. Each record
**requires** `cveID`, `vendorProject`, `product`, `vulnerabilityName`, `dateAdded`,
`shortDescription`, `requiredAction` and `dueDate`, and may carry `knownRansomwareCampaignUse`,
`notes` and `cwes`.[^kev-schema]

Two consequences worth drawing out:

- **`requiredAction` and `dueDate` are required fields.** The BOD 22-01 deadline is not external
  policy commentary a consumer has to apply — it ships inside every record. The directive is encoded
  as data.
- **`cveID` is the join key.** KEV composes with [OSV](/intelligence/osv-schema.md),
  [NVD](/intelligence/nvd.md) and any BOM whose components resolve to CVEs, the same way the rest of
  this corpus's vulnerability sources do. `knownRansomwareCampaignUse` is a further triage signal with
  no equivalent elsewhere.

**The landing page is not a source for any of this.** It is a catalog browser: rendered in a real
browser it yields ~2,900 words containing no occurrence of "BOD 22-01", "criteria" or "remediate" —
*fewer* words than a plain `curl` returns, so this is not a JavaScript-rendering artifact. The
definitions live in the directive and the field semantics in the schema.

# Why this belongs in a supply-chain reference

Four of this corpus's concepts trace to CISA, and they sit at three different points on the gradient
above. A reader who meets them separately can reasonably conclude that the SBOM minimum elements and
the six SBOM types have the same standing. They do not: one is a designated federal deliverable, the
other is a community document CISA hosted and explicitly disclaimed.

# Related

- [SBOM minimum elements](/regulation/sbom-minimum-elements.md) — the 2026 edition CISA authored
- [The six SBOM types](/formats/sbom-types.md) — the document it facilitated but did not author
- [VEX](/intelligence/vex.md) — the status justifications CISA published
- [NVD](/intelligence/nvd.md) — the other US vulnerability data source, and a different agency (NIST)

[^kev-schema]: [CISA Catalog of Known Exploited Vulnerabilities — JSON Schema](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities_schema.json)
[^bod-22-01]: [BOD 22-01: Reducing the Significant Risk of Known Exploited Vulnerabilities](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities)
[^cisa-types]: [Types of Software Bill of Material (SBOM) Documents (CISA, 2023-04-21)](https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf)
