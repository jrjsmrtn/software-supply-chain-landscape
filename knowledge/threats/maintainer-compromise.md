---
type: Attack
title: Maintainer compromise
description: A legitimate publisher's account or machine is taken over, so malicious releases are signed and published correctly.
tags:
  - threat
  - registry
  - signing
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T21:35:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T21:35:00Z'
stale_after: 2027-08-01
sources:
  - id: slsa-threats
    title: 'SLSA v1.0: Supply chain threats'
    resource: https://slsa.dev/spec/v1.0/threats
  - id: ossf-malicious
    title: 'OpenSSF: Detecting Malicious Packages Using the OSV API'
    resource: https://openssf.org/blog/2026/05/20/detecting-malicious-packages-using-the-osv-api/
    last_modified: '2026-05-20'
---

The publisher is real; the person operating the account is not. A stolen credential, a phished
token, or a compromised maintainer machine produces releases that are **published through the
legitimate path and signed with the legitimate identity**.

# The reason this concept exists

Every other control in this bundle assumes the publisher is honest.

**Signing does not help.** A compromised maintainer signs malicious releases perfectly validly — the
signature attests *who published*, which is exactly what an attacker has taken. See
[Sigstore](/provenance/sigstore.md).

**Provenance does not help.** SLSA grades the integrity of the build process; a compromised
maintainer's build is faithfully and verifiably built from source they control. This is threats F
and H in [the SLSA threat model](slsa-threat-model.md), and v1.0 addresses neither the registry
compromise case (G) nor the dependency case (D).[^slsa-threats]

**Reproducible builds do not help**, for the same reason: reproducing an attacker's source produces
the attacker's artifact.

# What actually reduces exposure

Nothing prevents it outright. The controls are all about **shortening the window**:

- **[Cooldowns](/tools/update-cooldown.md)** — the single most effective one. Compromised releases
  are typically yanked within days; an automerging bot with no cooldown adopts them in minutes.
- **Pin and review.** A diff read by a person is the control that has actually caught these.
- **Consume `MAL-` records**, which cover published malicious packages rather than flawed
  ones.[^ossf-malicious]
- **Two-person publishing and hardware-backed tokens** on the publishing side, if you are the
  maintainer.

# The asymmetry worth internalising

A BOM, a signature and provenance together establish **what you have and where it came from**. None
of them establishes that **what came from there was benign.** That gap is the whole reason
maintainer compromise remains effective against otherwise well-instrumented pipelines.

# Related

- [Update cooldown](/tools/update-cooldown.md) — the practical mitigation
- [Sigstore](/provenance/sigstore.md) · [SLSA](/provenance/slsa.md) — what does *not* cover this
- [SLSA threat model](slsa-threat-model.md)

[^slsa-threats]: [SLSA v1.0: Supply chain threats](https://slsa.dev/spec/v1.0/threats)
[^ossf-malicious]: [OpenSSF: Detecting Malicious Packages Using the OSV API](https://openssf.org/blog/2026/05/20/detecting-malicious-packages-using-the-osv-api/)
