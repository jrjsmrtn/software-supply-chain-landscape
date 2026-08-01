---
type: Tool
title: Dependency-Track
description: OWASP continuous SBOM analysis platform — stores BOMs and re-evaluates them as advisories arrive, rather than scanning once at build time.
resource: https://dependencytrack.org/
tags:
  - tool
  - platform
  - owasp
  - sbom
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:20:00Z'
stale_after: 2026-12-01
sources:
  - id: dependency-track
    title: OWASP Dependency-Track
    resource: https://dependencytrack.org/
  - id: dt-5-release
    title: Dependency-Track 5.0 release announcement
    resource: https://dependencytrack.org/news/dependency-track-5-0/
---

The standing inventory. It stores BOMs **per project and version** and re-evaluates them as new
vulnerability intelligence arrives, rather than scanning once at build time.[^dependency-track]

That distinction is the whole value. Scanning at build time tells you what was known on build day;
disclosure is continuous and artifacts do not rescan themselves. A stored BOM can become newly
affected months after the binary stopped changing.

| | |
|---|---|
| Ingests | [CycloneDX](/formats/cyclonedx.md) BOMs, [VEX](/intelligence/vex.md) |
| Intelligence sources | NVD, GitHub Advisories, OSV, Snyk |
| Capabilities | portfolio-wide component search, VEX ingestion and audit workflow, policy engine (licence / severity / operational), notifications |
| Outbound | Slack, Teams, Jira, webhooks |
| Deployment | server — API server plus frontend |

**It is an operational commitment, not a CLI.** Running it means running a service, and that is the
honest cost of the capability. Tools that scan on demand are cheaper and answer a smaller question.

# Version

5.0 became generally available on **2026-06-09**, described by the project as its largest
architectural redesign; 5.0.3 was current as of 2026-07.[^dt-5-release]

> Version facts are the perishable part of this concept and the reason for its earlier expiry.

# Related

- [CycloneDX](/formats/cyclonedx.md) — the format it ingests
- [VEX](/intelligence/vex.md) — what filters its findings down to the actionable ones
- [osv.dev](/intelligence/osv-dev.md) — one of its intelligence sources

[^dependency-track]: [OWASP Dependency-Track](https://dependencytrack.org/)
[^dt-5-release]: [Dependency-Track 5.0 release announcement](https://dependencytrack.org/news/dependency-track-5-0/)
