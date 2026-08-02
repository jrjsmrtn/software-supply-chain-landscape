# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Scope note**: this file records *releases*. Changes to the knowledge itself — concepts added,
re-verified, or expired — are in [`knowledge/log.md`](knowledge/log.md), which is the OKF-native
place for them.

## [Unreleased]

## [0.2.0] - 2026-08-02

**63 concepts.** Adds a `regulation/` directory — the causal layer the corpus was missing. It
explained every mechanism and never said who requires them, or by when.

Minor rather than patch: a new top-level directory and a new `type` value are additive changes a
consumer can see.

### Added

- **`knowledge/regulation/`**, admitted by one test recorded in the meta-project: an instrument is
  in scope only if it changes **what a bill of materials must contain, or when one must exist**.
  General cyber-security obligations that never reach the BOM are out of scope, and so is any
  question of whether an instrument applies to a given reader — that is legal advice, and every
  concept in the directory says so
- **`regulation/cra.md`** — Regulation (EU) 2024/2847, the Cyber Resilience Act. Sourced entirely
  from the enacting text on EUR-Lex rather than from commentary, which is a stricter sourcing rule
  than the rest of the bundle applies. Two findings that summaries routinely lose: the SBOM floor is
  **top-level dependencies only**, not the transitive graph; and the Regulation compels the document
  to *exist* and be producible on reasoned request, but not to be **published** — disclosure to
  users is explicitly optional
- The **`Regulation`** type. A regulation obliges rather than describes, so `Specification` was the
  wrong shelf

## [0.1.0] - 2026-08-02

First release: **62 concepts**, extracted from the `supplychain-workspace` meta-project into a
repository of their own. A bundle that cannot leave its parent cannot be fetched, and OKF names a
git repository as the recommended distribution unit.

**Tagged, not published.** This repository is private. Publication is a separate decision running
through its own gate, and a version tag does not pre-empt it.

### Added

- **The bundle.** 62 concepts across ten directories — `bom-types` (7), `disclosure` (2),
  `distribution` (2), `formats` (5), `intelligence` (11), `licensing` (5), `naming` (8),
  `provenance` (5), `threats` (5), `tools` (11) — plus `knowledge/landscape.md`, the
  read-straight-through explanation. It is carried as a concept (`type: Explanation`) rather than a
  separate document, so the bundle is one distribution unit instead of two halves that only make
  sense together
- **Per-claim provenance.** Every concept carries `sources` with keyed ids, footnotes that resolve
  to them, a `verified` trust tier and a `stale_after` expiry. 61 of 62 are verified; `landscape.md`
  is deliberately not, being durable rationale rather than a checkable fact
- **`stale_after` chosen per concept, not by default.** Five volatility tiers, from ~3 months for
  drafts under revision to ~24 months for durable rationale. An earlier state had 40 of 61 concepts
  sharing one date, which is what a default applied without thinking looks like
- **CC BY 4.0**, declared in `REUSE.toml` and enforced by `reuse lint`. The upstream source set was
  checked rather than assumed — Apache-2.0, CC0-1.0 and US government works — so no share-alike
  obligation propagates to consumers
- **Automated gates.** OKF conformance, footnote→`sources[].id` attribution in both directions,
  `stale_after` expiry, link resolution including bundle-relative `/`, and ISO 8601 dates in prose.
  They run on every commit and again weekly, because expiry is a function of today's date rather
  than of a diff and no commit hook can fire for it. The scripts live in the meta-project; the hook
  invokes them and fails loudly if it is absent rather than skipping
- `README.md`, `CHANGELOG.md`, and `knowledge/log.md` — which records content changes, while this
  file records releases

[Unreleased]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/releases/tag/v0.1.0
