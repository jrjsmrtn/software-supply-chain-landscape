---
type: Identifier
title: SPDX License List
description: The controlled vocabulary of short licence identifiers — the join key for licences, as purl is for packages.
resource: https://spdx.org/licenses/
tags:
  - identifier
  - licensing
  - spdx
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:55:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:12:00Z\'
stale_after: 2027-08-01
sources:
  - id: spdx-license-list
    title: SPDX License List
    resource: https://spdx.org/licenses/
---

Licences are named with **SPDX identifiers** drawn from the SPDX License List — `Apache-2.0`,
`MIT`, `GPL-3.0-or-later`.[^spdx-license-list]

The list does for licences what [purl](/naming/purl.md) does for packages: it turns a string a
human wrote into an identifier a machine can join on. `Apache-2.0` is an identifier; "Apache
License" is not — it does not say which version, or whether the patent grant applies.

The list is the controlled vocabulary. Free text is the fallback, not the norm, and a licence
field carrying prose is a licence field nothing downstream can act on.

# Naming conventions worth knowing

| Pattern | Meaning |
|---|---|
| `GPL-3.0-only` | that version, no later-version option |
| `GPL-3.0-or-later` | that version or any later one, at the recipient's choice |
| `LicenseRef-<idstring>` | a licence not on the list, defined within the document itself |

The `-only` / `-or-later` distinction replaced an older `+` suffix and is not cosmetic: it is the
difference between one obligation and an open-ended set of them.

**The superseded forms are still on the list**, flagged `isDeprecatedLicenseId` — 32 of 733
identifiers as of 2026-08-02. So encountering `GPL-3.0` or `GPL-3.0+` does not mean the producer
invented an identifier; it means they used a deprecated one, and the ambiguity `-only` was
introduced to remove is back.

# Related

- [SPDX licence expression](spdx-license-expression.md) — composing identifiers when one licence
  is not enough
- [Declared versus concluded](declared-vs-concluded.md) — an identifier says *which* licence, not
  *how well anyone checked*

[^spdx-license-list]: [SPDX License List](https://spdx.org/licenses/)
