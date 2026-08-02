---
type: Regulation
title: FD&C Act §524B
description: US medical devices — an SBOM is a condition of premarket submission, with no content floor stated in the statute at all.
resource: https://www.govinfo.gov/content/pkg/USCODE-2023-title21/html/USCODE-2023-title21-chap9-subchapV-partA-sec360n-2.htm
tags:
  - regulation
  - us
  - sbom
  - medical-devices
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-02T08:25:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-02T08:25:00Z'
stale_after: 2027-08-01
sources:
  - id: usc-360n-2
    title: 21 U.S.C. §360n-2 — Ensuring cybersecurity of devices
    resource: https://www.govinfo.gov/content/pkg/USCODE-2023-title21/html/USCODE-2023-title21-chap9-subchapV-partA-sec360n-2.htm
---

Section **524B of the Federal Food, Drug, and Cosmetic Act**, codified at **21 U.S.C. §360n-2**,
"Ensuring cybersecurity of devices". Added by §3305 of the Consolidated Appropriations Act, 2023,
and effective 90 days after 2022-12-29 — that is, **2023-03-29**.[^usc-360n-2]

> **This describes what the statute requires of a submission. It does not say whether your product
> is a cyber device**, which is the question that decides whether any of it applies. That is a legal
> and regulatory determination, and this is not legal advice.

# What it requires

The sponsor of a premarket submission for a cyber device must, under subsection (b):[^usc-360n-2]

| ¶ | Requirement |
|---|---|
| (b)(1) | Submit a plan to monitor, identify and address postmarket cybersecurity vulnerabilities and exploits |
| (b)(2) | Design and maintain processes giving reasonable assurance of cybersecurity, and deliver updates — on a regular cycle for known vulnerabilities, urgently for critical ones |
| **(b)(3)** | **"provide to the Secretary a software bill of materials, including commercial, open-source, and off-the-shelf software components"** |
| (b)(4) | Comply with such other requirements as the Secretary may require |

# What counts as a cyber device

Subsection (c) sets three conditions, and they are conjunctive — a device that fails any one of them
is outside the section entirely. It must include software validated, installed or authorized by the
sponsor; have the ability to connect to the internet; and contain technological characteristics that
could be vulnerable to cybersecurity threats.[^usc-360n-2]

# The statute states no content floor

This is the point worth carrying away. Compare the three instruments in this directory:

| Instrument | What it says an SBOM must contain |
|---|---|
| [EU CRA](cra.md) | at least the **top-level dependencies**, in a commonly used machine-readable format |
| [2026 minimum elements](sbom-minimum-elements.md) | **17 named data fields**, grouped into document metadata and component data |
| **§524B** | **"commercial, open-source, and off-the-shelf software components"** — and nothing further |

§524B names no fields, no depth, no format and no identifier scheme. It says *which kinds of
component* must be covered — including the off-the-shelf and commercial ones a manufacturer might
otherwise treat as opaque — and leaves everything else to the Secretary under (b)(4) and to agency
guidance.

**The floor is therefore set below the statute, not in it.** A reader looking for "what does FDA
require in an SBOM" will not find the answer here, and should not conclude there is no answer.

> **Deliberately not tracked here**: the FDA guidance elaborating how to satisfy §524B in a
> submission. That is process for demonstrating compliance rather than a content requirement on a
> document, which puts it outside this directory's scope — and it moves faster than the statute. The
> `stale_after` on this concept reflects statutory claims only.

# It goes to the regulator, not the customer

(b)(3) says "provide to the Secretary". Like the [CRA](cra.md), the statute compels an SBOM to
**exist and be handed to an authority**; neither compels publication to the people using the
product. Two instruments, two jurisdictions, the same shape — which is worth knowing before assuming
that regulation is what will make SBOMs generally available.

# Related

- [SBOM](/bom-types/sbom.md) — the artifact
- [EU Cyber Resilience Act](cra.md) — the other statutory instrument, with a stated floor
- [SBOM minimum elements](sbom-minimum-elements.md) — the US content floor, set by guidance rather than statute
- [HBOM](/bom-types/hbom.md) — a connected medical device is hardware with firmware, not software alone

[^usc-360n-2]: [21 U.S.C. §360n-2 — Ensuring cybersecurity of devices](https://www.govinfo.gov/content/pkg/USCODE-2023-title21/html/USCODE-2023-title21-chap9-subchapV-partA-sec360n-2.htm)
