---
type: Format
title: SPDX
description: The Linux Foundation BOM format, grown out of license compliance and standardized as ISO/IEC 5962.
resource: https://spdx.dev/
tags:
  - format
  - bom
  - linux-foundation
  - licensing
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:00:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T21:50:00Z'
  - by: claude/opus-5
    at: '2026-09-10T10:00:00Z'
stale_after: 2027-03-10
sources:
  - id: spdx
    title: SPDX
    resource: https://spdx.dev/
  - id: spdx-3-model
    title: 'SPDX 3 model (tags 3.0.1 and 3.1-rc1)'
    resource: https://github.com/spdx/spdx-3-model
  - id: spdx-security
    title: 'SPDX 3.0.1: Security profile'
    resource: https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Security/
---

**Software Package Data Exchange** — the Linux Foundation format, and the older of the two
dominant ones. It grew out of **license compliance**, and its name says so.[^spdx]

| | |
|---|---|
| Steward | Linux Foundation |
| Origin | license compliance |
| Standardization | ISO/IEC 5962 |
| Serializations | JSON, YAML, RDF, tag-value, spreadsheet |
| xBOM coverage | profile-based — Software, AI, Dataset, Security, Build, Licensing |
| VEX / VDR | **native since 3.0**, via the Security profile |
| Typical audience | legal |

The origin still shows in the licensing depth, but **"SPDX for lawyers, CycloneDX for security" is
no longer an accurate split**. As of 3.0 the two formats have overlapping *and* genuinely
complementary scopes — see [choosing between them](cyclonedx.md#the-two-are-complementary-not-rivals).

Two things follow from the licensing origin:

- Licence data is first-class rather than an attribute bolted on, including the
  [declared-versus-concluded](/licensing/declared-vs-concluded.md) distinction as **distinct
  fields** rather than a marker on one entry.
- Some procurement processes mandate SPDX specifically. That is a reason to be able to *emit* it,
  not necessarily to store it.

# Profiles are the 3.0 mechanism

SPDX 3.0 reorganised around **namespaces (profiles)**, each adding a domain's vocabulary on top of
Core:[^spdx-security]

`Core` · `Software` · `Licensing` · `Security` · `Build` · `Dataset` · `AI` · `Extension` · `Lite`

**Count them from the model tree at the 3.0.1 tag and you get eleven, not nine**, because
`SimpleLicensing` and `ExpandedLicensing` sit beside `Licensing` as their own
namespaces.[^spdx-3-model] The nine above are the ones a consumer chooses between; the extra two
subdivide licensing rather than adding a domain. Stated because the two numbers are both defensible
and neither is wrong — say which you are counting.

⚠ **SPDX 3.1 is in progress**, tagged `3.1-rc1`, and adds five namespaces absent from 3.0.1:
**`Hardware`**, **`SupplyChain`**, `Operations`, `Service` and `FunctionalSafety`.[^spdx-3-model]
The first two are this bundle's own subject matter arriving in a format that previously left it to
[CycloneDX](cyclonedx.md) — worth watching rather than acting on, since a release candidate is not
a specification.

Two consequences matter:

- **SPDX now covers domains it used to leave alone.** The [AI and Dataset
  profiles](spdx-ai-profile.md) carry structured model and training-data metadata — energy by
  phase, `knownBias`, `safetyRiskAssessment` — with no CycloneDX equivalent.
- **VEX is native, and it is not only VEX.** The Security profile defines twelve
  vulnerability-assessment relationship classes, of which **five are `Vex…`** (`VexAffected…`,
  `VexNotAffected…`, `VexFixed…`, `VexUnderInvestigation…`, plus the abstract base). The other seven
  model **CVSS v2, v3 and v4 scores, [EPSS](/intelligence/epss.md), [SSVC](/intelligence/ssvc.md)
  and exploit catalogs** such as [KEV](/intelligence/cisa.md) as first-class
  relationships.[^spdx-3-model] So the profile carries the whole triage stack this bundle documents
  separately, not just the supplier's verdict. A
  `Vulnerability` class, 21 properties including `justificationType` and `vexVersion`, and a
  `VexJustificationType` vocabulary. Its own description is terse — "The Security Profile captures
  security related information."[^spdx-security]

> **This corrects a claim widely repeated about 2.x**, including in earlier versions of this bundle:
> that SPDX handles VEX "by separate mechanisms". True before 3.0, false now, and it was the
> most-cited reason to prefer CycloneDX for triage.

> **Verify field names against the version your tooling emits.** Field spellings documented for 2.x
> may not carry over, and much tooling still emits 2.x.

# Related

- [CycloneDX](cyclonedx.md) — the other dominant format; the comparison lives in
  [the landscape explanation](/landscape.md#cyclonedx-and-spdx--the-file-formats)
- [SPDX License List](/licensing/spdx-license-list.md) · [SPDX licence expression](/licensing/spdx-license-expression.md)
  — the licence vocabulary, which both formats use

[^spdx]: [SPDX](https://spdx.dev/)
[^spdx-security]: [SPDX 3.0.1 Security profile](https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Security/)
[^spdx-3-model]: [SPDX 3 model](https://github.com/spdx/spdx-3-model)
