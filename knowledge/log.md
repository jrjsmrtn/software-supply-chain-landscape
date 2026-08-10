# Bundle Update Log

Content changes to the knowledge bundle: concepts added, re-verified, corrected or expired.

**Date headings, per OKF §9**, which requires ISO 8601 `YYYY-MM-DD` and admits no other heading form.
The log's model is date-grouped, not release-grouped, so an entry cannot carry its release in a
heading and five releases landing on one day share one. The release map below is how a `knowledge/`
tree separated from this repository still names its version: OKF has no in-band content-version
field, and a git tag does not travel with a copied directory.

**Releases**, newest first: **v0.11.0** 2026-08-11 (tooling only — no concept changed) · **v0.10.0** 2026-08-10 · **v0.9.0** 2026-08-07 · **v0.8.0** 2026-08-07 · **v0.7.0** 2026-08-05 · **v0.6.0** 2026-08-05 · **v0.5.0** 2026-08-02 · **v0.4.0** 2026-08-02 · **v0.3.0** 2026-08-02 ·
**v0.2.0** 2026-08-02 · **v0.1.0** 2026-08-02. Unreleased work sits at the top of the newest date.
[`../CHANGELOG.md`](../CHANGELOG.md) is the repository-level view of the same releases. <!-- audience-ok: an explicit repository-level pointer; a copied tree loses it by design -->

## 2026-08-10

* **Removed**: `landscape.md`'s *Relevance to This Workspace* section <!-- audience-ok: naming the removed section is the point of the entry -->, and four further passages
  across the bundle that addressed a maintainer rather than a reader. The bundle is published; that
  section was internal guidance that had travelled with the corpus out of the meta-project and was
  never re-scoped for a public audience.

  **The section named a specific private host and asserted a cryptographic weakness in it**, under a
  named GitHub account. It carried no hostname, so the secret-scanning rules never fired; the fault
  was prose, and prose is what those rules do not read. It also referred readers to five skill
  plugins — two of them in private repositories,
  which a reader cannot install, and pointed at `../reference/`, `../howto/` and `../adr/` — sibling
  directories that do not exist beside a distributed bundle, one of them a tier this log records as
  retired.

  **The same disclosure appeared twice**, and only one instance was found by reading. `bom-types/cbom.md`
  carried it as its worked line item; a `grep` for the phrase found both. That is the finding worth
  keeping: a leak stated in two voices reads as one sentence to a reviewer and as two hits to a
  pattern.

  Where an example was carrying its weight it was **generalised rather than deleted**, since the
  teaching was never the ownership:
  * `bom-types/cbom.md` — the CBOM line item now describes *a* self-hosted git server. The mapping
    to `assetType: protocol` is what the concept was demonstrating.
  * `provenance/cosign.md` — the v2→v3 bundle-format break is still recorded as observed in a real
    pipeline rather than read off a changelog, no longer sited in "this workspace's" project. <!-- audience-ok: quoting the removed phrase -->
  * `tools/syft.md` — contributing a cataloger is still "a real path rather than a theoretical one";
    the sibling project offered as evidence is gone.

  **These last two were fixed for the right reason and nearly recorded with the wrong one.** The
  first draft of this entry called both projects private. They are public — the note asserting
  otherwise had gone stale, and the check that caught it was `gh repo view`, run while assembling
  the checker's denylist. The fault in those two passages was never privacy; it was **deixis**. A
  reader holding a copied `knowledge/` tree has no workspace, so "this workspace's X" identifies <!-- audience-ok: quoting the removed phrase -->
  nothing, whatever X's visibility. Removing them was right; the first explanation for why was not.
  * `index.md` — the decision log is still declared private, no longer by repository name.

  Two references remain and are correct as they stand. This entry's own predecessor at 2026-08-01
  names the meta-project the bundle was extracted *from*; rewriting a dated entry to conceal that
  would falsify the record rather than close a leak. And `../CHANGELOG.md` in this file's preamble
  points outside `knowledge/` but inside the same public repository.

  **No gate would have caught any of this**, which was the part to fix rather than to note: `okf
  validate` and `okf lint` both report clean before and after, because every claim removed here was
  conformant, sourced, unexpired and false only in the sense of being addressed to the wrong reader.
  A checker for the class now runs on every commit and in the weekly sweep — three rules, deixis,
  private names and links leaving the bundle, with `<!-- audience-ok: why -->` for deliberate cases.
  It was proven by running it against the pre-fix tree, where it reports every passage removed here.

