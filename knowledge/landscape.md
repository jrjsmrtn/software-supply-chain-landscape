---
type: Explanation
title: Understanding the Software Supply Chain Landscape
description: Why the supply-chain security landscape exists, what each piece is for, and how they compose — the durable rationale behind every concept in this bundle.
tags:
  - explanation
  - orientation
  - supply-chain
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:50:00Z'
stale_after: 2028-08-01
sources:
  - id: cyclonedx
    title: CycloneDX
    resource: https://cyclonedx.org/
  - id: spdx
    title: SPDX
    resource: https://spdx.dev/
  - id: purl-spec
    title: Package URL specification
    resource: https://github.com/package-url/purl-spec
  - id: slsa
    title: SLSA
    resource: https://slsa.dev/
  - id: in-toto
    title: in-toto
    resource: https://in-toto.io/
  - id: sigstore
    title: Sigstore
    resource: https://www.sigstore.dev/
  - id: osv
    title: OSV
    resource: https://osv.dev/
  - id: endoflife-date
    title: endoflife.date
    resource: https://endoflife.date/
  - id: openssf
    title: OpenSSF
    resource: https://openssf.org/
  - id: tea
    title: Transparency Exchange API
    resource: https://github.com/CycloneDX/transparency-exchange-api
---

# Understanding the Software Supply Chain Landscape

> **This is the one document to read straight through.** Everything else in this bundle is a
> concept you look *up*; this is the map that makes the concepts make sense when you meet them.
> It carries a deliberately long `stale_after`: it is durable rationale, and should need review
> only when the landscape's shape changes rather than when a version number does.

> **A word used deliberately.** This bundle says **landscape** for the terrain surveyed here, and
> reserves **ecosystem** for a *package* ecosystem — npm, PyPI, Hex, crates.io. `ecosystem` is a
> field name in the OSV schema and the thing purl's `type` selects, so "coverage varies by
> ecosystem" is a precise claim about package ecosystems, not a vague one about the industry.

## Introduction

Almost everything you run is assembled from code written by strangers. A modest application
pulls in hundreds of transitive dependencies, built by people you will never meet, on machines
you cannot inspect, and delivered through registries you implicitly trust. That is the software
supply chain, and for most of its history nobody was accountable for its integrity.

The landscape described here is the industry's answer. It is younger than it looks, it is still
consolidating, and its acronyms overlap in confusing ways — several of them answer *adjacent*
questions and are routinely mistaken for one another. This document is a map, written to be read
straight through once, so that the individual specs make sense when you meet them later.

Four questions organize everything that follows:

1. **What is in this thing?** → bills of materials (SBOM and family), written in a format
   (CycloneDX, SPDX).
2. **Where did it come from, and can I prove it?** → provenance and attestation (SLSA, in-toto),
   made practical by signing (Sigstore).
3. **Do the scary findings actually matter to me?** → intelligence and triage (OSV,
   endoflife.date, VEX, VDR).
4. **How do I obtain any of these documents in the first place?** → distribution (TEA).

Answer only the first and you get a list nobody acts on. Answer only the second and you can prove
the origin of something you cannot describe. The value is in the combination — and the fourth
question is the one the field left until last, having spent a decade standardizing documents
that in practice still travel by email attachment.

Three more concerns sit at the edges of that list and are easy to overlook. Beneath all four is
**naming**: none of these documents compose unless everyone identifies a component the same way,
which is what **purl** provides. After all four is **operations**: a finding that never reaches
the person who can act on it accomplished nothing, which is where update bots, a component
analysis platform, and a **SIEM** come in.

Alongside all four is a question with a different character entirely — *am I allowed to ship
this?* **Licensing** is not a security property, and it is the one obligation in this document
that a court can enforce. It rides on the same inventory as everything else, which is why it
appears here rather than in a separate legal document. All three are covered below.

---

## The Cast

### OpenSSF — the organization

The **Open Source Security Foundation**, hosted by the Linux Foundation and funded largely by
big technology companies. The simplest framing: the shared pile of open-source code that
everything depends on had no one in charge of its safety, and OpenSSF is the group that
volunteered to be sort of in charge of it.

It writes rules and builds tools rather than shipping products — SLSA, Scorecard, the Best
Practices Badge, Sigstore, and Alpha-Omega funding for critical projects maintained by one
exhausted volunteer, which is the failure mode underneath most supply-chain incidents. Most of
those appear below in their own right.

### The xBOM family — what's in the box

A bill of materials is an inventory of what a thing is made of. The variants — SBOM for software,
HBOM for hardware, OBOM for a deployed environment, CBOM for cryptography, AI/ML-BOM for models
and datasets, SaaSBOM for hosted services — differ only in what "thing" means.

The family exists because the original insight — *you cannot secure what you cannot enumerate* —
turned out to generalize well beyond software packages.

