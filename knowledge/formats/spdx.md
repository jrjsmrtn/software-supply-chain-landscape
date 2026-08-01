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
    at: \'2026-08-01T21:50:00Z\'
stale_after: 2027-02-01
sources:
  - id: spdx
    title: SPDX
    resource: https://spdx.dev/
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
Core. Nine exist in 3.0.1:[^spdx-security]

`Core` · `Software` · `Licensing` · `Security` · `Build` · `Dataset` · `AI` · `Extension` · `Lite`

Two consequences matter:

- **SPDX now covers domains it used to leave alone.** The [AI and Dataset
  profiles](spdx-ai-profile.md) carry structured model and training-data metadata — energy by
  phase, `knownBias`, `safetyRiskAssessment` — with no CycloneDX equivalent.
- **VEX is native.** The Security profile defines twelve vulnerability-assessment relationship
  classes (`VexAffected…`, `VexNotAffected…`, `VexFixed…`, `VexUnderInvestigation…`), a
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