* **Corrected**: `threats/index.md`, three stale claims in one short file.
  * **"All three defeat the controls"** — there are **four**. `instruction-payloads` was added to
    this directory on 2026-08-02 and the sentence beneath the list was never re-counted.
  * The SLSA entry advertised **"the A-H taxonomy"** and **"threats SLSA v1.0 does not address"**.
    The concept it points at has been rewritten twice since — it is **A–I** and **v1.2**, and says
    so in its own `description`. The index kept describing the version the concept no longer covers.

  Both are the same defect: **a summary that restates what a neighbour says, and ages separately
  from it.** An index is the file most likely to be read and least likely to be re-read. Swept every
  other `index.md` for prose counts afterwards rather than assuming this was the only one — the
  other five hits are counts of *content* ("the six SBOM types", "five target types") that belong to
  a source and are correct.

* **Declared**: `Attack` in the type vocabulary, where it had been in use on the four `threats/`
  techniques without being listed. `okf` does not constrain the vocabulary and neither did anything
  else, so nothing contradicted anything — the list said ten types while the corpus used eleven.
  Recorded with the reason the type exists at all: a practice is something you adopt and an attack
  is something done to you, so filing these under `Practice` would flatten the distinction the
  concepts are about. `slsa-threat-model.md` stays a `Specification`; a taxonomy is a document.

## 2026-08-07

* **Added** to `landscape.md`, under *Common Misconceptions*: **"the organisation that published it is
  the organisation that wrote it"** — a pattern the corpus had recorded piecemeal eight times and
  never named.

  Recorded as **rationale rather than a concept**, deliberately. It has no source of its own — it
  would cite the eight already cited elsewhere — and no independent expiry, which is precisely the
  test `CLAUDE.md` sets for what belongs in `landscape.md` instead of the bundle. It is a reading
  skill for the rest of the corpus, not a new fact about the world.

  The instances, now collected in one place: CISA *facilitated* the six SBOM types (a document
  stating "It is not an official US government document", drafted from the Linux Foundation and
  Medtronic); SSVC is a CERT/CC model over which CISA runs a tree; EPSS is stewarded by a FIRST SIG
  while Empirical Security generates the scores; OMS is a format and `model-signing` one
  implementation; Sigstore is a project and `cosign` its client; OWASP develops CycloneDX while Ecma
  standardises it; the Linux Foundation develops SPDX while ISO/IEC standardises it; and a CNA
  assigns while an ADP enriches inside one CVE record.

  The rule it leaves the reader with: **ask who authored and who published separately before citing
  something as authority.** "CISA published" and "CISA requires" are different claims.