→ Short definitions of every variant: [the workspace glossary](/bom-types/index.md)

### CycloneDX and SPDX — the file formats

A BOM has to be written down in something. Two standards dominate, and the interesting thing
about them is where they came from.

**CycloneDX** (OWASP) was designed security-first. That shows in what it makes easy: the
dependency *graph* — which component pulled in which — so you can answer "am I affected, and
through what path?" rather than merely "is this package present somewhere?" It also covers the
whole xBOM family in one format and carries VEX and provenance data natively rather than
delegating them to separate specifications.

**SPDX** (Linux Foundation) grew out of *license compliance*. The old shorthand — SPDX for lawyers,
CycloneDX for security — was never quite right and is now wrong: **SPDX 3.0 carries VEX natively**
through its Security profile, which removes the differentiator most often cited for choosing
CycloneDX.

The more useful frame is that the two are **complementary rather than rival**. Their scopes overlap
heavily and diverge at the edges, and the edges decide. CycloneDX is stronger where the question is
about a *build*: the dependency graph, declared completeness, the whole xBOM family in one schema.
SPDX is stronger where the question is about a *model or a dataset* — its AI and Dataset profiles
carry structured energy, bias and safety fields with no CycloneDX equivalent — and where licensing
must be answered precisely.

A project shipping a model inside a container has a good reason to emit both, describing different
things. What to avoid is emitting both for the same content with no answer to which is authoritative
when they disagree.

| | CycloneDX | SPDX |
|---|---|---|
| Steward | OWASP | Linux Foundation |
| Origin | vulnerability management | license compliance |
| Standardization | Ecma (ECMA-424) | ISO/IEC 5962 |
| Serializations | JSON, XML, Protocol Buffers | JSON, YAML, RDF, tag-value, spreadsheet |
| xBOM coverage | SBOM, HBOM, OBOM, SaaSBOM, ML-BOM, CBOM in one format | profile-based: Software, AI, Dataset, Security, Build, Licensing |
| VEX / VDR | native (`vulnerabilities` array) | native since 3.0 (Security profile) |
| Strongest at | dependency graph, completeness, one schema for the whole family | AI/dataset metadata, licence precision, ISO reference |

Both are widely supported and most generators emit either on request. Treat the row above as *where
each is strongest*, not as a tiebreak — several projects legitimately produce both.

→ Each format, completeness (`compositions`), merging:
[`formats/` in the knowledge bundle](/formats/index.md)

### purl — the name everything joins on

A BOM lists components, but a component has to be *named*, and the naming is where a supply-chain
program quietly succeeds or fails. "django 4.2" is not an identifier: which registry, which
distribution, which architecture, is it the PyPI package or a Debian rebuild of it? If your BOM
and the vulnerability database disagree about what a component is called, no amount of correct
data in either one produces a correct answer.

**purl** (Package URL) is the canonical string that settles it, derivable from where the artifact
actually came from rather than negotiated. This is what makes the rest of the landscape compose:
your SBOM records purls, vulnerability databases key on purls, your scanner joins the two. It is
unglamorous plumbing whose absence would leave every tool doing fuzzy string matching on package
names.

The older identifier, **CPE**, was designed to name IT *products* — vendor, product, version —
which suits commercial software with a clear vendor and suits the open-source dependency graph
badly, because matching is fuzzy and produces both false positives and silent misses. The two are
not mutually exclusive and BOMs often carry both, since CPE remains the key into NVD data.
Practical stance: purl as the primary identifier, CPE where an upstream data source forces it.

| | purl | CPE |
|---|---|---|
| Full name | Package URL | Common Platform Enumeration |
| Steward | Ecma TC54-TG2 (ECMA-427) | NIST |
| Names | packages, as published | IT products — vendor/product/version |
| Derivation | mechanical, from the package coordinates | assigned, from a controlled dictionary |
| Matching | exact | fuzzy — false positives and silent misses |
| Primary consumer | OSV, ecosystem advisories, SBOM tooling | NVD |
| Weak on | non-package software (OS images, appliances, commercial products) | open-source dependency graphs |

→ Syntax, type registry, per-ecosystem examples:
[`naming/` in the knowledge bundle](/naming/index.md)

### Licensing and REUSE — the obligation a court can enforce

Every other concern in this document is about *risk*: something might be vulnerable, might be
unmaintained, might not be what it claims. Licensing is about *permission*, and it is
categorically different. A vulnerability is a probability; a licence violation is a fact, and the
remedy is an injunction rather than a patch.

It belongs here rather than in a legal appendix because it rides on the same inventory. Once you
have enumerated components and named them, "what is each one licensed under" is one more column
on a table you already built — and the formats provide it. SPDX grew out of license compliance
and carries it natively; CycloneDX records it per component, expressed as an SPDX licence
identifier, an SPDX licence *expression* (`Apache-2.0 OR MIT`, `GPL-2.0-only WITH
Classpath-exception-2.0`), or a free-text name when neither fits.

