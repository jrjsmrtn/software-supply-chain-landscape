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
stale_after: 2027-02-01
sources:
  - id: spdx
    title: SPDX
    resource: https://spdx.dev/
---

**Software Package Data Exchange** — the Linux Foundation format, and the older of the two
dominant ones. It grew out of **license compliance**, and its name says so.[^spdx]

| | |
|---|---|
| Steward | Linux Foundation |
| Origin | license compliance |
| Standardization | ISO/IEC 5962 |
| Serializations | JSON, YAML, RDF, tag-value, spreadsheet |
| xBOM coverage | SBOM-centric, with profiles added over time |
| VEX / VDR | separate mechanisms |
| Typical audience | legal |

Both formats now do both jobs and most generators emit either on request, so the choice is rarely
urgent. What persists is the **centre of gravity**: reach for SPDX when the audience is legal, and
when procurement or an ISO reference is the requirement.

Two things follow from the licensing origin:

- Licence data is first-class rather than an attribute bolted on, including the
  [declared-versus-concluded](/licensing/declared-vs-concluded.md) distinction as **distinct
  fields** rather than a marker on one entry.
- Some procurement processes mandate SPDX specifically. That is a reason to be able to *emit* it,
  not necessarily to store it.

> **Verify field names against the version your tooling emits.** SPDX 3.0 reorganised the model;
> field spellings documented for 2.x may not carry over.

# Related

- [CycloneDX](cyclonedx.md) — the other dominant format; the comparison lives in
  [the landscape explanation](/landscape.md#cyclonedx-and-spdx--the-file-formats)
- [SPDX License List](/licensing/spdx-license-list.md) · [SPDX licence expression](/licensing/spdx-license-expression.md)
  — the licence vocabulary, which both formats use

[^spdx]: [SPDX](https://spdx.dev/)