* **Added**: `intelligence/epss.md`, the last of the prioritisation terms the corpus used without
  defining — it appeared in `grype`'s capability table and in `cisa.md` and was nowhere explained.

  **A probability, not a severity**: the likelihood a CVE is exploited in the wild within the next 30
  days, scored 0–1 for every published CVE and **refreshed daily**. Recorded with the distinction most
  readers get wrong — `epss` is an absolute probability, `percentile` is a ranking against currently
  scored vulnerabilities, and a percentile of 0.9 can still be an absolute probability of a few
  percent.

  Three findings worth the space:
  * **The base rates explain the shape of the data.** KEV lists ~0.5% of published CVEs; EPSS observes
    exploitation activity in ~2.5–3% in any 30-day window. Scores clustering near zero is the model
    being *calibrated*, and it is why a high score is a strong signal.
  * **FIRST says KEV takes precedence over EPSS when present.** Not a claim about model quality — it is
    structural: EPSS predicts, KEV observes, and a prediction does not survive evidence.
  * **"EPSS is not a complete risk score"**, in FIRST's own words: no impact, no environment, no
    compensating controls. The same boundary SSVC draws from the other side.

  Ends by separating the four things called "prioritisation" — CVSS (how bad), EPSS (how likely), KEV
  (happening now), SSVC (what to do) — of which only the last produces a decision.

  **The residual gate earned its keep here.** `check-okf.py` failed the first draft on an orphan
  footnote definition: a source listed and cited nowhere, which renders as nothing. That is the exact
  fault the check exists for, and it was in freshly written prose that had already passed `okf lint`
  as a warning.

* **Added**: `intelligence/ssvc.md`, closing a term the corpus had begun to lean on: `adp.md` and
  `cisa.md` both referenced SSVC and neither defined it — the same dangling-term shape KEV had a day
  earlier.

  **SSVC is a CERT/CC (Carnegie Mellon) model**, not a CISA one; CISA operates a customised tree and
  publishes a guide for it. The same author-versus-operator distinction the corpus already draws for
  the six SBOM types, and worth stating for the same reason.

  The substantive point is what the name encodes. The five decision points split cleanly: **State of
  Exploitation, Technical Impact and Automatable are properties of the vulnerability** — anyone
  analysing it reaches the same answer — while **Mission Prevalence and Public Well-Being Impact are
  properties of your deployment**. That is exactly why the CISA ADP publishes only the first three
  into CVE records: a central publisher can answer questions about the flaw and cannot answer
  questions about your mission. The model is stakeholder-*specific* by construction.

  Two properties worth knowing before relying on the published values:
  * **There is no "unknown" value, deliberately.** Where evidence is thin CISA "identifies the value
    that is the most reasonable assumption based on prior events", qualifying that this "requires
    reliable historical evidence and future events may change these assumptions". So a decision point
    can be an assumption rather than an observation, which is defensible for a model that must always
    answer and a trap for a reader treating the values as measurements.
  * **Exploitation is present-tense with a shelf life** — it "does not predict future exploitation",
    reflects information at time of analysis, and "answers should be time-stamped".

  Also records the boundary against VEX, which sits beside it in this directory: VEX asks whether a
  vulnerability affects the product at all; SSVC asks what to do given that it does.

  `adp.md`'s bare external SSVC link now points at the concept, and says the three decision points are
  three of five.

## 2026-08-06

* **Added**: `intelligence/adp.md` — the **Authorized Data Publisher** role, which the corpus was
  missing while already covering [CNA](intelligence/cna.md). That left the CVE Program account as half
  a mechanism: who may *create* a record was documented, who may *add to* one was not — and SSVC
  scores, KEV membership and backfilled CPE strings all arrive by the second route.

  Sourced from the CVE Program's own page, reached with a **browser**: `cve.org` is a SPA and returns
  22 words to `curl`. A genuine JavaScript-rendering case, unlike the CISA KEV page it was checked
  against the same day.

  The mechanism is the container rule: an ADP **cannot modify** the CNA container and writes into a
  separate one, so a CVE Record is a set of containers each owned by its author, and every assertion
  stays attributable. Three further findings:
  * **There is exactly one active ADP** — CISA. "ADP" reads like a populated category and is not.
  * **Enrichment is rationed by triage.** Since 2024-02 every new record gets three SSVC decision
    points; only those scoring `Technical Impact: Total`, `Automatable: Yes`, or `Exploitation:
    Proof-Of-Concept`/`Active` *and* missing CVSS, CWE or CPE get the expensive second pass. The
    restraint is documented too — where a confident guess is impossible, CISA "will not venture such
    a guess", so a missing field can mean *nobody could tell* rather than *nobody looked*.
  * **Conflicts resolve by withdrawal, not precedence.** If a CNA later publishes its own CVSS, CWE
    or CPE, the ADP **removes** its assessed value from the record. Most enrichment pipelines
    accumulate opinions and leave the consumer to reconcile; here the third party stands down once
    the first party speaks, so no consumer implements precedence logic.

  Typed `Organization` to match `cna.md`, which the corpus already types that way despite CNA being a
  role rather than a body. Consistency chosen over precision so that filtering the type returns both
  CVE Program roles together.

  `cna.md` and `cisa.md` both gained a pointer: the first because its account was incomplete without
  the counterpart, the second because **KEV reaches consumers by two independent routes** — its own
  JSON feed and the CISA ADP container inside CVE records.

