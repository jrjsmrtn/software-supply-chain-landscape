# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Scope note**: this file records *releases*. Changes to the knowledge itself — concepts added,
re-verified, or expired — are in [`knowledge/log.md`](knowledge/log.md), which is the OKF-native
place for them.

## [Unreleased]

### Added

- Extracted from the `supplychain-workspace` meta-project as an independent repository, so the
  bundle can actually be distributed. A bundle that cannot leave its parent cannot be fetched, and
  OKF names a git repository as the recommended distribution unit
- **CC BY 4.0** for knowledge and documentation, **Apache-2.0** for the scripts, declared per-file
  in `REUSE.toml` and enforced by `reuse lint`. The upstream source set is permissive throughout —
  Apache-2.0, CC0-1.0 and US government works — with no share-alike obligation to propagate
- `README.md`, `CHANGELOG.md`, and `knowledge/log.md`
- `reuse lint` in the pre-commit gate, alongside `gitleaks`. The bundle checks — OKF conformance,
  footnote attribution, `stale_after` expiry, links, ISO dates — run from the meta-project, pointed
  here. **A known weakness**: a gate that lives apart from what it checks can silently stop
  running, so running them is a deliberate act before publishing

### Changed

- **This repository carries knowledge and nothing else.** The checking scripts and the decision log
  were moved into the meta-project it was extracted from: both reason about private repositories,
  and this one is meant to be publishable. What ships is the bundle plus the metadata a consumer
  needs — README, changelog, licence
- **Single-licensed CC BY 4.0** as a result. With the scripts gone there is no Apache-2.0 component
  and no mixed-licence question
- **The landscape explanation is now a bundle concept** (`knowledge/landscape.md`,
  `type: Explanation`) rather than a separate Diátaxis document. It gains the attribution and expiry
  gates it previously escaped, and the bundle becomes one distribution unit instead of two halves
  that had to be fetched together to make sense
- All cross-document links converted to bundle-relative form
