# software-supply-chain-landscape

Curated supply-chain knowledge as an OKF bundle. Knowledge only — the gates that check it
and the decisions that shaped it live in the meta-project this was extracted from.

## Project Context

- **Category**: Knowledge / documentation — no application code
- **Type**: OKF bundle — the unit of distribution, and all this repository carries
- **Stack**: Markdown + YAML frontmatter. No code
- **License**: CC BY 4.0 throughout — see `REUSE.toml`
- **Tier**: t1
- **Distribution profile**: Private — **Public is the point**, via the `public-release` gate
- **Extracted from** `supplychain-workspace` on 2026-08-01. The decision records stayed there
  (ADR-0005, ADR-0006): they reason about private repositories, and this one is meant to be
  publishable

## What this repository is for

A bundle that cannot leave its parent repository cannot be distributed. This one exists to be
fetched, quoted and grounded on — by a person reading `knowledge/landscape.md` straight through, or
by an agent loading a concept it needs.

**The corpus is the product**, and it is the only thing here. Gates and decision records live in
the private meta-project, so that what ships is knowledge plus the metadata a consumer needs.

## The two rules that matter

1. **Facts go in the bundle; rationale goes in `landscape.md`.** Both are concepts now
   (`landscape.md` carries `type: Explanation`), but they are different kinds of claim. A fact has
   a source and an expiry. An argument has neither, and does not belong in a concept body pretending
   to be one.
2. **Never bump a `stale_after` without re-checking.** The gate cannot tell the difference, which
   is exactly why it is written down. Re-verify against upstream, record it in `verified`, then move
   the date.

## Choosing a `stale_after`

Pick the tier that matches how fast the *claims in that concept* move — not how important the
concept is. A default value applied without thinking is how 40 of 61 concepts once ended up sharing
one date.

| Tier | For |
|---|---|
| **~3 months** | draft or beta specifications under active revision (TEA, TEI) |
| **~4 months** | version and capability claims about actively-shipping software; coverage counts that grow (tool concepts, `osv.dev` source counts, `endoflife.date` product totals) |
| **~6 months** | registries and rosters, and enums that move with a spec version (CNA roster, purl type registry, VEX vocabularies, SPDX profiles) |
| **~12 months** | definitions, ratified specifications, structural mechanisms, attack mechanics |
| **~24 months** | durable rationale — currently only `landscape.md` |

**Clustering within a tier is fine and intended.** Concepts that share a volatility class also tend
to share sources, so re-verifying them in one sitting is cheaper than spreading them arbitrarily.
Clustering *across* classes, because nobody chose, is the failure this replaced.

## Gates

The bundle checks still live in the `supplychain-workspace` meta-project — this repository carries
knowledge and nothing else — but they are **no longer run by hand**. Two mechanisms, covering two
different failures:

| When | What runs | Catches |
|---|---|---|
| every commit here | `bundle-gates` in `.lefthook.yml`, invoking `../workspace/scripts/` | anything a change breaks |
| weekly, unattended | `workspace/scripts/run-gates.sh` via a `launchd` agent | `stale_after` expiry |

**Conformance is `okf`'s job** (ADR-0010) — `okf validate` + `okf lint`, pinned at v0.2.1, covering
§5.1 attribution, §5.2 datetimes, §5.5 expiry, §8 `index.md` frontmatter, §9 `log.md` headings and
links. Install with `go install github.com/okfcli/okf/cmd/okf@v0.2.1`; the hook fails without it.
The local scripts now cover only the residual: two footnote-*definition* faults, and ISO dates
across files outside the bundle. **Do not reimplement an `okf` check locally.**

**The scheduled run is not redundant.** Expiry is a function of today's date, not of a diff: a
concept goes stale on a repository nobody is committing to, so a hook would never fire. Failures
raise a macOS notification and land in `~/Library/Logs/supplychain-bundle-gates.log`.