* **Added**: `intelligence/cisa.md` — the third `Organization` concept, alongside `cna` and `aegis`.
  CISA was referenced in four concepts and defined in none, and the four references sit at **three
  different points on an authority gradient** that the concept exists to record: BOD 22-01 is
  *binding* on US federal civilian agencies with deadlines; the SBOM minimum elements were *authored*
  under an OMB designation; the VEX status justifications were *published*; and the six SBOM types
  were merely *facilitated*, with the document stating "It is not an official US government document".
  A reader meeting those separately would reasonably assume they carry the same standing.

  It records KEV as a **published feed with a JSON Schema**, not only as prose: `requiredAction` and
  `dueDate` are *required* per record, so the BOD 22-01 deadline ships inside the data rather than
  being policy a consumer applies, and `cveID` is the join key that composes KEV with OSV, NVD and any
  CVE-resolvable BOM. `knownRansomwareCampaignUse` is a triage signal with no equivalent elsewhere.

  It also **defines KEV**, which the corpus previously contained only as a bare word in `grype`'s
  capability table. Three inclusion criteria, all required: a CVE ID, reliable evidence of active
  exploitation, **and clear remediation guidance** — the third being why absence from KEV is not
  evidence of safety. Deadlines of two weeks for CVEs from 2021 onward, six months for older.

  **Sourced from BOD 22-01, not the KEV landing page**, and the reason was established with a real
  browser rather than assumed. The first draft of this entry called that page JavaScript-rendered.
  It is not: the rendered DOM yields ~2,900 words — *fewer* than `curl` returns — and still contains
  no "BOD 22-01", "criteria" or "remediate". The page is a **catalog browser**, and the definitions
  were never on it in any representation. Citing the directive was right; the first explanation for
  why was wrong. The browser also surfaced the feed, CSV and schema URLs, which no `curl` of that
  page would have revealed.

