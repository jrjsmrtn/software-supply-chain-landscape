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

## Gates

`gitleaks` and `reuse lint` run here on commit. **The bundle checks do not** — they live in the
`supplychain-workspace` meta-project, because they reason about private repositories. Run them from
there before publishing anything:

```bash
python3 workspace/scripts/check-okf.py                                             # conformance, attribution, expiry
python3 workspace/scripts/check-doc-links.py software-supply-chain-landscape/knowledge
python3 workspace/scripts/check-dates.py software-supply-chain-landscape
```

**This is a known weakness**, recorded as such: a gate that lives apart from what it checks can
silently stop running. Until that is resolved, running them is a deliberate act rather than an
automatic one.

## Conventions

- **Dates ISO 8601 everywhere**, prose included. Reduce precision rather than invent it — `2026-07`
  for a known month, `2026` for a known year.
- **Landscape, not ecosystem.** "Ecosystem" is reserved for a *package* ecosystem (npm, PyPI, Hex);
  it is an OSV schema field and the thing purl's `type` selects.
- **Bundle-relative links** (`/naming/purl.md`) between concepts; the leading `/` means the bundle
  root, not the filesystem root.
- **Type vocabulary**: `BOM Type`, `Format`, `Identifier`, `Specification`, `Data Source`, `Tool`,
  `Practice`, `Organization`, `Explanation`.
- Commits: Conventional Commits. Branch: `main` only.
- `knowledge/log.md` records bundle content changes; `CHANGELOG.md` records releases.
- **`knowledge/` must name no private repository, path or host.** It is the published product.
  This file is developer guidance and may reference the meta-project by name — but never a
  hostname, URL or credential, which belong in `CLAUDE.local.md`.

## AI Collaboration Notes

**What AI should know:**

- **Only decompose concepts that carry content.** A bundle of one-line stubs is worse than prose.
  If a subject has nothing but a definition, leave it out until sourcing earns it a file.
- **A capability page is a weaker source than a schema.** This was learned the hard way on CBOM:
  CycloneDX's marketing page lists three asset types, the JSON schema has four.
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
