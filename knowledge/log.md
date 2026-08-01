# Bundle Update Log

Content changes to the knowledge bundle: concepts added, re-verified, corrected or expired.
Releases are in [`../CHANGELOG.md`](../CHANGELOG.md).

## 2026-08-02

* **Added**: `threats/instruction-payloads.md` — artifacts whose payload is natural-language
  instructions rather than code. Scope for agent skills was decided deliberately rather than by
  accumulation: the artifact *class* is in scope, the vendor and runtime landscape is not. The
  boundary and its test are recorded in the meta-project's ADR-0007.

## 2026-08-01

* **Added**: `disclosure/` (2 concepts) — model cards (Mitchell et al. 2019) and datasheets for
  datasets (Gebru et al.). Deliberately a new subdirectory rather than filed under `bom-types/`:
  a BOM says what an artifact is *made of*, a card says what it is *for*. Placing them together
  would have blurred the distinction the concepts exist to draw. It is also where the identified
  AI-governance gap (EU AI Act, NIST AI RMF) will go.

* **Added**: `provenance/model-signing.md` — the Sigstore project's tool for signing a *directory
  tree*, by hashing every component into a manifest and signing that. Fills a real gap: `cosign`
  signs one blob or image, and a model, a skill and an OKF bundle are all trees of files. Four
  signing methods including keyless OIDC and PKCS #11. Records that OMS is the format and
  `model-signing` one implementation — the Sigstore/cosign separation again. NVIDIA uses it to sign
  agent skills, which is the evidence that it is not model-specific.

* **Added**: `formats/spdx-ai-profile.md` — SPDX 3.0's AI and Dataset profiles. Where CycloneDX has
  one ML-BOM, SPDX has two: the model and the data it was trained on. Six energy properties split
  by training/fine-tuning/inference, and structured governance fields (`knownBias`,
  `safetyRiskAssessment`, `modelExplainability`, `anonymizationMethodUsed`) that CycloneDX carries
  only as narrative.
* **Corrected**: `formats/spdx.md`, `intelligence/vex.md` and `landscape.md` all stated that SPDX
  handles VEX by "separate mechanisms". **False since 3.0** — the Security profile defines twelve
  VEX relationship classes, a `justificationType` property and a `VexJustificationType` vocabulary.
  That was the most-cited reason to prefer CycloneDX for triage. `vex.md` now documents three
  justification vocabularies rather than two.
* **Reframed**: CycloneDX versus SPDX is no longer presented as a choice with an audience-based
  tiebreak. Their scopes are complementary — CycloneDX stronger on the build (graph, completeness,
  one schema for the family), SPDX stronger on models, datasets and licence precision. Emitting both
  for different subjects is legitimate; emitting both for the same subject is the thing to avoid.

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