* **Added**: `formats/sbom-types.md` — the six SBOM types (Design, Source, Build, Analyzed, Deployed,
  Runtime) from the 2023 CISA-facilitated document. A real gap: the corpus described the **xBOM
  family** in `bom-types/` — *what* is inventoried — and said nothing about *where an SBOM's data came
  from*, which is the axis that decides what a given document can be trusted to say. Zero mentions
  before this.

  Filed under `formats/` as a **Practice**, alongside `bom-completeness` and `bom-merging`, because
  it is a document-level property rather than a new BOM variant. Putting it in `bom-types/` would have
  conflated the two axes it exists to separate.

  Three findings that survive only by reading the document rather than a summary of it:
  * **It is not a lifecycle taxonomy**, and says so in its second paragraph: the list is "not intended
    to be tightly tied to the software lifecycle". The ordering invites the misreading, and the
    misreading has a consequence — it implies a Runtime SBOM supersedes a Source SBOM, when the two
    answer different questions and both remain valid.
  * **"It is not an official US government document."** Drafted by a community-led working group that
    CISA *facilitated*, led by Kate Stewart (Linux Foundation) and Melissa Rhodes (Medtronic).
    "CISA published" is accurate; "CISA says" is not.
  * Its footnote 1 anchors minimum content to the **2021 NTIA minimum elements**, an edition this
    corpus already records as superseded by the 2026 CISA one. The taxonomy rests on a baseline that
    has since moved, which does not invalidate the six types but is worth knowing when citing it.

  It also records **how to declare a type in a CycloneDX document** — `metadata.lifecycles`, verified
  against `bom-1.6.schema.json` rather than a capability page. The finding is that **the two
  vocabularies do not align**: seven phases against six types, neither a subset of the other, and
  Deployed and Runtime both collapse onto `operations`. That is the one distinction a consumer most
  needs — what is installed versus what actually loaded — and `phase` cannot express it, so the
  custom `name`/`description` form is the escape hatch. Prompted by a concrete case: `ansible-bom`
  emits a **Deployed** SBOM and currently declares no lifecycle at all.

  The operationally useful half is the limitations, recorded per type: Source can list components
  compiled out of the shipped artifact, Build may hold the wrong versions of dynamically linked
  dependencies, Analyzed is heuristic and is also the type you get when scanning someone else's
  binary, and Runtime sees only what has actually executed. Hence the synthesis the concept ends on:
  **two SBOMs for one artifact can disagree while both are accurate**, and reconciling them destroys
  the information.

## 2026-08-05

* **Added**: `provenance/dco.md` — the Developer Certificate of Origin. A real gap: the corpus had
  **no DCO concept and no mention of one**, while `ai-contribution-policies` leaned on the
  instrument throughout to explain why organisations reach opposite conclusions about AI-generated
  contributions. Mechanics belong here; the decisions organisations make with them belong there
  (ADR-0008's reference-don't-restate boundary, applied in the other direction).
* The record's point of leverage is that **(a), (b) and (c) are alternatives**, and only (a)
  mentions creating anything — "in whole or in part". The common gloss *"I wrote this"* is not what
  the certificate says; the load-bearing assertion is the **right to submit under the stated
  licence**, and (c) covers pure pass-through of work the signer neither wrote nor touched.
