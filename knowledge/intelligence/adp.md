---
type: Organization
title: ADP (Authorized Data Publisher)
description: The other role in the CVE Program — enrich a record without touching what the CNA wrote. Two containers, no overwrite, and conflicts resolved by withdrawal rather than precedence.
resource: https://www.cve.org/ProgramOrganization/ADPs
tags:
  - cve
  - vulnerability
  - enrichment
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-06T22:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-06T22:20:00Z'
  - by: claude/opus-5
    at: '2026-09-04T14:20:00Z'
stale_after: 2027-03-04
sources:
  - id: cve-adp
    title: 'CVE Program: Authorized Data Publishers (ADPs)'
    resource: https://www.cve.org/ProgramOrganization/ADPs
  - id: vulnrichment
    title: cisagov/vulnrichment
    resource: https://github.com/cisagov/vulnrichment
---

A [CNA](cna.md) decides *who may assign a CVE ID and describe the vulnerability*. An **ADP** is the
other role: an organisation authorised to **enrich a record someone else published**, with risk
scores, references, vulnerability characteristics or translations.[^cve-adp]

An ADP "focuses on specific informational elements, agreed upon with the CVE Program, as the scope
of that ADP's contributions" — so an ADP is not licensed to add anything it likes.[^cve-adp]

> ⚠ **A quotation correction.** Earlier revisions ended that quotation *and approved by the CVE
> Board*. **The ADP page does not contain that clause.** It appears in the CVE Program's *CNA
> Operational Rules*, about how those rules themselves are maintained — a real phrase from a
> different document, spliced onto a sentence it does not belong to. Checked 2026-09-04 against the
> rendered page, the roster page being a JavaScript application that serves no text to a plain
> fetch. A wrong clause inside quotation marks is the worst failure this corpus can have: it is
> citable, it reads as authoritative, and nothing downstream catches it.

# The container rule is the whole mechanism

Three sentences from the CVE Program carry the design:[^cve-adp]

> An ADP augments the information in a CVE Record
> An ADP **cannot modify** the data the CNA has published in their "CNA container"
> All ADP updates to the CVE Records occur in a separate organizational "**ADP container**"

**A CVE Record is not one document with one author.** It is a set of containers, each owned by the
party that wrote it. Enrichment is additive and attributable: a consumer can always tell which
assertion came from the vendor who owns the vulnerability and which came from a third party scoring
it afterwards.

That distinction is what makes the whole arrangement safe. Without it, "enrichment" would mean a
third party silently editing a vendor's advisory.

# There is currently one active ADP

CISA.[^cve-adp] Worth stating plainly, because "ADP" reads like a populated category and is not —
the role exists in the CVE Program's design and one organisation occupies it. That number is the most
likely thing on this page to change.

The **CISA ADP** contributes three things:[^cve-adp]

- **[SSVC](ssvc.md) decision points** — Exploitation, Automatable, Technical Impact. Note these are
  three of five: the other two are stakeholder-specific and no central publisher can supply them
- **[KEV](cisa.md) catalog data**
- **"Vulnrichment"** — missing CVSS, CWE or CPE for records meeting specific threat characteristics

Note the second: **KEV reaches CVE records through the ADP container**, not only through its own
[JSON feed](cisa.md). The same fact arrives by two routes, and a consumer reading enriched CVE data
gets it without querying CISA separately.

# Two passes, and a threshold

Since **2024-02**, for every newly published CVE Record:[^cve-adp]

**First pass — universal.** The three SSVC decision points are published for *all* new records.

**Second pass — conditional.** A record qualifies if it scores at least one of `Technical Impact:
Total`, `Automatable: Yes`, `Exploitation: Proof-Of-Concept`, or `Exploitation: Active`, **and** is
missing CVSS, CWE or CPE. Only then does CISA analyse further and supply the missing metric.

Two properties of this worth noticing:

- **Enrichment is rationed by triage, not applied uniformly.** The expensive analysis follows the
  cheap signal. A record nobody scores as risky keeps its gaps.
- **Restraint is documented.** "In some rare cases, it may be impossible to confidently field a guess
  on CVSS, CWE, or CPE. In those cases, the CISA ADP will not venture such a guess."[^cve-adp] A
  missing field can mean *nobody could tell*, which is different from *nobody looked*.

# Conflicts resolve by withdrawal

The rule that distinguishes this from most data-merging schemes:[^cve-adp]

> If a CNA later updates a CVE Record with their own CVSS, CWE, or CPE data, the CISA ADP will
> **remove** their assessed metrics for those specific elements from the updated CVE Record.

Not "the CNA wins at read time" — the ADP value is *withdrawn from the record*. The stated purpose is
to "reduce duplicate (and conflicting) data within the CVE Record", and where both are somehow present
"the originating CNA's data should take precedence".

**This is the opposite of how most enrichment pipelines behave.** The common pattern accumulates
opinions and leaves the consumer to reconcile them. Here the third party stands down once the
first party speaks — which means a consumer never has to implement precedence logic, because the
conflict is resolved before the data reaches them.

# Why this belongs in a supply-chain reference

The corpus already explains [who may assign a CVE ID](cna.md). Without the ADP role that account is
half a mechanism: it describes who *creates* a record and is silent on who may *add to* one, which is
where SSVC scores, KEV membership and backfilled CPE strings actually come from. Anyone reasoning
about why a CVE record contains what it contains needs both halves.

CISA's own repository is explicit that consumers "need not fork and track this GitHub repo if they are
already consuming live CVE data" — the enrichment is pushed back into the CVE corpus.[^vulnrichment]

# Related

- [CNA](cna.md) — the other CVE Program role: who may assign an ID
- [CISA](cisa.md) — the one active ADP, and the KEV catalog it publishes by both routes
- [NVD](nvd.md) — the other enrichment layer over CVE, run by a different agency and predating this
- [CPE](/naming/cpe.md) — one of the identifiers the second pass backfills

[^cve-adp]: [CVE Program: Authorized Data Publishers (ADPs)](https://www.cve.org/ProgramOrganization/ADPs)
[^vulnrichment]: [cisagov/vulnrichment](https://github.com/cisagov/vulnrichment)
