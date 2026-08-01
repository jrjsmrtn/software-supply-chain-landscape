---
type: Attack
title: Dependency confusion
description: A public package published under an internal package's name, selected by the resolver because its version is higher.
tags:
  - threat
  - registry
  - resolution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T21:35:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T21:35:00Z'
stale_after: 2027-08-01
sources:
  - id: birsan
    title: 'Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies'
    resource: https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610
    last_modified: '2021-02-09'
  - id: sonatype-depconf
    title: 'Sonatype: Why dependency confusion attacks are not going away'
    resource: https://www.sonatype.com/blog/why-are-dependency-confusion-attacks-not-going-away
---

An attacker publishes a package to a **public** registry using the name of a target's **internal**
package. The build then resolves to the attacker's copy.

Disclosed by Alex Birsan on **2021-02-09**, having reached more than 35 companies including Apple,
Microsoft, Tesla and Yelp, and earning over $130,000 in bounties.[^birsan][^sonatype-depconf]

# Why it works without exploiting anything

**Most package managers select the highest available version.** An internal `acme-utils` at `1.0.0`
against a public `acme-utils` at `9.9.9` resolves to the public one — no vulnerability, no
misconfiguration in the classical sense, just the resolver doing what it was designed to do.

The names are not secret either. Birsan harvested internal package names from GitHub, forum posts
and JavaScript files that list a project's dependencies.[^birsan]

This is SLSA threat **D**, and SLSA v1.0 does not address it — see
[the threat model](slsa-threat-model.md).

# Practice

The defences are resolution-side, not scanner-side:

- **Scope or namespace internal packages** (`@acme/utils`) so an unscoped public name cannot
  satisfy the dependency.
- **Pin, and install from a lockfile.** A resolver that never re-resolves cannot be confused.
- **Configure the registry, not just the client** — a proxy that refuses to fall through to a public
  upstream for names in an internal namespace removes the ambiguity entirely.
- **Claim your internal names publicly** as a defensive registration, where the registry allows it.

Note what does *not* help: a [BOM](/bom-types/sbom.md) records what you resolved, after the fact. It
makes the substitution auditable, not preventable.

# Related

- [SLSA threat model](slsa-threat-model.md) — threat D, out of scope for SLSA v1.0
- [Typosquatting](typosquatting.md) — the other name-based attack; that one needs a typo, this one
  does not
- [osv.dev](/intelligence/osv-dev.md) — `MAL-` records cover published malicious packages

[^birsan]: [Alex Birsan, *Dependency Confusion*](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
[^sonatype-depconf]: [Sonatype: why dependency confusion attacks are not going away](https://www.sonatype.com/blog/why-are-dependency-confusion-attacks-not-going-away)
