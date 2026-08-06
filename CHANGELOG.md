# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Scope note**: this file records *releases*. Changes to the knowledge itself — concepts added,
re-verified, or expired — are in [`knowledge/log.md`](knowledge/log.md), which is the OKF-native
place for them.

## [Unreleased]

### Added

- **[CISA](knowledge/intelligence/cisa.md)** — referenced in four concepts, defined in none. The
  concept exists for the **authority gradient**: BOD 22-01 is *binding* on US federal civilian
  agencies with deadlines, the SBOM minimum elements were *authored* under an OMB designation, the
  VEX justifications were *published*, and the six SBOM types were only *facilitated* — a document
  that says "It is not an official US government document". Cited interchangeably, they read as one
  level of authority; they are three
  - Also **defines KEV**, which appeared in the corpus only as a bare word in `grype`'s capability
    table. Three inclusion criteria, all required — a CVE ID, reliable evidence of active
    exploitation, and **clear remediation guidance**; the third is why absence from KEV is not
    evidence of safety. Two-week and six-month deadlines by CVE vintage
- **[The six SBOM types](knowledge/formats/sbom-types.md)** — Design, Source, Build, Analyzed,
  Deployed, Runtime, from the CISA-facilitated 2023 document. The corpus covered the **xBOM family**
  (*what* is inventoried) and had **no coverage at all** of *where an SBOM's data came from*, which is
  what decides whether a given document can answer a given question
  - **It is not a lifecycle taxonomy** — the document disclaims that in its second paragraph, and the
    misreading matters: it implies a Runtime SBOM supersedes a Source SBOM, when in fact the two
    answer different questions and both stay valid
  - **"It is not an official US government document"** — a community-led working group that CISA
    facilitated, drafting led by Kate Stewart (Linux Foundation) and Melissa Rhodes (Medtronic)
  - Its minimum-content footnote still points at the **2021 NTIA** elements, which
    [`regulation/sbom-minimum-elements.md`](knowledge/regulation/sbom-minimum-elements.md) records as
    superseded by the 2026 edition
  - The limitations are recorded per type, because they are the half that changes decisions: **two
    SBOMs for one artifact can disagree while both are accurate**, and treating that as an error to
    reconcile destroys the information
  - Includes **how to declare a type in CycloneDX** via `metadata.lifecycles`, verified against
    `bom-1.6.schema.json`. The two vocabularies **do not align** — seven phases, six types, neither a
    subset of the other — and **Deployed and Runtime both collapse onto `operations`**, losing exactly
    the installed-versus-loaded distinction a consumer needs. The custom `name`/`description` form is
    the way out

## [0.7.0] - 2026-08-05

**Published.** The repository is public at
<https://github.com/jrjsmrtn/software-supply-chain-landscape>, having been private since
extraction on 2026-08-01 with publication always the stated point.

### Added

- **Pre-publication files**, ahead of the repository going public: `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md` and a root `LICENSE`. Adapted from the precedent set by
  `ai-contribution-policies`, which went through the `public-release` gate first
  - `CONTRIBUTING.md` states the sourcing rule with the evidence for it — re-verifying the CRA
    concept against the enacting text found a **wrong annexe citation** carried in confidence, and
    nothing but reading the instrument would have caught it. It also warns that a status code proves
    the server answered and never that the content arrived: EUR-Lex answers `202` with an empty body,
    and some hosts serve a challenge page for *any* path, including ones that do not exist
  - Contributions are accepted under the **DCO**, with no CLA — both instruments are documented in
    this bundle, which is a good reason to get our own use of them right
  - `SECURITY.md` is explicit that a documentation repository's real failure mode is a **wrong
    claim**, and names the class that matters most: a concept understating a security property such
    that someone trusts an artifact they should not

## [0.6.0] - 2026-08-05

### Added

