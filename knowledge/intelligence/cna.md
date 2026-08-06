---
type: Organization
title: CNA (CVE Numbering Authority)
description: Who is authorized to assign CVE IDs, within what scope — the mechanism behind uneven per-ecosystem advisory quality.
resource: https://www.cve.org/
tags:
  - vulnerability
  - organization
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:45:00Z'
stale_after: 2027-02-01
sources:
  - id: cve-program
    title: CVE Program
    resource: https://www.cve.org/
  - id: ossf-cna-guide
    title: 'OpenSSF: Becoming a CNA as an Open Source Org or Project'
    resource: https://github.com/ossf/wg-vulnerability-disclosures/blob/main/docs/guides/becoming-a-cna-as-an-open-source-org-or-project.md
  - id: psf-cna
    title: The Python Software Foundation has been authorized as a CNA
    resource: https://discuss.python.org/t/the-python-software-foundation-has-been-authorized-by-the-cve-program-as-a-cve-numbering-authority-cna/32561
  - id: eef-cna
    title: Erlang Ecosystem Foundation CNA
    resource: https://cna.erlef.org/
---

An organization authorized by the CVE Program to assign [CVE](/naming/cve.md) IDs and publish CVE
Records **within a defined scope**.[^cve-program]

**Scope is the operative word.** A CNA covers named products, repositories, or a package registry.
Anything outside every CNA's scope falls back to a generalist authority with no domain knowledge of
it.

# Why this belongs in a supply-chain reference

"Coverage varies by ecosystem" sounds like a data-quality observation. It is an **organizational**
one.

Where a foundation runs a CNA for its own ecosystem, affected-version ranges are written by people
who maintain the code. Where none does, ranges are inferred. So the question "is my ecosystem well
covered" resolves to **"does anyone own vulnerability disclosure for it"** — a question about
people, not schemas.

This is also why a tool must declare when it has no coverage rather than emit a clean scan.

# Open-source foundations taking the seat

| CNA | Scope | Notes |
|---|---|---|
| **Python Software Foundation** | Python and PyPI | its Security Developer-in-Residence's experience informed the OpenSSF guide[^psf-cna] |
| **curl** | curl / libcurl | adopted partly to gate low-quality CVE filings against the project |
| **Erlang Ecosystem Foundation** | active packages on Hex.pm, and projects under the `elixir-lang`, `erlang`, `erlef`, `erlef-cna` and `gleam-lang` GitHub organizations; fallback CNA for all Hex.pm packages | authorized 2025-05, under [Ægis](aegis.md); publishes to OSV; disclosure embargo capped at 3 months[^eef-cna] |

Illustrative, not exhaustive — the authoritative roster is the CVE Program's own. OpenSSF publishes
a guide for projects considering it.[^ossf-cna-guide]

> **Acronym collision.** CNA here is a CVE Numbering Authority, unrelated to the container-networking
> sense.

# The other half of the mechanism

A CNA decides who may *assign* an ID and describe the vulnerability. It does not cover who may *add
to* a published record — that is the [ADP](adp.md) role, whose contributions live in a separate
container the CNA's data is protected from.

# Related

- [CVE](/naming/cve.md) — what a CNA assigns
- [Ægis](aegis.md) — the worked example closest to this portfolio
- [osv.dev](osv-dev.md) — where the resulting records are aggregated

[^cve-program]: [CVE Program](https://www.cve.org/)
[^ossf-cna-guide]: [OpenSSF: Becoming a CNA as an Open Source Org or Project](https://github.com/ossf/wg-vulnerability-disclosures/blob/main/docs/guides/becoming-a-cna-as-an-open-source-org-or-project.md)
[^psf-cna]: [PSF authorized as a CNA](https://discuss.python.org/t/the-python-software-foundation-has-been-authorized-by-the-cve-program-as-a-cve-numbering-authority-cna/32561)
[^eef-cna]: [Erlang Ecosystem Foundation CNA](https://cna.erlef.org/)
