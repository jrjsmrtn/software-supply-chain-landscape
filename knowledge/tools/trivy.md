---
type: Tool
title: trivy
description: Aqua Security's broad scanner — vulnerabilities, misconfigurations, secrets and licences across images, filesystems, VMs and Kubernetes.
resource: https://github.com/aquasecurity/trivy
tags:
  - tool
  - vulnerability
  - scanning
  - misconfiguration
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
  - id: trivy-repo
    title: aquasecurity/trivy
    resource: https://github.com/aquasecurity/trivy
    last_modified: '2026-04-24'
  - id: trivy-docs
    title: Trivy documentation
    resource: https://trivy.dev/docs/latest/
---

Aqua Security's scanner, Apache-2.0. The distinguishing feature is **breadth** rather than depth in
any one dimension.[^trivy-repo]

| | |
|---|---|
| Targets | container image, filesystem, remote git repository, virtual machine image, Kubernetes |
| Detects | OS packages and dependencies (SBOM), known CVEs, IaC issues and misconfigurations, secrets, software licences |

# Breadth is the trade-off, not a free win

Where [grype](grype.md) does one job against one input class, trivy spans vulnerability scanning,
IaC misconfiguration, secret detection and licence identification across five target types. That is
genuinely useful as a single CI step, and it means each dimension competes for attention with the
others.

Two specific consequences:

- Its **licence detection** is a *declared*-licence reading like any generator's — see
  [declared versus concluded](/licensing/declared-vs-concluded.md). Breadth does not make it a
  compliance answer.
- Its **secret detection** overlaps tools like `gitleaks` and is not a substitute for scanning git
  history, which is a different question from scanning a working tree.

# Verify before pinning

Its README states neither the **SBOM formats** it emits and consumes nor its **vulnerability data
source**; both are documented separately.[^trivy-docs] Since those two facts determine whether it
fits a given pipeline, check them against the docs for the version you deploy rather than assuming
parity with the other scanners here.

# Related

- [grype](grype.md) · [osv-scanner](osv-scanner.md) — narrower scanners
- [Declared versus concluded](/licensing/declared-vs-concluded.md) — what its licence output is worth

[^trivy-repo]: [aquasecurity/trivy](https://github.com/aquasecurity/trivy)
[^trivy-docs]: [Trivy documentation](https://trivy.dev/docs/latest/)
