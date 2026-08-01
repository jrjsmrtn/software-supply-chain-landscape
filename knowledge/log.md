# Bundle Update Log

Content changes to the knowledge bundle: concepts added, re-verified, corrected or expired.
Releases are in [`../CHANGELOG.md`](../CHANGELOG.md).

## 2026-08-02

* **Re-verified**: `distribution/tea` and `distribution/tei` — the two nearest expiry, and the two
  that had never been checked. The largest single improvement of the day:
  * **`tei` now documents its syntax.** The concept previously said the identifier syntax was
    "deliberately not restated" because it was a moving target, and recorded that as the thing to
    fill in once it settled. It has: `urn:tei:<type>:<domain-name>:<unique-identifier>`, with types
    including `purl`, `swid` and `uuid`, and resolution through DNS (`A`/`AAAA`/`CNAME`) to a
    `/.well-known/tea` endpoint over validated HTTPS. IANA registration of the URN scheme is still
    outstanding. A purl nests *inside* a TEI as its identifier component — TEI names a release,
    purl names a component.
  * **`tea`'s object model was missing two levels.** It listed Product / Component / Collection /
    Artifact and omitted **Product Release** — which is the primary entry point a TEI resolves
    to — and **Release** (Component Release).
  * **Beta 2 confirmed** from the specification repository, with the consequence made explicit:
    the beta covers the *consumer* side only, and publisher-API work begins after 1.0. A consumer
    can be built now; a publisher cannot. Note also that only `0.1.0-beta.1` is tagged, so the
    status cannot be read from the release list.
  * `landscape.md` updated to match, replacing the passage that said the syntax was too unstable to
    restate.

* **Re-verified**: the last five of the ~6 month tier — `nvd`, `vdr`, `csaf-vex`, `dependabot`,
  `renovate`. **Both short tiers are now fully verified.** One sourcing correction and three
  enrichments:
  * `intelligence/vdr` and `landscape.md` gave VDR *"a lineage in NIST and EO 14028"*, attributed
    to the CycloneDX VDR capability page. **That page says no such thing** — it cites
    **ISO/IEC 29147:2018** and mentions neither NIST nor the Executive Order. The claim may be
    defensible in US policy terms but it was sourced to a document that does not carry it. Both
    places corrected.
  * `tools/dependabot` — the `cooldown` block named properly: `default-days` plus per-bump
    `semver-major-days` / `semver-minor-days` / `semver-patch-days`, and `include` / `exclude`
    lists up to 150 entries.
  * `tools/update-cooldown` — "both exempt security updates by default" understated it. For
    Dependabot the boundary is structural: *"The `cooldown` option is only available for version
    updates, not security updates."* It cannot delay a security fix even by misconfiguration.
  * `intelligence/csaf-vex` — CSAF **2.0** established with an errata revision, **2.1** under
    development alongside it.
  * Confirmed unchanged: Renovate AGPL-3.0 with `minimumReleaseAge` still the option name; NVD's
    role as CVE enrichment carrying CPE applicability and CVSS.

* **Re-verified**: the ~6 month tier, 10 of 15 concepts. Four enrichments and one correction:
  * `naming/purl-type-definitions` — **42 registered types**. `huggingface` and `mlflow` are
    among them, so a model is nameable with a purl and an ML-BOM joins on the same key as
    everything else. `ansible` still is not, which is the premise of
    `provisional-purl-identifiers`.
  * `formats/cyclonedx` — current specification **1.7.1** (2026-06-02) recorded; the concept gave
    only the Ecma standard number.
  * `tools/scorecard` — the check table omitted **`SBOM`**, the check most directly about this
    bundle's subject.
  * `intelligence/openvex` — specification **v0.2.0**, CC0-1.0.
  * `intelligence/aegis` — the 3-month embargo is now quoted from the CNA's own security policy.
    The **2025-05 authorization month is not stated on the CNA's own pages**; the concept now says
    it is secondary-sourced rather than presenting it as primary.
  * Verified against **schemas rather than capability pages**, after a capability page proved
    incomplete on SPDX: the CycloneDX `impactAnalysisState` and `impactAnalysisJustification` enums
    match `bom-1.7.schema.json` exactly, and the OpenVEX status values match `OPENVEX-SPEC.md`.
  * **Five concepts were deliberately left unverified** — `nvd`, `vdr`, `csaf-vex`, `dependabot`,
    `renovate`. Their claims were not re-checked this round, so no `verified` entry was added.
    Stamping them would have made the field mean "someone looked at the tier" rather than "someone
    checked this concept".

* **Re-verified**: the ~4 month tier, all 14 concepts. Six of the seven that had never carried a
  `verified` entry were checked against upstream and now do; the seventh (`osv-scanner`) already
  did. Three corrections resulted:
  * `tools/dependency-track` — 5.0.3 → **5.0.4**, released 2026-07-30. One day after the concept
    was written, which is precisely the decay rate this tier exists for.
  * `intelligence/osv-dev` — "roughly two dozen sources" overstated it; **around twenty** current,
    plus three conversion pipelines. The source list corroborates two other concepts: OpenSSF
    Malicious Packages (`MAL-`) and the Erlang Ecosystem Foundation CNA are both in it.
  * `licensing/spdx-license-expression` — the caveat "the spec version that introduced
    `acknowledgement` was not confirmed" is **resolved**: absent in `bom-1.5.schema.json`, present
    in 1.6 and 1.7, so **introduced in CycloneDX 1.6**. A tool emitting 1.5 cannot express
    declared-versus-concluded at all.
  * Unchanged and confirmed: purl-spec#854 still open and unmerged (last activity 2026-06-09),
    OWASP Agentic Skills Top 10 still at v1 public review, osv-scanner still "11+ language
    ecosystems and 19+ lockfile types", `model-signing` still 1.1.1, cosign v3 bundle format
    current at 3.1.2.
  * `intelligence/endoflife-date` — product count tightened to **462**, but its API's *beta* status
    could not be re-confirmed and the concept now says so rather than repeating it.

* **Reviewed**: every `stale_after` date. 40 of 61 concepts shared `2027-02-01` — a default reached
  for rather than a judgement made. Reassigned 25 by volatility class: tool capability claims and
  `instruction-payloads` (OWASP AST10 is at v1 public review) pulled in to ~4 months; BOM-type
  definitions, attack mechanics, ratified specs and structural mechanisms pushed out to ~12 months.
  The tiers are now written down in `CLAUDE.md` so the next concept gets assigned deliberately.
  **No content was re-verified and no `verified` entry was added** — moving a date because the
  volatility class was misjudged is not the same act as re-checking a claim, and only the second
  earns a `verified` entry.

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
