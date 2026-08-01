---
type: Identifier
title: SPDX licence expression
description: Composition operators over SPDX identifiers, for components that are not under exactly one licence.
resource: https://spdx.dev/
tags:
  - identifier
  - licensing
  - spdx
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:55:00Z'
stale_after: 2026-12-01
sources:
  - id: spdx
    title: SPDX
    resource: https://spdx.dev/
  - id: cyclonedx-licensing
    title: 'CycloneDX: Legal and Compliance Use Case — Open Source Licensing'
    resource: https://cyclonedx.org/use-cases/open-source-licensing/
    last_modified: '2026-08-01'
---

Being under exactly one licence is the exception, not the rule. Expressions compose
[SPDX identifiers](spdx-license-list.md) to say what actually applies.[^spdx]

# Schema

| Form | Meaning |
|---|---|
| `Apache-2.0 OR MIT` | dual-licensed — the recipient chooses |
| `Apache-2.0 AND MIT` | both apply simultaneously — obligations accumulate |
| `GPL-2.0-only WITH Classpath-exception-2.0` | a listed exception modifies the licence |
| `LicenseRef-<idstring>` | a licence not on the SPDX List, defined within the document |

**`OR` and `AND` are not interchangeable, and the difference is the whole compliance question.**
`OR` lets you pick the cheaper obligation; `AND` makes you satisfy both. A tool that flattens an
expression to "the licences involved" has discarded the only part that determines what you owe.

# Where an expression lands in each format

| | CycloneDX | SPDX |
|---|---|---|
| Location | `components[].licenses[]` | package-level licence fields |
| Accepted forms | SPDX licence ID, SPDX expression, or a free-text name | SPDX ID or expression |
| Declared vs concluded | `acknowledgement` on a licence entry — `declared` or `concluded` | distinct fields (`licenseDeclared` / `licenseConcluded` in SPDX 2.x) |

CycloneDX accepts three forms, of which only two are machine-actionable; the free-text name exists
for licences that fit nowhere else.[^cyclonedx-licensing]

> **Verify field names before relying on them.** SPDX 3.0 reorganised the model, so the 2.x
> spellings above may not apply. The CycloneDX `acknowledgement` field and its `declared` /
> `concluded` values were confirmed against the CycloneDX licensing documentation, but **the spec
> version that introduced it was not** — check against the version your tooling actually emits.

# Related

- [SPDX License List](spdx-license-list.md) — the identifiers being composed
- [Declared versus concluded](declared-vs-concluded.md) — what `acknowledgement` distinguishes
- [Copyleft floor](copyleft-floor.md) — why `AND` across bundled components is the expensive case

[^spdx]: [SPDX](https://spdx.dev/)
[^cyclonedx-licensing]: [CycloneDX open-source licensing use case](https://cyclonedx.org/use-cases/open-source-licensing/)