The **SPDX License List** is doing the same job for licences that purl does for packages: turning
a string a human wrote into an identifier a machine can join on. `Apache-2.0` is an identifier;
"Apache License" is not.

**Declared is not concluded.** SBOM formats distinguish what a package *says* its licence is from
what an analysis of the actual files *concluded* it is, and the two genuinely differ — a
permissively-licensed package that vendored a copyleft file is the standard case. A declared
licence is author-supplied metadata and inherits every weakness of author-supplied metadata:
unverified at publication, and wrong often enough that tools which conclude rather than trust
exist as a category.

**REUSE** (FSFE) attacks the problem at the source rather than the SBOM. Every file carries
`SPDX-FileCopyrightText` and `SPDX-License-Identifier` headers, full licence texts live in
`LICENSES/`, and bulk or vendored material is annotated in `REUSE.toml`. The point is that
`reuse lint` then *fails* — in a git hook, in CI — rather than a `CONTRIBUTING.md` paragraph
asking people to remember. Downstream, a generator reads facts instead of guessing, so the SBOM's
licence column is derived rather than inferred.

**The copyleft floor is the trap.** A permissive wrapper does not make a permissive artifact. If
you statically link, vendor, or bundle into a container image, what you ship is an *aggregate*,
and the aggregate is governed by the most restrictive licence in it. An Apache-2.0 wrapper around
a GPL-3.0 library ships a GPL-3.0-floored artifact no matter what your `LICENSE` file says. The
sharpest version is AGPL: bundle an AGPL component and its §13 network clause applies the moment
you offer the result as a service, which is the case teams discover after launching, not before.

The floor depends on *how you distribute*, not only on what you depend on — so a pivot from
self-hosting to SaaS can change your obligations without a single dependency changing.

> **Why licensing gets less depth here than vulnerabilities.** The corpus this bundle grew from
> was written for vulnerability- and provenance-oriented work, and chose CycloneDX as its canonical
> format partly on that basis — accepting weaker license-compliance support as the cost. Licensing
> is covered because the landscape includes it, not because this corpus is compliance-driven. If
> you are here for compliance, SPDX is the format that argument favours, and the concepts below
> will feel thinner than the vulnerability ones.

→ Identifiers, expressions, declared-vs-concluded, REUSE, the copyleft floor:
[`licensing/` in the knowledge bundle](/licensing/index.md)

### CBOM — finding the crypto before it breaks

Worth separating from its siblings, because its motivation is a deadline rather than good hygiene.

A CBOM inventories every piece of cryptography a system uses and, critically, *where each one is
used*: this certificate is signed with that algorithm, provided by that library, used by that
service.

The driver is **post-quantum migration**. A sufficiently capable quantum computer breaks RSA and
elliptic-curve cryptography — the basis of essentially all current key exchange and digital
signatures. Everyone must swap them for post-quantum algorithms. But you cannot replace what you
cannot find, and in a real estate nobody knows where all the RSA is: buried in a firmware image,
hardcoded in a service written in 2011, baked into an appliance with a fixed certificate. A CBOM
is the "find it first" step, and the dependency chain it records is what tells you the blast
radius of retiring an algorithm.

There is time pressure beyond the eventual arrival of the hardware — **harvest now, decrypt
later**: an adversary records encrypted traffic today and decrypts it when the hardware exists.
Anything requiring long-term confidentiality is therefore already exposed.

Be realistic about tooling maturity: CBOM scanners are well behind SBOM scanners. Expect them to
catch TLS configuration, certificates, and obvious library calls, and to miss cryptography
embedded in binaries or selected dynamically at runtime.

### SLSA — how strong is your provenance

**S**upply-chain **L**evels for **S**oftware **A**rtifacts, pronounced "salsa". A graded framework
for producing verifiable **provenance**: a signed record of how an artifact was built, aimed
squarely at tampering between the source repository and the consumer.

The value of the grading is that it makes "we have provenance" a claim with teeth. Higher levels
demand progressively stronger properties — provenance exists at all, it is generated by the build
platform rather than asserted by the author, the build runs in an isolated environment the author
cannot influence, and so on.

Two details trip people up: the expansion is *Supply-chain* (hyphenated, lowercase c), and the
level numbering changed between the v0.1 and v1.0 specs, which scoped levels to a Build track.
Check slsa.dev before citing a specific level's requirements — this is exactly the kind of detail
this document deliberately does not pin down.

### in-toto — a recipe with signatures

Where SLSA says how strong a claim must be, **in-toto** provides the shape of the claim.

