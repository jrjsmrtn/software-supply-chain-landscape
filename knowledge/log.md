# Bundle Update Log

Content changes to the knowledge bundle: concepts added, re-verified, corrected or expired.
Releases are in [`../CHANGELOG.md`](../CHANGELOG.md).

## 2026-08-01

* **Added**: `threats/` (4 concepts) — the SLSA A–H threat taxonomy, dependency confusion,
  typosquatting, maintainer compromise. Fills the corpus's largest hole: 56 concepts described
  artifacts, named them and reported known-bad, and said nothing about how hostile code *enters* a
  dependency graph. Anchored on SLSA's own statement that v1.0 does not address threats A, B, C, D
  or G — the bundle had inherited SLSA's blind spot.
* **Corrected**: `naming/osv-ids.md` omitted the `MAL-` prefix. OpenSSF's malicious-packages
  records are served through the same OSV API but assert something different — *this package is
  hostile*, with no fixed version to upgrade to. A scanner that does not distinguish them from
  `PYSEC-`/`GHSA-` advisories invites the wrong remedy.

* **Extracted**: the bundle moved out of the `supplychain-workspace` meta-project into this
  repository, so it can be distributed. Cross-document links converted to bundle-relative form.
* **Added**: `landscape.md` as a `type: Explanation` concept — previously a separate Diátaxis
  document outside the bundle. It now carries `sources` and a long `stale_after`, and is checked
  by the same gates as everything else.
* **Corrected**: `bom-types/cbom.md` — verified `cryptoProperties.assetType` against the CycloneDX
  1.6 and 1.7 JSON schemas. Protocols **are** a first-class asset type, and "keys" is not one;
  keys are `related-crypto-material`. The capability page lists three of the four.
* **Restored**: six sources dropped during migration, each the specific page supporting a claim
  rather than a project homepage — osv.dev's data-sources page, CISA's VEX status-justification
  document, the OpenVEX specification, CycloneDX's VEX and VDR capability pages, and
  endoflife.date's v1 API docs. One CISA URL written from memory was removed.
* **Added**: `bom-types/` (7 concepts) and the six remaining `tools/` concepts, sourced against
  CycloneDX capability pages and upstream repositories. `MBOM` was missing from this corpus
  entirely; `HBOM` covers firmware; `OBOM` is full-stack.
* **Added**: the initial migration — 38 concepts across `naming/`, `licensing/`, `formats/`,
  `intelligence/`, `tools/`, `provenance/` and `distribution/`, from the retired reference tier.