- **Three `provenance/` concepts covering how a contribution's origin is asserted.** The corpus had
  none of them, while its sibling `ai-contribution-policies` leaned on all three to explain why
  organisations reading the same instruments reach opposite conclusions
  - **[Developer Certificate of Origin](knowledge/provenance/dco.md)** — clauses (a), (b) and (c) are
    *alternatives*, and only (a) mentions creating anything ("in whole or in part"). The common gloss
    "I wrote this" is not what the certificate says; the load-bearing assertion is the **right to
    submit under the stated licence**. Its text may not be modified, so a house variant is a
    contradiction rather than a stricter policy
  - **[Contributor License Agreement](knowledge/provenance/cla.md)** — worked from Apache's ICLA
    V2.2. Apache *licenses* and explicitly does not assign, but that is a property of Apache's
    agreement and not of the category. The operative clause is **§4, the employer representation**:
    a missing sign-off is fixable by amending a commit, a §4 problem needs the employer to act
  - **[Commit trailers](knowledge/provenance/commit-trailers.md)** — **git standardises the shape and
    nothing about the meaning**. Absorbs sign-off-chain semantics rather than giving them a record,
    since chain conventions are kernel practice while the mechanism is general

### Fixed

- **A wrong citation in the CRA concept**, found by re-verifying against the enacting text ahead of
  its 2026-09-01 expiry: the SBOM-on-reasoned-request provision is **Annex VII point 8, not Annex
  VIII point 8** — Annex VIII is Conformity Assessment Procedures and says nothing about SBOMs
- **`knowledge/log.md` violated OKF §9.** Earlier the same day its entries were re-headed by release
  (`## v0.5.0 — 2026-08-02`) to put a version inside the bundle. §9 requires date headings in ISO
  8601 `YYYY-MM-DD` form and admits no other, so that was 6 spec errors. The premise — that `log.md`
  bodies are unconstrained prose — was inferred from §5 instead of read from §9. Date headings are
  restored and the **release↔date map moved to the preamble**, which *is* unconstrained prose, so a
  detached `knowledge/` tree still names its version.
- **37 malformed `verified[].at` values**, carrying literal backslash-escaped quotes around the
  timestamp. Valid YAML, so `yaml.safe_load` accepted them and the local gates — which assert only
  that `type` is present — never inspected the value. None parsed as a timestamp (OKF §5.2).

Both found by **`okf validate` v0.2.1** (`okfcli/okf`), run against the bundle for the first time on
2026-08-03. The bundle now reports 0 errors and 0 findings.

### Changed

- **`okf validate` and `okf lint` are now the conformance gate** (ADR-0010). `check-doc-links.py`
  retired here — two implementations of one rule diverge silently, and this one was the weaker.
  `check-okf.py` stays, reduced to the two footnote-definition faults `okf` does not cover;
  `check-dates.py` stays because it checks files the bundle does not contain
- Recorded the **EUR-Lex fetch method** by pointer rather than copy: EUR-Lex answers HTTP 202 with an
  empty body to a non-browser client, so a `regulation/` re-verification silently degrades into a
  commentary check unless content negotiation on the CELEX resource is used
- Repaired an ordering fault found while regrouping: the five newest entries had been inserted into
  the middle of the **oldest** dated section, and one carried an inline date contradicting the
  heading above it. Entries are unchanged verbatim; only their grouping and order moved.

## [0.5.0] - 2026-08-02

**Corrections only — no new concepts, and minor rather than patch on purpose.** These do not repair
how the corpus says things; they change what it asserts. A consumer holding v0.4.0 has two concepts
describing a **retired** version of SLSA as current.

### Fixed

- **`provenance/slsa.md` and `threats/slsa-threat-model.md` were written against SLSA v1.1, which is
  retired.** `slsa.md` stated flatly that "v1.1 is current". Both are now verified against **v1.2**
- **SLSA now has a Source track** (`Source L1`–`L4`: version controlled; history and provenance;
  continuous technical controls; two-party review). This closes v1.1's own stated gap — *"SLSA does
  not yet address source threats, but we anticipate doing so in a future version"* — which both
  concepts had been asserting as current