Write down in advance what is supposed to happen when your software is made: Alice checks out the
source, the build machine compiles it, the test runner tests it, in that order. That plan is the
**layout**. As each participant performs its step, it signs a note recording that the step
happened and what went in and came out — the **link metadata**. Verification then checks the whole
chain: did every step in the recipe occur, in order, performed by the authorized party, with each
step's output being the next step's input? Slip an extra ingredient in between two steps and the
chain no longer lines up.

Its other contribution is the **in-toto Attestation** format: a standard envelope for a signed
statement *about* an artifact. SLSA provenance travels inside that envelope, which is how the two
connect.

### Sigstore — signing without owning a key

Signing traditionally means guarding a private key forever, and a single leak invalidates
everything you ever signed. That burden is why most projects never signed anything at all.
Sigstore removes the key from the equation: you authenticate with an identity you already have,
receive a certificate valid for minutes, sign within that window, and discard the key. There is
nothing left to steal. The signature is recorded in a public append-only transparency log, so
"this was signed at this time by this identity" is publicly verifiable and cannot be quietly
rewritten later.

The trade-off is real and worth stating: you have exchanged key custody for dependence on
identity providers and public log infrastructure, and signing events become public by design.
For most projects that is a good trade; for some it is a disclosure problem.

→ Component roles (Fulcio, Rekor, cosign), SLSA and in-toto:
[`provenance/` in the knowledge bundle](/provenance/index.md)

### OSV — vulnerability data a machine can act on

Everything so far describes *your* software. To find problems in it you need the other half: a
record of what is known to be wrong with the components you depend on.

The traditional answer is **CVE** — the shared identifier namespace — enriched by **NVD**. That
pairing was built to catalogue vulnerabilities in IT products generally, and it shows: the
authoritative content is prose written for humans, the machine-readable part is CPE with its
matching imprecision, and interpreting "which versions of this library are actually affected"
often requires a person to read an advisory and decide.

**OSV** — Open Source Vulnerabilities — attacks that specific weakness. It is a schema in which a
record states exactly which package versions or git commits are affected, plus a database
aggregating the ecosystems' own advisory sources into that one shape behind a free API.

Two properties do the work. Advisories are authored by whoever actually owns the package, so
affected ranges are accurate rather than inferred. And records key on purl, so joining "what I
have" to "what is known bad" is a lookup rather than a heuristic.

It is not a competitor to CVE for identity — OSV records alias CVE and GHSA identifiers, and CVE
remains the shared namespace everyone cites. OSV is the structured data layer over it. Honest
limits: coverage varies by ecosystem, and OSV is scoped to *open source packages*. For operating
systems, appliances, and commercial products, NVD and CPE remain the data you have.

"Coverage varies by ecosystem" is worth unpacking, because it sounds like a data-quality
observation and is really an *organizational* one. CVE IDs are assigned by **CNAs** — CVE
Numbering Authorities, each with a defined scope — and the striking development of recent years is
that open-source foundations have been becoming CNAs for their own ecosystems, rather than leaving
their packages to a generalist authority with no domain knowledge. An ecosystem whose foundation
runs a CNA and feeds OSV produces advisories written by people who know which versions are
actually affected. An ecosystem with nobody in that seat falls back to whatever NVD infers.

So the question "is my ecosystem well covered" resolves to "does anyone own vulnerability
disclosure for it" — and that is a question about people, not about schemas. It is also the
mechanism behind the coverage gaps, which is why a tool must declare when it has none rather than
emit a clean scan.

→ Schema fields, data sources, identifier namespaces, who assigns CVEs:
[`intelligence/` in the knowledge bundle](/intelligence/index.md)

### endoflife.date — the risk with no CVE attached

Vulnerability data is a *lagging* indicator: it tells you what has already been found and
published. There is a *leading* indicator that scanners are blind to — whether anyone is still
maintaining the thing at all.

A component with zero known vulnerabilities is not therefore safe. If it reached end of life two
years ago, the correct reading is not "no problems found" but "no one is looking, and when
something is found there will be no fix". Unmaintained dependencies do not show up in scan output
until the day they show up permanently.

**endoflife.date** is the community-maintained database of support lifecycles. The distinction
that matters is between *end of active support* (no more bug fixes) and *end of security support*
(no more patches at all). The second is what converts a dependency into a liability, and the gap
between them is often years, which is why treating "supported" as a single boolean loses the
information you actually need for planning. Its API maps purl and CPE identifiers, so lifecycle
data joins to a BOM on the same key as everything else.

This intersects with regulation in a way that is easy to miss. Where a support period must be
declared and honoured — the EU Cyber Resilience Act being the current driver — you cannot
credibly promise support for your product beyond the support horizon of what it is built from.
Lifecycle data on your dependencies is an input to a commitment you are making, not merely
hygiene.

Honest limits: it is volunteer-curated, coverage skews to widely-used products, and dates get
revised. It is strong on runtimes, operating systems, and databases; it does not attempt the long
tail of ordinary libraries, where "is this maintained" remains a judgement call informed by commit
activity and Scorecard signals rather than a published date.

