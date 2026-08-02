---
type: Data Source
title: Repology
description: Cross-repository package version tracker — the currency axis, and a working answer to identity across ecosystems rather than within one.
resource: https://repology.org/
tags:
  - packaging
  - data-source
  - versions
  - distributions
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-02T06:57:47Z'
verified:
  - by: claude/opus-5
    at: '2026-08-02T06:57:47Z'
stale_after: 2026-12-01
sources:
  - id: repology-about
    title: 'Repology: about'
    resource: https://repology.org/docs/about
  - id: repology-api
    title: 'Repology: API documentation'
    resource: https://repology.org/api
  - id: repology-stats
    title: 'Repology: repository statistics'
    resource: https://repology.org/repositories/statistics
  - id: libversion
    title: repology/libversion
    resource: https://github.com/repology/libversion
---

A service that "tracks and compares package versions" across package repositories — distributions,
language ecosystems and ports trees.[^repology-about] **293 repositories are listed on its statistics
page as of 2026-08-02**, covering **323,052 projects and 4,863,320 individual packages**.[^repology-stats]

# The axis it adds

[osv.dev](osv-dev.md) answers *is a known vulnerability published against this*.
[endoflife.date](endoflife-date.md) answers *is this line still supported*. Repology answers a third
question neither touches: **how far behind upstream is the packaging you actually installed**.

The three fail independently. A package can carry no CVE, sit inside its support window, and still
be four upstream releases behind because the distribution froze it — and nothing in a BOM says so.

# Project versus package

The distinction is the concept's transferable part. A **package** is one repository's entry; a
**project** groups related packages across repositories under a unified name derived from the
package names, which "may differ from actual package names" in any given repository.[^repology-api]

That is identity *across* ecosystems. [purl](/naming/purl.md) deliberately does not solve it: a purl
is unique within a `type`, so `pkg:deb/...` and `pkg:pypi/...` naming the same upstream project are
simply different identifiers with nothing joining them. Repology's project name is one working answer
to that join, built by normalisation rather than by registry — which is also why it is approximate.

# Status vocabulary

Each package is classified by comparing its version against the project's other
packages.[^repology-api] Ten values: `newest`, `devel`, `unique`, `outdated`, `legacy`, `rolling`,
`noscheme`, `incorrect`, `untrusted`, `ignored`.

`outdated` is the one that carries supply-chain weight, and `rolling` and `noscheme` are the honest
admissions — some repositories have no comparable version scheme at all.

# API

`/api/v1/project/{name}` for one project, `/api/v1/projects/` for ranges and filters. Two mandatory
fields per package, `repo` and `version`; optional ones include `status`, `licenses`, `maintainers`,
`srcname`, `binname` and `origversion`.[^repology-api]

**Rate limited to one request per second**, with a database dump offered instead for anything over
1,000 requests daily, and bulk clients required to send a custom `User-Agent` naming their source
repository and issue tracker or risk blocking.[^repology-api] Plan on the dump for any systematic use.

The `licenses` field makes this a secondary licence source too — but the strings are whatever each
repository declares, unnormalised, so it is [declared, not concluded](/licensing/declared-vs-concluded.md)
and not an [SPDX expression](/licensing/spdx-license-expression.md).

# Limits

**Version is not content.** Distributions backport security fixes without changing the version
string, so a package Repology marks `outdated` may already carry the patch, and one marked `newest`
may not. This is the standard source of disagreement between distro packaging and version-range
vulnerability matching — treat currency as a signal to investigate, never as a verdict.

**The data has no declared licence.** The about page states only that code is "licensed under
GPLv3+"; nothing states terms for the aggregated package data.[^repology-about] For a service built
entirely on redistributing other projects' metadata, that gap is worth knowing before building on it.

**Its own figures disagree.** The about page says "more than 120 package repositories" while the
statistics page lists 293.[^repology-about][^repology-stats] Both are true as written; the prose is
simply older than the data. Prefer the statistics page.

Version comparison across ecosystems is hard enough to have produced a dedicated library — the same
project publishes **libversion** (MIT), "advanced version string comparison".[^libversion] The about
page describes the site's own classification as "a custom general algorithm" without naming
it,[^repology-about] so treat the two as related work rather than assuming one implements the other.

The repository and project counts above are the perishable parts of this concept.

# Related

- [purl](/naming/purl.md) — identity *within* an ecosystem, which this complements rather than duplicates
- [endoflife.date](endoflife-date.md) — the lifecycle axis
- [osv.dev](osv-dev.md) — the vulnerability axis
- [declared vs concluded licensing](/licensing/declared-vs-concluded.md) — what its `licenses` field is

[^repology-about]: [Repology: about](https://repology.org/docs/about)
[^repology-api]: [Repology: API documentation](https://repology.org/api)
[^repology-stats]: [Repology: repository statistics](https://repology.org/repositories/statistics)
[^libversion]: [repology/libversion](https://github.com/repology/libversion)
