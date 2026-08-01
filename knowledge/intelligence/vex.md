---
type: BOM Type
title: VEX
description: Vulnerability Exploitability eXchange — the supplier's per-vulnerability statement about whether a finding actually applies.
resource: https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex-status-justification-document-june-2022
tags:
  - vex
  - triage
  - vulnerability
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
stale_after: 2027-02-01
sources:
  - id: cisa-vex
    title: 'CISA: VEX Status Justification document'
    resource: https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex-status-justification-document-june-2022
    last_modified: '2022-06'
  - id: openvex-spec
    title: OpenVEX specification
    resource: https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md
  - id: cyclonedx-vex
    title: 'CycloneDX: VEX capability'
    resource: https://cyclonedx.org/capabilities/vex/
  - id: spdx-security
    title: 'SPDX 3.0.1: Security profile'
    resource: https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Security/
---

A scanner reports two hundred vulnerabilities. Most are not real problems for *this* product: the
flawed function lives in a part of the library nobody calls, or the vulnerable path is
unreachable. VEX is the supplier's answer, **per vulnerability**.[^cisa-vex]

The valuable verdict is **`not_affected`**, because it must carry a machine-readable
justification. An unjustified "not affected" is an assertion; a justified one is a claim a consumer
can evaluate.

Without VEX, SBOMs generate alert fatigue and get ignored — the single most common way a
supply-chain programme fails in practice.

# Schema

**The formats do not share an enum.** This is the most common source of confusion when mapping
between them, and it is why "supports VEX" is not a sufficient tooling requirement.

CISA / [OpenVEX](openvex.md) status values:[^cisa-vex][^openvex-spec]

| Status | Meaning |
|---|---|
| `not_affected` | the vulnerability does not affect this product |
| `affected` | the product is affected; action recommended |
| `fixed` | a released version contains the fix |
| `under_investigation` | not yet determined |

OpenVEX `not_affected` justifications:

| Justification |
|---|
| `component_not_present` |
| `vulnerable_code_not_present` |
| `vulnerable_code_not_in_execute_path` |
| `vulnerable_code_cannot_be_controlled_by_adversary` |
| `inline_mitigations_already_exist` |

[CycloneDX](/formats/cyclonedx.md) `analysis.state` (impactAnalysisState):[^cyclonedx-vex]

| State |
|---|
| `resolved` |
| `resolved_with_pedigree` |
| `exploitable` |
| `in_triage` |
| `false_positive` |
| `not_affected` |

CycloneDX `analysis.justification` (impactAnalysisJustification):

| Justification |
|---|
| `code_not_present` |
| `code_not_reachable` |
| `requires_configuration` |
| `requires_dependency` |
| `requires_environment` |
| `protected_by_compiler` |
| `protected_at_runtime` |
| `protected_at_perimeter` |
| `protected_by_mitigating_control` |

**SPDX 3.0 adds a third.** The Security profile carries VEX natively — twelve
vulnerability-assessment relationship classes (`VexAffected…`, `VexNotAffected…`, `VexFixed…`,
`VexUnderInvestigation…`), a `justificationType` property and a `VexJustificationType`
vocabulary.[^spdx-security] Anything written on the assumption that SPDX handles VEX externally
predates 3.0 — see [SPDX](/formats/spdx.md).

The justification vocabularies overlap in intent but not in spelling, and CycloneDX's is
finer-grained — `requires_configuration` and `protected_at_perimeter` have no OpenVEX equivalent.
A lossless round-trip between any two of the three does not exist.

# Related

- [VDR](vdr.md) — the adjacent document answering a different question
- [OpenVEX](openvex.md) · [CSAF VEX](csaf-vex.md) — the standalone formats
- [CycloneDX](/formats/cyclonedx.md) — carries VEX natively in the `vulnerabilities` array[^cyclonedx-vex]

[^cisa-vex]: [CISA VEX status justifications](https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex-status-justification-document-june-2022)
[^openvex-spec]: [OpenVEX specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md)
[^cyclonedx-vex]: [CycloneDX VEX capability](https://cyclonedx.org/capabilities/vex/)
[^spdx-security]: [SPDX 3.0.1 Security profile](https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Security/)