→ Fields, dates, API status:
[`intelligence/endoflife.date`](/intelligence/endoflife-date.md)

### VEX and VDR — does it actually matter

Your scanner reports two hundred vulnerabilities. Most are not real problems for *your* product:
the flawed function lives in a part of the library you never call, or the vulnerable path cannot
be reached by an attacker. Without a way to say so, SBOMs generate alert fatigue and get ignored —
which is the single most common way this whole landscape fails in practice.

**VEX** — Vulnerability Exploitability eXchange — is the supplier's answer, per vulnerability.
The valuable verdict is *not affected*, because it must carry a machine-readable justification:
the vulnerable code is not present, is not in the execute path, the component is not in the
shipped build, a mitigation is already in place. That is what converts "trust me" into something a
consumer's tooling can process automatically.

**VDR** — Vulnerability Disclosure Report — answers a different question with the same machinery.
Where VEX *adjudicates*, VDR *enumerates*: the product's vulnerability picture, framed around the
known completeness of vulnerability intelligence, and positioned as a disclosure vehicle — bug
bounty output, coordinated disclosure, a supplier's standing statement of what is wrong.

They are confusable because in CycloneDX both are built from the same `vulnerabilities` array, and
a VDR *can* carry analysis data. The working rule: if the document's job is to enumerate, it is a
VDR; if its job is to adjudicate, it is a VEX. One wrinkle — VEX is a cross-format concept that
CycloneDX implements, with OpenVEX and CSAF VEX as independent alternatives and CISA behind the
original push, while VDR terminology comes more from the NIST and Executive Order 14028 lineage.

| | VDR | VEX |
|---|---|---|
| Question | what is wrong | whether it is exploitable *here* |
| Scope | the product's whole vulnerability picture | usually one CVE, or a batch, against one product |
| Trigger | ongoing, standing disclosure | a scan finding, or a customer asking about a specific CVE |
| Center of gravity | the vulnerability records | the `analysis` verdict |
| Direction | supplier discloses outward, broadly | supplier answers a specific downstream question |
| Lineage | vulnerability-disclosure practice (CycloneDX cites ISO/IEC 29147:2018) | CISA; implemented by CycloneDX, OpenVEX, CSAF |

→ States, justifications, and the formats:
[`intelligence/` in the knowledge bundle](/intelligence/index.md)

### TEA — how the documents actually reach you

**Transparency Exchange API.** Everything above concerns the *content* of supply-chain documents.
TEA concerns their *delivery*, which turns out to be the unglamorous problem that blocks the rest
from working at scale.

Consider the state of practice: you want the SBOM for version 4.2 of a vendor's product. You email
your account manager. Eventually you sign an NDA, get a login to a customer portal, download a
file, and repeat the whole ritual for the next version and for every other vendor. Meanwhile the
VEX statement that would have suppressed half your findings sits somewhere else entirely. The
documents are standardized; obtaining them is not.

TEA is a standard API for automated discovery and retrieval: a consumer resolves an identifier for
a product release and gets back what exists for it, without a human in the loop. It is
deliberately format-agnostic — plumbing, not another document format. The design detail worth
carrying is that it versions *the set of documents about a release* separately from the release
itself, so publishing a new VEX statement for an unchanged binary is a first-class event rather
than a silent file swap.

Governance follows CycloneDX's lineage: an OWASP effort being standardized through Ecma
International TC54. The identifier syntax and resolution mechanics have since settled enough to
document — a `urn:tei:` URN resolved through DNS to a `/.well-known/tea` endpoint — but the
specification is at **beta 2**, and deliberately covers the *consumer* side only: work on the
publisher API begins after 1.0.

So the asymmetry decides what you can do with it. Building something that *reads* TEA is possible
now; building something that *publishes* is not, and publishing is the side most projects would
need.

→ Object model, TEI, status:
[`distribution/` in the knowledge bundle](/distribution/index.md)

### Dependency-Track — the standing inventory

A scan at build time answers a narrower question than it appears to: *what was known to be wrong
on the day we built this*. Vulnerabilities are disclosed continuously, and the artifact you
shipped last quarter does not rescan itself. Nothing described so far closes that gap — the SBOM
is a static document, and the scanner is a point-in-time tool.

**OWASP Dependency-Track** is the platform that turns those documents into standing
infrastructure. You upload a BOM per project and version; it stores them and continuously
re-evaluates every stored BOM against incoming vulnerability intelligence. When something newly
disclosed touches a component you recorded eight months ago, that surfaces without anyone
rebuilding or rescanning anything. Holding that inventory is also what makes "where do we use this
library" answerable in seconds during an incident.

Trade-offs worth stating plainly. It is a server you run and maintain, which is a real operational
commitment rather than a CLI you invoke. Its output quality is bounded by your BOM quality —
incomplete BOMs produce confidently incomplete analysis. And without VEX discipline it becomes an
alert-fatigue machine with better uptime.

