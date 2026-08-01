---
type: Data Source
title: osv.dev
description: The free aggregating database that normalises roughly two dozen ecosystem advisory sources into the OSV schema.
resource: https://osv.dev/
tags:
  - vulnerability
  - data-source
  - openssf
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
stale_after: 2026-12-01
sources:
  - id: osv-dev
    title: OSV — Open Source Vulnerabilities
    resource: https://osv.dev/
  - id: osv-data-sources
    title: 'osv.dev: data sources'
    resource: https://google.github.io/osv.dev/data/
---

The database half of OSV: upstream advisory sources normalised into the
[OSV schema](osv-schema.md) behind a free API.[^osv-dev]

# Coverage

Roughly two dozen upstream sources as of 2026-07, including ecosystem advisory databases (GitHub
Security Advisories, PyPA, RustSec, the Go vulnerability database, npm), Linux distribution
trackers, and OSS-Fuzz findings.[^osv-data-sources]

> This count and source list are the perishable part of this concept and the reason for its earlier
> expiry. The schema does not move at this rate — see [OSV schema](osv-schema.md).

**Two properties do the work.** Advisories are authored by whoever actually owns the package, so
affected ranges are accurate rather than inferred. And records key on
[purl](/naming/purl.md), so the join is a lookup.

# Limits

**Scope: open-source packages.** Operating systems, appliances and commercial products remain
[NVD](nvd.md) and CPE territory.

**Coverage varies by ecosystem**, and that is an organizational fact rather than a data-quality
one — it resolves to whether anyone owns disclosure for that ecosystem. See [CNA](cna.md).

An unregistered [purl](/naming/purl.md) type returns an **empty result, not an error**, which is
indistinguishable in output from a component with no known vulnerabilities.

# Consumers

`osv-scanner` (first-party), Trivy, Dependency-Track, pip-audit, Renovate, OSS Review Toolkit.

# Related

- [OSV schema](osv-schema.md) · [OSV IDs](/naming/osv-ids.md)
- [NVD](nvd.md) — where coverage stops
- [CNA](cna.md) — why coverage is uneven

[^osv-dev]: [OSV — Open Source Vulnerabilities](https://osv.dev/)
[^osv-data-sources]: [osv.dev data sources](https://google.github.io/osv.dev/data/)
