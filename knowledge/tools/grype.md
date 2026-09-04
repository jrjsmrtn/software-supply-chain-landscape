---
type: Tool
title: grype
description: Anchore's vulnerability scanner — takes container images, filesystems, or an SBOM directly.
resource: https://github.com/anchore/grype
tags:
  - tool
  - vulnerability
  - scanning
  - anchore
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:33:36Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:33:36Z'
  - by: claude/opus-5
    at: '2026-09-04T13:20:00Z'
stale_after: 2027-01-04
sources:
  - id: grype-repo
    title: anchore/grype
    resource: https://github.com/anchore/grype
    last_modified: '2025-12-17'
---

Anchore's vulnerability scanner, Apache-2.0, and the natural consumer of a
[syft](syft.md) SBOM.[^grype-repo]

| | |
|---|---|
| Scans | container images, filesystems, **and SBOMs** |
| Image formats | Docker, OCI, Singularity |
| Prioritisation | EPSS, KEV, risk scoring |
| Triage input | **OpenVEX**, for filtering and augmenting results |

# Scanning an SBOM, not the artifact

The property worth knowing: grype will scan an SBOM directly — upstream's phrasing is
"**Scan an SBOM for even faster vulnerability detection**".[^grype-repo]

That closes the loop this landscape is built around. Generate once with syft, store the BOM, and
re-scan the *document* as new advisories arrive rather than re-scanning the artifact — which is the
same argument [Dependency-Track](dependency-track.md) makes as a standing service rather than a CLI.

# What its README does not say

It **does not name its vulnerability data source**. That is worth stating rather than assuming: the
provenance of the matching data is the thing that determines whether a finding is trustworthy, and
a scanner's coverage is only as good as the feed behind it. Check the database it downloads before
relying on a clean result.

Its [OpenVEX](/intelligence/openvex.md) support is the mechanism for suppressing findings you have
adjudicated, so a clean run means "nothing new" rather than "nothing filtered".

# Related

- [syft](syft.md) — what produces its input
- [OpenVEX](/intelligence/openvex.md) — how findings get filtered honestly
- [trivy](trivy.md) · [osv-scanner](osv-scanner.md) — the alternatives

[^grype-repo]: [anchore/grype](https://github.com/anchore/grype)