→ Capabilities and current version:
[`tools/dependency-track`](/tools/dependency-track.md)

### Dependabot and Renovate — closing the loop

Every layer described so far *detects*. None of them changes a single version constraint. The
update bots are what actually fix things: they watch your manifests, notice that a dependency has
moved, and open a pull request. Boring, and the highest-leverage automation in the list — a
finding that arrives as a ready-to-merge PR costs a fraction of one that arrives as a ticket.

The choice between them is mostly about reach. **Dependabot** is GitHub-native with no
infrastructure to run, at the cost of configurability and of any path to self-hosted GitLab CE,
Gitea, or Forgejo. **Renovate** is open source, runs against every major forge hosted or
self-hosted, and is substantially more configurable. Outside GitHub it is the only real option.

The pairing that matters here: SHA-pinning your CI actions and digest-pinning your base images
makes builds reproducible and tamper-evident, but those pins then rot. Update bots are what keep
pinned references current, which is why pinning and a bot are a package deal rather than two
separate ideas.

**The counter-intuitive part.** Automating updates is itself an attack surface. The modern
npm-style compromise is a malicious version published to a legitimate package, and a bot on
default settings will open — and possibly automerge — that update within minutes of publication,
delivering the compromise faster than a human ever would. The mitigation is a **cooldown**: refuse
to propose a release until it has survived in the wild for a configured period, by which time
malicious releases are typically yanked. Both tools support this and both exempt security updates
by default, so fixes for known vulnerabilities still arrive immediately. If you run either tool
with automerge and no cooldown, you have optimized for the wrong failure mode.

The other failure mode is mundane and more common: **PR fatigue**. An ungrouped bot on a large
repository produces a stream nobody keeps up with, and the endgame is a muted notification channel
or a disabled bot — worse than never installing it, because the project now looks maintained.
Grouping related updates and automerging low-risk ones (with cooldown, and with CI you actually
trust) is what keeps the tool alive.

| | Dependabot | Renovate |
|---|---|---|
| Licence / owner | GitHub (proprietary, hosted) | AGPL-3.0, maintained by Mend |
| Forges | GitHub only — no clean path to self-hosted GitLab CE, Gitea, or Forgejo | GitHub, GitLab, Bitbucket, Azure DevOps, Gitea, Forgejo — hosted or self-hosted |
| Configuration | `.github/dependabot.yml` | `renovate.json` / preset inheritance |
| Infrastructure | none | hosted app, or self-hosted runner |
| Managers | language package ecosystems, `github-actions`, `docker` | the above plus Dockerfiles, Kubernetes manifests, Terraform, and more |
| Grouping | supported | extensive rule-based grouping |
| Automerge | limited | policy-driven |
| Dashboard | — | dependency dashboard issue |
| Advisory source | GitHub Advisory Database | OSV and ecosystem sources |

Both satisfy the OpenSSF Scorecard `Dependency-Update-Tool` check, so the choice is about forge
support and operational cost rather than compliance.

→ Each tool, and the cooldown control:
[`tools/` in the knowledge bundle](/tools/index.md)

### SIEM — where findings become somebody's problem

**Security Information and Event Management.** Set expectations first: unlike everything above,
SIEM is not a supply-chain standard, has no native understanding of BOMs, and long predates this
landscape. It appears here because it is the *destination*, and a supply-chain program that stops
at generating documents has not yet done anything.

Note that the update bots above are the *other* destination, and the preferable one: a finding
that becomes a merged pull request never needs a human queue at all. What reaches the SIEM should
be the residue — findings with no available fix, or that need a judgement call.

A SIEM is the platform where logs, alerts, and events from across an estate are aggregated,
correlated, and turned into something a human is assigned. Its value is correlation: an event is
rarely meaningful alone, and meaning comes from joining it against everything else you know. Two
directions connect it to this landscape:

- **Inventory answers incident questions.** The canonical case is Log4Shell: the industry's
  scramble was not to *fix* anything, it was to determine *where the affected library even was*.
  An SBOM corpus turns that from weeks of archaeology into a query. This — not compliance — is
  the argument that convinced most organizations to generate SBOMs at all.
- **Findings need a workflow.** A vulnerability match is inert until it is a ticket with an owner.
  Routing supply-chain findings into the same queue as everything else is what makes them get
  worked rather than admired in a dashboard.

The piece usually missing from this picture is the layer in between. A SIEM consumes events, not
CycloneDX documents — so the component analysis platform described above is what translates
between them, emitting an event when a stored BOM becomes newly affected. The realistic pipeline
is *BOMs → Dependency-Track → SIEM/ticketing*, not BOMs straight into a SIEM.

