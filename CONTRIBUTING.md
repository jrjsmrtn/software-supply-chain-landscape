# Contributing

Corrections are the most valuable contribution here. Every concept states facts about specifications,
tools, regulations and formats that change without telling anyone — if something is out of date or
wrong, saying so is worth more than a new concept.

## The one rule: read the primary source

**A claim is not accepted until someone has read the specification, the standard, the tool's own
documentation or the enacting text.** Not a blog post, not a vendor summary, not another knowledge
base, not a model's recollection.

This is not a formality. Re-verifying the CRA concept against the enacting text found a **wrong
annexe citation** that had been carried in confidence — the SBOM-on-reasoned-request provision is
Annex VII point 8, not Annex VIII point 8, and Annex VIII is Conformity Assessment Procedures, which
says nothing about SBOMs. Nothing but reading the instrument would have caught that.

**Check for the content, not the status code.** Several primary sources answer `HTTP 200` or `202`
with something other than the document — EUR-Lex returns 202 with an empty body to a non-browser
client, and some hosts serve a proof-of-work challenge page for *any* path, including ones that do
not exist. A status code proves the server answered, never that the content arrived, and on those
hosts it does not even prove the page exists. If a source cannot be retrieved, **say so and stop**.

## What a concept must have

Concepts are OKF documents. Each needs:

- **`sources`** — every source cited, each with an `id`, `title` and `resource`.
- **Footnotes joining body to sources** — every `[^id]` reference must have a definition, every
  definition must be referenced, and every `sources` entry must have a footnote. The gates check all
  four directions, because a footnote defined but never cited renders as nothing, so a source that
  *looks* cited is not.
- **`verified`** — who read it and when.
- **`stale_after`** — when it must be re-checked. Longer for stable instruments (the DCO has not
  changed since 2006), shorter for anything moving.
- **Re-verification notes** — where to look next time and what specifically to watch. Name the check
  that would catch a change, not just the URL.

Quote sources directly and generously. Paraphrase is what expires first.

## Filing

By **subject**, in the existing categories — `bom-types/`, `formats/`, `provenance/`, `licensing/`,
`naming/`, `regulation/`, `threats/`, `tools/`, `intelligence/`, `disclosure/`, `distribution/`.

Each category states its own scope in its `index.md`, and those boundaries are load-bearing.
`regulation/` admits *"only instruments that change what a bill of materials must contain, or when
one must exist"* — a significant cyber-security obligation that never reaches the BOM belongs
elsewhere or nowhere.

## Scope

This bundle holds **generic mechanics**: what a specification says, how a tool behaves, what an
instrument requires of a document. It does not hold:

- **What a particular organisation has decided** — that is entity-keyed knowledge, and lives in
  [`ai-contribution-policies`](https://github.com/jrjsmrtn/ai-contribution-policies) for AI
  contribution positions.
- **Procedure** — how to run an audit or prepare a release. That belongs in tooling and skills.
- **Legal advice.** Concepts describe what an instrument requires *of a document*. Whether it applies
  to a given product or organisation is a legal question, and not one a reference corpus should
  answer.

## Gates

```bash
okf validate knowledge && okf lint knowledge
```

Conformance, attribution in both directions, ISO 8601 dates, links, `reuse lint` and secret scanning
run on every commit — and again **weekly**, because expiry is a function of the date rather than of
the diff. A commit-triggered check alone would never notice a concept going stale.

## Use of AI in contributions

**AI assistance is permitted. It is not permitted to substitute for reading the source.**

- **You must have read the primary text yourself.** A concept summarising what a model reported about
  a specification is exactly the failure this bundle exists to prevent, one layer removed.
- **Quotations must be verified against the source**, not reproduced from a model's output. A
  plausible near-quotation is worse than none, because it is citable.
- **Disclose it** with an `Assisted-by:` trailer naming the tool and model — see
  [`knowledge/provenance/commit-trailers.md`](knowledge/provenance/commit-trailers.md) for why that
  field and not `Co-developed-by:`.
- **You are responsible for the contribution** regardless of what produced it, and must be able to
  explain and defend every claim under review.

Contributions are accepted under the [DCO](knowledge/provenance/dco.md) — add `Signed-off-by:` with
`git commit -s`. There is no CLA. Both instruments are documented in this bundle, which is a good
reason to get our own use of them right.