The hook **fails** if the meta-project is not checked out beside this repository, rather than
skipping. A gate that quietly does nothing is the failure this arrangement risks, and silence is
what makes it dangerous.

Run them by hand at any time with `../workspace/scripts/run-gates.sh`.

**The residual weakness is narrower but real**: the gates and what they check are still separate
repositories, so a clone without the sibling cannot self-check. That is a publication-time problem,
not a today problem — and until then the hook says so loudly instead of passing.

## Conventions

- **Dates ISO 8601 everywhere**, prose included. Reduce precision rather than invent it — `2026-07`
  for a known month, `2026` for a known year.
- **Landscape, not ecosystem.** "Ecosystem" is reserved for a *package* ecosystem (npm, PyPI, Hex);
  it is an OSV schema field and the thing purl's `type` selects.
- **Bundle-relative links** (`/naming/purl.md`) between concepts; the leading `/` means the bundle
  root, not the filesystem root.
- **Type vocabulary**: `BOM Type`, `Format`, `Identifier`, `Specification`, `Data Source`, `Tool`,
  `Practice`, `Organization`, `Explanation`, `Regulation`, `Attack`. Two of those exist because a
  neighbouring type would have flattened a distinction the concept is *about*: a regulation is not a
  specification — it obliges rather than describes — and an attack is not a practice, because a
  practice is something you adopt and an attack is something done to you.
  `Attack` covers the four techniques in `threats/`; `slsa-threat-model.md` sits beside them as a
  `Specification`, because SLSA's taxonomy is a document, not a technique.
  **Verify a new type against this list before using it.** `Attack` was in use on four concepts for
  a week while this list named ten types, so nothing contradicted anything — `okf` does not
  constrain the vocabulary, and neither did anything else.
- Commits: Conventional Commits. Branch: `main` only.
- `knowledge/log.md` records bundle content changes; `CHANGELOG.md` records releases.
  **`log.md` headings are ISO dates and nothing else** — OKF §9 makes that a MUST, and `okf validate`
  enforces it. Do not head entries by release; it was tried on 2026-08-03 and failed the spec.
  The **release↔date map lives in the preamble**, which is unconstrained prose: that is how a
  `knowledge/` tree copied out of this repository still names its version, since OKF has no in-band
  content-version field and a git tag does not travel with a copied directory. Update the map when
  cutting a release.
- **`knowledge/` must name no private repository, path or host.** It is the published product.
  This file is developer guidance and may reference the meta-project by name — but never a
  hostname, URL or credential, which belong in `CLAUDE.local.md`.

## AI Collaboration Notes

**What AI should know:**

- **Only decompose concepts that carry content.** A bundle of one-line stubs is worse than prose.
  If a subject has nothing but a definition, leave it out until sourcing earns it a file.
- **A capability page is a weaker source than a schema.** This was learned the hard way on CBOM:
  CycloneDX's marketing page lists three asset types, the JSON schema has four.
- **EUR-Lex cannot be fetched programmatically** — it returns HTTP 202 with an empty body rather
  than an error, so a `regulation/` re-verification silently falls back to commentary. The working
  route is content negotiation on the Publications Office CELEX resource; the exact command and the
  headers that matter are in the meta-project's `CLAUDE.md` under *Sourcing Methods*.
- **`verified` is an act, not a formatting step.** Absent is the honest default. Most of this corpus
  is migrated prose that nobody has re-checked, and it says so.
- **The gates verify structure, not sense.** Links resolving and YAML parsing says nothing about
  whether a claim is true or a sentence contradicts the paragraph above it. Read what you write.
- **Do not add a `docs/` tree.** Reference facts belong in the bundle. Decisions belong in the
  meta-project's log, not here — this repository is publishable and should not describe private
  ones.

**AI leads**: sourcing concepts against upstream, conformance work.
**Human leads**: what is worth a concept, licence and publication decisions, when a claim is
verified.
