---
type: Attack
title: Typosquatting
description: A malicious package registered under a name lexically close to a popular one, catching mistyped or misremembered installs.
tags:
  - threat
  - registry
  - naming
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T21:35:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T21:35:00Z'
stale_after: 2027-08-01
sources:
  - id: typogard
    title: 'Defending Against Package Typosquatting (TypoGard)'
    resource: https://dl.acm.org/doi/10.1007/978-3-030-65745-1_7
  - id: ossf-malicious
    title: 'OpenSSF: Detecting Malicious Packages Using the OSV API'
    resource: https://openssf.org/blog/2026/05/20/detecting-malicious-packages-using-the-osv-api/
    last_modified: '2026-05-20'
  - id: typosquat-dataset
    title: 'ecosyste.ms: curated typosquatting dataset'
    resource: https://github.com/ecosyste-ms/typosquatting-dataset
---

A package registered under a name lexically close to a popular one, so that a mistyped or
misremembered dependency installs the attacker's code.

It affects **every** major ecosystem — npm, PyPI, Go, Maven, RubyGems, NuGet — because it exploits
naming similarity rather than any ecosystem-specific flaw.

# The distances are small

Analysis of 40 historical typosquatting attacks found **18 had a Levenshtein distance of 2 or less**
from their target.[^typogard] Detection research such as TypoGard combines lexical similarity with
package *popularity*, since a near-miss on an obscure package is not worth an attacker's
time.[^typogard]

# Why a scanner will not save you

This is a **registry-side** problem. Deciding that `reqeusts` is squatting on `requests` requires
knowing the namespace and the popularity distribution — neither of which is visible from inside the
package being installed. Static analysis of the artifact cannot do it.

Registries have moved accordingly: npm blocks names that closely resemble existing ones, and PyPI's
Warehouse has carried proposals for similar "distance" rules against top packages.

# Practice

- **Install from a lockfile.** A name typed once and pinned cannot be mistyped again.
- **Consume `MAL-` records.** OpenSSF's [malicious-packages](/intelligence/osv-dev.md) repository —
  "the first open source system for collecting and publishing cross-ecosystem reports of malicious
  packages" — publishes them in OSV format with `MAL-` identifiers, queryable through the same API
  as ordinary advisories.[^ossf-malicious]
- **Prefer a curated internal mirror** over direct public installs, so a new name is a deliberate
  admission rather than a typo away.

Curated ground truth exists for testing detection.[^typosquat-dataset]

# Related

- [OSV IDs](/naming/osv-ids.md) — `MAL-` is a distinct namespace from vulnerability advisories
- [Dependency confusion](dependency-confusion.md) — name-based, but needs no typo
- [SLSA threat model](slsa-threat-model.md) — threat D

[^typogard]: [Defending Against Package Typosquatting](https://dl.acm.org/doi/10.1007/978-3-030-65745-1_7)
[^ossf-malicious]: [OpenSSF: Detecting Malicious Packages Using the OSV API](https://openssf.org/blog/2026/05/20/detecting-malicious-packages-using-the-osv-api/)
[^typosquat-dataset]: [ecosyste.ms typosquatting dataset](https://github.com/ecosyste-ms/typosquatting-dataset)
