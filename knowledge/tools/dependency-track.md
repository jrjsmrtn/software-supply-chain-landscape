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
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:37:22Z'
  - by: claude/opus-5
    at: '2026-09-04T13:20:00Z'
stale_after: 2027-01-04
sources:
  - id: dependency-track
    title: OWASP Dependency-Track
    resource: https://dependencytrack.org/
  - id: dependency-track-repo
    title: DependencyTrack/dependency-track
    resource: https://github.com/DependencyTrack/dependency-track
    last_modified: '2026-08-24'
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
architectural redesign.[^dt-5-release] **5.1.0 is current as of 2026-09-04.**

The decay rate is the point of recording it. This concept said 5.0.3 when written, was corrected to
5.0.4 a day later, and by this re-verification had passed 5.0.5 (2026-08-24) and 5.1.0 (2026-08-27)
— two releases inside five weeks, none of which any expiry date would have flagged, because
`stale_after` was months away throughout.

⚠ **v4 is dated.** Upstream states v4 reaches end-of-life in **2026-12**, roughly six months after
v5 GA, and is in maintenance mode on its own branch.[^dependency-track-repo] Anyone still on v4 has
a deadline rather than a preference.

> Version facts are the perishable part of this concept and the reason for its earlier expiry.

# Related

- [CycloneDX](/formats/cyclonedx.md) — the format it ingests
- [VEX](/intelligence/vex.md) — what filters its findings down to the actionable ones
- [osv.dev](/intelligence/osv-dev.md) — one of its intelligence sources

[^dependency-track]: [OWASP Dependency-Track](https://dependencytrack.org/)
[^dt-5-release]: [Dependency-Track 5.0 release announcement](https://dependencytrack.org/news/dependency-track-5-0/)
[^dependency-track-repo]: [DependencyTrack/dependency-track](https://github.com/DependencyTrack/dependency-track)
