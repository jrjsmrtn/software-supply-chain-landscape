---
type: Tool
title: osv-scanner
description: The first-party OSV client — scans lockfiles, directories and images against osv.dev, with an offline mode and guided remediation.
resource: https://github.com/google/osv-scanner
tags:
  - tool
  - vulnerability
  - scanning
  - osv
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
  - id: osv-scanner-repo
    title: google/osv-scanner
    resource: https://github.com/google/osv-scanner
    last_modified: '2026-07-24'
---

The first-party client for [osv.dev](/intelligence/osv-dev.md), Apache-2.0. Written in Go, and the
reference implementation of "join what I have to what is known bad on
[purl](/naming/purl.md)".[^osv-scanner-repo]

| | |
|---|---|
| Scans | directories (recursively, for lockfiles and manifests such as `package.json`, `go.mod`, `pom.xml`), container images |
| Coverage | **11+ language ecosystems and 19+ lockfile types** — C/C++, Dart, Elixir, Go, Java, JavaScript, PHP, Python, R, Ruby, Rust |
| Data | osv.dev API (primary); deps.dev for dependency resolution, image scanning, licences and deprecation; package registries for native resolution |

The ecosystem and lockfile counts are upstream's own wording and the perishable part of this
concept.

# Two capabilities worth knowing

**Offline mode.** "Scan your project against a local OSV database. No network connection is
required after the initial database download." That matters for air-gapped builds and for making a
scan reproducible — a networked scan is not repeatable, because the database moves under it.

**Guided remediation.** Suggests version upgrades ranked by dependency depth, minimum severity, fix
strategy and return on investment — currently npm (`package-lock.json`, `package.json`) and Maven
(`pom.xml`). This is the one scanner here that tries to answer *what should I do* rather than only
*what is wrong*.

⚠ **It is labelled Experimental, and the `fix` command executes.** Upstream warns it "can be risky
when run on untrusted projects. It may trigger the package manager to execute scripts or follow
external registries specified in the project."[^osv-scanner-repo] That is the remediation step
reaching for the network and the shell on the strength of a manifest — the same surface
[dependency confusion](/threats/dependency-confusion.md) exploits, arriving through the tool you
brought in to close it. Read the manifest before running `fix` on code you did not write.

# Scope

Extraction is not its own: it is a CLI frontend over the **OSV-Scalibr** library, which is where
ecosystem coverage actually lives.[^osv-scanner-repo] So "does it support my ecosystem" is a
question about Scalibr, and a gap is a feature request against that boundary rather than this one.

It reads **package files**, so it sees declared dependency graphs rather than what is installed on
disk. [syft](syft.md) and [grype](grype.md) come at the same question from the artifact side. Which
is right depends on whether you are asking about the build or about the thing that shipped.

# Related

- [osv.dev](/intelligence/osv-dev.md) · [OSV schema](/intelligence/osv-schema.md) — the data behind it
- [grype](grype.md) · [trivy](trivy.md) — artifact-side alternatives

[^osv-scanner-repo]: [google/osv-scanner](https://github.com/google/osv-scanner)