- **The threat taxonomy is A–I, not A–H.** `(I) Usage` is new, and `(B)` was renamed from
  *Authoring & Reviewing* to *Modifying the source*. The letters have now moved twice; the concept
  says so rather than presenting the current set as settled
- Build Environment and Dependency tracks are **Working Draft only**, not in v1.2 — recorded so the
  draft's navigation is not mistaken for the release

### Changed

- Recorded that reviewer **collusion, "bugdoor" changes and rubber stamping are each explicitly
  "not currently addressed by SLSA"** within `(B)` — worth knowing before treating two-party review
  as a solved control
- Recorded that the specification's own overview page still describes dependency threats as
  "`A-H`, recursively" while its detail page enumerates `A`–`I`. Prefer the detail page
- Noted that a bare "SLSA Level 3" is **ambiguous between tracks** since v1.2, and almost always
  means Build L3

Unchanged, and re-confirmed: dependency threats and availability remain unaddressed in the same
words, and package selection (H) is still "not currently addressed" — so the argument that
typosquatting, dependency confusion and maintainer compromise live in categories SLSA leaves open
survives intact.

**How this was found matters more than what it was.** It surfaced by accident while researching a
sibling bundle, six months before either concept's `stale_after` would have prompted a re-check.
`stale_after` bounds how long an error can survive; it does not detect one.

## [0.4.0] - 2026-08-02

**65 concepts.** Completes the opening set of instruments in `regulation/`. With three in place, the
directory's real output is a comparison no single concept could carry: **they give three different
answers to what an SBOM must contain.**

| Instrument | Stated content floor |
|---|---|
| EU Cyber Resilience Act | at least the **top-level dependencies** |
| 2026 minimum elements | **17 named data fields** |
| FD&C Act §524B | **none stated** — only which kinds of component must be covered |

### Added

- **`regulation/fdc-act-524b.md`** — section 524B of the Federal Food, Drug, and Cosmetic Act,
  codified at 21 U.S.C. §360n-2, effective 2023-03-29. An SBOM is a condition of premarket
  submission for a "cyber device". Sourced from the codified statute, not from agency guidance
- The statute **states no content floor**, naming only commercial, open-source and off-the-shelf
  components. The floor is set below the statute, by guidance — and a reader who does not find one
  in the text should not conclude there is none
- Like the CRA, it directs the document **to an authority rather than to the customer**. Two
  jurisdictions, the same shape: neither compels publication to the people using the product

### Changed

- The CRA concept's `stale_after` moves from 2026-11-01 to **2026-09-01**. Its next milestone is
  2026-09-11, when reporting obligations begin, so the old date would have prompted a re-check two
  months after the fact it guards had already changed. An expiry that fires once a date has passed
  is checking the wrong thing
- FDA guidance elaborating §524B is **deliberately not tracked**: process for demonstrating
  compliance rather than a content requirement on a document, and faster-moving than the statute

## [0.3.0] - 2026-08-02

**64 concepts.** A second instrument in `regulation/`, and the contrast between the two is the
point: they set opposite content floors.

**If you hold a reference to "the NTIA minimum elements", it points at a superseded document.** The
2021 edition was replaced on 2026-07-29. The concept leads with this, because the old name is the
one still in circulation.

### Added

- **`regulation/sbom-minimum-elements.md`** — the **2026** edition, published 2026-07-29 by CISA
  with the NSA, FBI and sixteen international partner agencies. 17 data fields, up from the seven in
  the 2021 NTIA original it replaces, split into SBOM metadata and component data
- Where no producer can be determined, the document requires the author to **declare the component
  as being of unknown provenance** rather than omit the field. A declared gap and a silent omission
  are indistinguishable to a reader — the same argument as CycloneDX `compositions` and
  declared-versus-concluded licensing, and now cross-linked to both

### Changed

- The two instruments in `regulation/` now show a **17-field floor against a top-level-dependencies
  floor**. A document can satisfy the CRA comfortably and be thin against US federal procurement.
  That contrast only became visible once both were written

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

[Unreleased]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/jrjsmrtn/software-supply-chain-landscape/releases/tag/v0.1.0