* Two things the text says that are easy to miss: it **may not be modified** ("changing it is not
  allowed"), so a house variant is a contradiction rather than a stricter policy; and clause (d) is
  a standing consent to **permanent publication of personal data**, which is why sign-off requires a
  known identity.
* Also records that multi-`Signed-off-by` chains are a **custody trail, not co-authorship** — later
  entries are "from people handling and transporting the patch, but were not involved in its
  development". Reading them as authorship misattributes work to maintainers who only forwarded it.
* **Added**: `provenance/cla.md` — closing the gap the DCO record had just named. Worked from
  Apache's **ICLA V2.2** read in full, because the category name predicts nothing: Apache
  *licenses* and explicitly does not assign (*"You reserve all right, title, and interest in and to
  Your Contributions"*), while other stewards assign or take relicensing rights. The record says so
  and refuses to generalise.
* The contrast that matters operationally is **§4, the employer clause**, not the licence grant. A
  missing `Signed-off-by` is fixable by amending a commit; a §4 problem needs *your employer* to
  waive rights or sign a Corporate CLA, which is weeks if it works at all. That is why a CLA belongs
  on a pre-work checklist and a DCO on a pre-merge one.
* The other real asymmetry: the ICLA grants **patent** licences with defensive termination; the DCO
  is silent on patents entirely. For a steward whose risk model includes patents, that gap — not
  authorship tracking — is the reason to require a CLA.
* **Added**: `provenance/commit-trailers.md` — absorbing the sign-off-chain material rather than
  giving it a record of its own, because chain conventions are kernel practice while the trailer
  *mechanism* is general. The framing fact: **git standardises the shape and nothing about the
  meaning**. `Signed-off-by:` has no more standing in git than `Banana:`; every semantic is project
  convention.
* Records git's actual parsing rules, which are stricter than they look — no whitespace in the key,
  the block must follow a blank line, and a group qualifies only if it is all trailers **or**
  *"contains at least one Git-generated or user-configured trailer and consists of at least 25%
  trailers"*. Prose mixed into the footer can drop a block below that threshold, at which point
  nothing in it is a trailer to tooling while it still reads correctly to a human.
* **A finding neither source states alone.** Guidance that circulated before the kernel's AI policy
  landed recommended `Co-developed-by:` for AI attribution. The kernel's own rules make that
  incoherent: `Co-developed-by:` denotes authorship and *"must be immediately followed by a
  Signed-off-by: of the associated co-author"*, while the AI policy states *"AI agents MUST NOT add
  Signed-off-by tags"*. The tag would require a sign-off the policy forbids — so `Assisted-by:` is
  the only shape consistent with both rules, not a stylistic preference. This is exactly the
  template the retired 27-project survey was shipping.
* Also found while sourcing: `submitting-patches.rst` carries a dedicated *"Using Assisted-by:"*
  section making the tag **required** — *"you need to acknowledge that use … Failure to do so may
  impede the acceptance of your work."* Stronger than `coding-assistants.rst` alone conveys, and it
  means a contributor following the ordinary submission process meets the requirement.
* And: naming a person in a trailer needs their **explicit permission**, for every token except
  `Cc:`, `Reported-by:` and `Suggested-by:`. A trailer publishes a permanent association between a
  named person and a change.
* A retrieval note worth keeping: `cla-corporate.txt` **no longer exists** and returns a one-line
  notice pointing at a PDF. The fetch succeeds; the agreement is not in it. Checking for clause text
  rather than HTTP status is what caught it.

## 2026-08-03

* **Re-verified**: `regulation/cra.md`, ahead of its 2026-09-01 expiry, against the enacting text
  from the Publications Office rather than commentary. EUR-Lex answers HTTP 202 with an empty body
  to a non-browser client, so the official XHTML manifestation was retrieved by content negotiation
  on the CELEX resource — worth recording, because "the primary source was unreachable" is otherwise
  how a re-verification quietly becomes a search-summary check.

  **One citation was wrong.** The SBOM-on-reasoned-request provision is **Annex VII point 8**, not
  Annex VIII point 8; Annex VIII is *Conformity Assessment Procedures* and says nothing about
  SBOMs. That also collapsed a table row: what were listed as two provisions — "technical
  documentation" and "market surveillance authority" — are one, since Annex VII *is* the technical
  documentation and its point 8 is conditioned on the request. **Article 53** added as the separate,
  broader access route.

  Confirmed verbatim and unchanged: the Article 3(39) definition; "at the very least the top-level
  dependencies" in Annex I Part II(1); Article 13(24)'s *implementing* act power over "the format
  and elements", under Article 62(2); Article 13(8)'s support period with "at least five years" and
  the shorter-expected-use carve-out; Annex II point 9's optional user disclosure, quoted in full;
  and all three Article 71 dates — 2026-06-11, 2026-09-11, 2027-12-11.

  **Re-tiered** from a milestone-tracking expiry to ~6 months (2027-02-01). The old rule — expire
  before the next application date — existed so a date would be re-checked before it passed. The
  dates are now primary-source verified and are fixed law, so nothing about them changes when
  2026-09-11 arrives. What can change at any time is the implementing act on SBOM format, and the
  expiry now follows that. Its absence is also the one claim here not checkable against the
  enacting text, which cannot report what it does not contain.

* **Corrected**: this log violated **OKF §9**, which requires date headings in ISO 8601
  `YYYY-MM-DD` form. It had been restructured earlier the same day to head entries by release
  (`## v0.5.0 — 2026-08-02`), on the incorrect premise that `log.md` bodies are unconstrained prose.
  The spec constrains the headings; the premise was inferred from §5 rather than read from §9. Found
  by `okf validate` v0.2.1, which reported 6 errors. Date headings restored, and the release map
  moved into the preamble, where it is prose and therefore conformant.
* **Corrected**: **37 `verified[].at` values** were malformed, carrying literal backslash-escaped
  quotes around the timestamp. Valid YAML, so `yaml.safe_load` accepted them and the local gates —
  which assert only that `type` is present — never inspected the value. None parsed as a timestamp.
  Also found by `okf validate` (OKF §5.2).

## 2026-08-02

* **Swept** 2026-08-02: a **version-currency check** across every concept citing a versioned
  specification — asking only *"is the cited version still the current one?"*, which is a different
  question from *"is this claim accurate?"* and is the one the 2026-08-01 verification pass never
  asked. That pass checked SLSA claims against v1.1 pages without noticing v1.1 had been retired.

  Confirmed current at source: **CycloneDX 1.7.1**, **SPDX 3.0.1**, **OpenVEX v0.2.0**,
  **model-signing v1.1.1**, **cosign v3.1.2**, **REUSE 3.3** (confirmed by `reuse lint` itself),
  and **CSAF** — 2.0 established with 2.1 at committee-specification-draft-02, which is what
  `intelligence/csaf-vex.md` already says. `naming/purl.md` cites ECMA-427 without claiming an
  edition, so its 1st edition of 2025-12 contradicts nothing.

  **Not confirmed**: CPE 2.3. NIST's product page states API schema versions rather than the
  specification version, and no better source was checked. Recorded as unverified rather than
  assumed stable.

  Outcome: **SLSA was the only stale version claim**, and it was already corrected. This entry
  exists so the negative result is dated and does not get redone blindly.

* **Corrected**: `provenance/slsa.md` and `threats/slsa-threat-model.md`, both written against
  **v1.1 — which is retired**. `slsa.md` stated flatly that "v1.1 is current". Found by accident
  while researching a different bundle, six months before either concept's `stale_after` would have
  prompted a re-check. v1.2 adds a **Source track** (`Source L1`–`L4`), which closes v1.1's stated
  gap that "SLSA does not yet address source threats"; the threat taxonomy gains a ninth letter,
  **(I) Usage**, and renames (B) from *Authoring & Reviewing* to *Modifying the source*. Dependency
  and availability threats remain unaddressed, and a Dependency track exists only in the Working
  Draft. Also recorded: the spec's own overview page still says dependency threats are "A-H,
  recursively" while its detail page enumerates A–I.

* **Added**: `regulation/fdc-act-524b.md`, completing the opening set named in the scope decision.
  Sourced from the codified statute at 21 U.S.C. §360n-2 rather than from FDA guidance — an early
  attempt landed on a webinar deck about a superseded 2024 draft, which is what the primary-source
  rule is for. The finding is a negative one: the statute states **no content floor at all**, naming
  only which kinds of component must be covered, so the three instruments now in this directory give
  three different answers to "what must an SBOM contain". Like the CRA, it directs the document to
  an authority rather than to the customer.

* **Added**: `regulation/sbom-minimum-elements.md`. Written as the **2026** edition, not the 2021
  NTIA one: CISA, with the NSA, FBI and sixteen international partners, published a replacement on
  2026-07-29 — four days before the scope ADR named the superseded document as a candidate. The
  count roughly doubled to 17 data fields, `Supplier Name` became `Component Producer` with the
  ambiguity acknowledged rather than fixed, and SWID tags were dropped as not widely used. Its
  instruction to declare unknown provenance explicitly is the same principle as CycloneDX
  `compositions` and declared-versus-concluded licensing.

* **Added**: `regulation/` and its first concept, `regulation/cra.md`, under a scope test recorded
  in the meta-project: an instrument is in scope only if it changes what a bill of materials must
  contain or when one must exist. Sourced entirely from the enacting text on EUR-Lex rather than
  from commentary, which is a stricter rule than the rest of the bundle applies. Two findings worth
  the space: the Regulation's SBOM floor is **top-level dependencies only**, not the transitive
  graph, and it compels the document to exist without compelling its publication — disclosure to
  users is explicitly optional under Annex II point 9. Introduces the `Regulation` type.

* **Added**: `intelligence/repology.md` — the version-currency axis, which neither `osv.dev`
  (vulnerabilities) nor `endoflife.date` (support dates) covers: how far behind upstream an
  installed packaging is. It also records the project-versus-package distinction as a worked answer
  to identity *across* ecosystems, which purl deliberately does not attempt. Sourced against the
  API docs and statistics page; two limits worth the space are that its data carries no declared
  licence, and that distro backporting makes `outdated` a signal rather than a verdict.

* **Every fact-bearing concept is now verified** — 60 of 61. Only `landscape.md` carries no
  `verified` entry, which is correct: it is durable rationale, and its claims are arguments rather
  than facts with sources to re-check.
* **Re-tiered**: `provenance/slsa` and `threats/slsa-threat-model` moved from ~12 months to
  ~6 months. The tier was assigned on the reasoning that ratified specifications do not move; SLSA
  then turned out to have shipped v1.1 and rewritten its threat taxonomy. "Ratified" is a weaker
  guarantee than it sounds when a specification is actively developed.
* **Last five verified**, with four enrichments:
  * `licensing/spdx-license-list` — the superseded `+` forms are **still on the list**, flagged
    `isDeprecatedLicenseId` (32 of 733 identifiers). Encountering `GPL-3.0` means a deprecated
    identifier was used, not an invented one — and the ambiguity `-only` exists to remove is back.
  * `provenance/in-toto` — a Statement's `subject` is a **required array of ResourceDescriptor
    objects**, so one attestation can cover several artifacts; `predicateType` is a URI.
  * `licensing/copyleft-floor` — AGPL-3.0 §13 quoted by its actual heading, *"Remote Network
    Interaction"*. The trigger is interaction over a network, not distribution of a binary.
  * `naming/cpe` — current specification **CPE 2.3**.

* **Re-verified**: the ~12 month tier, 24 of 29. The most consequential correction of the review:
  * **SLSA v1.1 reassigned the threat letters**, and `threats/slsa-threat-model` documented v1.0.
    `D` was *use compromised dependency* and is now *External Build Parameters*; `G` was *compromise
    package registry* and is now *Distribution Channel*, which v1.1 **partially addresses** through
    consumer verification. Anyone citing "SLSA threat D" from the old concept would have meant
    something the current specification does not. Rewritten for v1.1, with the reassignment called
    out, and the citing concepts repointed.
  * **`H` in v1.1 is *Package Selection* — typosquatting and naming confusion** — and SLSA states
    *"this threat is not currently addressed by SLSA."* The specification now names the gap this
    subdirectory was created to fill.
  * `provenance/slsa` still said v1.0 was current. It is v1.1.
  * `formats/bom-completeness` listed **six** `aggregate` values; the schema has **ten**. The four
    omitted are the proprietary/open-source splits, which are what let a BOM say *we enumerated our
    open-source dependencies and not our commercial ones*.
  * `naming/bom-link` described one URN form with an optional fragment. The schema defines **two
    distinct types**, with the serial number a UUID and the version a positive integer.
  * `intelligence/osv-schema` omitted the record lifecycle fields, including **`withdrawn`** — a
    scanner ignoring it keeps reporting advisories the database has retracted.
  * `licensing/reuse` — specification version recorded: **REUSE 3.3**.
  * **Five left unverified**: `copyleft-floor`, `declared-vs-concluded`, `spdx-license-list`, `cpe`,
    `in-toto`. Their claims were not re-checked this round.

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

## 2026-08-01

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

* **Extracted**: the bundle moved out of the `supplychain-workspace` meta-project into this <!-- audience-ok: dated historical entry; rewriting it to conceal the source would falsify the record -->
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