And note what makes that pipeline mechanical rather than heuristic: **purl** as the join key
across the BOM, the advisory database, and the asset inventory. Correlation is only as good as
the identifiers being correlated.

---

## How the Pieces Fit Together

A concrete pass through a release, which is the fastest way to see the seams:

1. CI builds the artifact. A generator emits a **CycloneDX SBOM** describing what went in, each
   component named by **purl**.
2. The build platform emits **SLSA provenance** — how it was built — carried in an **in-toto
   attestation** envelope.
3. **cosign** signs the artifact and its attestations via **Sigstore**, using the CI job's own
   identity, and the signatures land in a public transparency log.
4. A consumer verifies the signature, checks the provenance against the SLSA level they require,
   and scans the SBOM.
5. Findings arrive. The supplier publishes **VEX** statements marking the unreachable ones *not
   affected*, and the consumer's tooling suppresses them instead of paging someone.
6. The SBOM is stored in a **component analysis platform** (Dependency-Track), which re-evaluates
   it as new advisories appear — matching **OSV** data on purl, filtered by VEX — and raises an
   event into the **SIEM** or ticket queue when a stored BOM becomes newly affected. The same
   inventory, joined to **endoflife.date**, answers the parallel question of what has gone
   unmaintained since it shipped.
7. Where a fix exists, **Renovate** or **Dependabot** has usually already opened the pull request
   that resolves it, subject to a cooldown.
8. **OpenSSF Scorecard** watches the repository's habits over time, independently of any single
   release.

Steps 1–5 assume the consumer somehow *has* your documents. Today that is usually a portal, a
release-page attachment, or an email. **TEA** is the intended answer: publish the artifacts against
a resolvable identifier for the release, and let the consumer's tooling fetch them — including the
VEX you publish three months later, long after the binary stopped changing.

Read as a sentence: *inventory* (SBOM) plus *origin* (SLSA/in-toto) plus *trust* (Sigstore) plus
*intelligence* (OSV) plus *triage* (VEX) plus *distribution* (TEA) plus *action*
(Dependency-Track → SIEM) plus *remediation* (Renovate/Dependabot) — all of it joined on
*identity* (purl), with Scorecard grading the process that produced it.

Steps 1–5 describe a single release and are finished when it ships. Steps 6–7 are standing
infrastructure, and are where the value compounds instead of expiring: they keep answering the
question months later, against advisories that did not exist when the artifact was built.

---

## Trade-offs and Honest Limits

- **An SBOM is an inventory, not a defense.** It changes nothing about your security posture on
  its own; it makes the next question answerable. Organizations that generate SBOMs and never
  consume them have bought a filing cabinet.
- **Triage is the bottleneck, not generation.** Producing BOMs is nearly free and largely
  automated. Deciding what the findings mean is neither, and it is where programs stall.
- **Partial BOMs lie by default.** A BOM that omits transitive dependencies looks identical to one
  that has none. CycloneDX's `compositions` field exists to say "this portion is incomplete"; if
  you generate partial BOMs and leave it unset, you are publishing a false claim of completeness.
- **Provenance proves origin, not quality.** A high-SLSA-level artifact can be thoroughly insecure
  software, faithfully and verifiably built from thoroughly insecure source.
- **Coverage is uneven across the family.** SBOM tooling is mature; CBOM, OBOM, and SaaSBOM
  tooling is early. Treat outputs there as a starting inventory to verify, not a finished one.
- **Distribution is the least settled layer.** TEA is in beta and unratified. Anything built on it
  now is a bet on a moving specification; the pragmatic near-term posture is to produce artifacts
  in stable formats and keep the publishing mechanism replaceable.
- **Licence data in a generated SBOM is weaker than it looks.** Most generators report the
  *declared* licence, which is author-supplied and unverified. Treating it as a compliance answer
  rather than a starting point is how a copyleft file inside a permissive package survives review.
- **This is a moving target.** Spec versions, field names, and conformance levels change. That is
  precisely why they are quarantined in `../reference/` rather than stated here — but verify
  against upstream before relying on any of it.

---

## Common Misconceptions

**"VEX and VDR are two names for the same thing."**
They share a schema and a purpose in the broad sense, but answer different questions — enumeration
versus adjudication. Producing a VDR does not discharge the obligation to tell consumers which
findings actually apply.

**"CycloneDX has a 'fragment' object."**
It does not; the term is not in the specification. Informally it means one of three real
mechanisms — partial BOMs later merged, the `compositions` field declaring a portion incomplete,
or BOM-Link references between separate BOMs. When a tool's documentation says "fragment", it
almost always means the first.

**"SLSA levels measure how secure the code is."**
They measure the integrity of the *build and delivery process*. Code quality is a different axis
entirely.

**"No known vulnerabilities means the dependency is fine."**
It means nothing has been *published* about it. An end-of-life component with a clean scan is
usually worse than a supported one with a patched CVE, because the next finding will never get a
fix. Lifecycle status is a separate axis from vulnerability status, and scanners do not report it.

**"Scanning at build time tells you whether your release is vulnerable."**
It tells you what was known *on build day*. Disclosure is continuous and artifacts do not rescan
themselves, which is the entire argument for storing BOMs in something that re-evaluates them.

**"Automated dependency updates are strictly safer than not updating."**
Not on default settings. A bot with automerge and no cooldown will adopt a compromised release
faster than any human would. Cooldowns are what make the automation net-positive, and both tools
still let security fixes through immediately.

**"Pipe the scanner output into the SIEM and you have supply-chain coverage."**
You have an alert-fatigue machine. Raw findings without VEX triage and without a component
analysis layer produce volume, and volume gets muted. The order matters: triage first, route
second.

**"purl and CPE are interchangeable identifiers."**
They name different things for different audiences — packages versus products — and match with
very different precision. Carrying both is common and sensible; treating a CPE match as
authoritative for an open-source dependency is how false positives enter the queue.

**"TEA is another BOM format to support."**
It is a transport and discovery API, deliberately format-agnostic. Adopting it does not change
what you generate, only how consumers find it. (Unrelated name collision worth knowing in this
environment: `tea` is also the Forgejo/Gitea command-line client — same four letters, no
relationship.)

**"Our project is MIT, so what we ship is MIT."**
Only if you ship nothing else. Static linking, vendoring, and container images produce an
aggregate governed by its most restrictive component — the `LICENSE` file at your repository root
describes your own code, not the artifact. Changing how you distribute can change the obligation
without changing a single dependency.

**"The SBOM says Apache-2.0, so it's Apache-2.0."**
It says the package *declared* Apache-2.0. Declared and concluded licences are different fields
for a reason, and a permissive package that vendored one copyleft file is the ordinary case, not
an exotic one.

**"Signing solves supply-chain security."**
Signing establishes who published an artifact. It says nothing about whether that publisher was
compromised, or whether the signed contents are trustworthy — a compromised maintainer signs
malicious releases perfectly validly.

---

## Relevance to This Workspace

The `SupplyChain` workspace exists to host projects in this space. The concepts above are the
shared vocabulary; the practical controls are already covered by installed skills, which should be
reused rather than reimplemented:

- `project-maintenance-skills:supply-chain` — dependency vulnerabilities, SBOM generation,
  signing, OpenSSF Scorecard
- `project-maintenance-skills:dependency-health` — Dependabot/Renovate configuration and update-PR
  triage
- `project-orchestration-skills:setup-container-security` — `grype` + `syft`, digest pinning,
  non-root runtime
- `project-orchestration-skills:harden-github-actions` / `:harden-gitlab-ci` — CI hardening,
  SHA-pinning, provenance
- `project-orchestration-skills:setup-pre-commit` — REUSE scaffolding and `reuse lint` as a hook
  and a CI job; `setup-adrs` covers the `LICENSING.md` copyleft-floor analysis for anything that
  vendors or bundles

A worked example close to home: the private git server negotiates a classical, non-post-quantum
SSH key exchange. That is exactly one CBOM line item — one host, one protocol, one classical
algorithm, and a note that traffic over it is harvestable today and readable later.

---

## Related

- The **concepts** this document points into are the rest of this bundle; start at
  [the index](/index.md).
- **How-to**: none yet — "generate and verify an SBOM for project X" belongs in `../howto/`.
- **ADR**: cross-project decisions (canonical BOM format, signing approach) belong in `../adr/`
  once the workspace is promoted to t1.

## Sources

Conceptual orientation drawn from the upstream projects. Per-topic source links live in the
reference documents, alongside the facts they support.

- [CycloneDX](https://cyclonedx.org/) · [SPDX](https://spdx.dev/) ·
  [Package URL](https://github.com/package-url/purl-spec) ·
  [Transparency Exchange API](https://github.com/CycloneDX/transparency-exchange-api)
- [SLSA](https://slsa.dev/) · [in-toto](https://in-toto.io/) · [Sigstore](https://www.sigstore.dev/)
- [OSV](https://osv.dev/) · [endoflife.date](https://endoflife.date/) ·
  [OWASP Dependency-Track](https://dependencytrack.org/)
- [OpenSSF](https://openssf.org/) · [Scorecard](https://scorecard.dev/)
- [REUSE](https://reuse.software/) · [SPDX License List](https://spdx.org/licenses/) ·
  [CVE Program](https://www.cve.org/) ·
  [OpenSSF guide to becoming a CNA as an open-source project](https://github.com/ossf/wg-vulnerability-disclosures/blob/main/docs/guides/becoming-a-cna-as-an-open-source-org-or-project.md)

_Last reviewed: 2026-08-01. This document is durable rationale and should need review only when
the landscape's shape changes, not when a version number does._
