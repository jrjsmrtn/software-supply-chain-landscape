# Software Supply Chain Landscape

Curated, sourced knowledge about the software supply chain — bills of materials, provenance,
attestation, vulnerability intelligence, licensing and the tooling around them.

Distributed as an [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle: one concept per markdown file, YAML frontmatter, no tooling required to read it.

## Start here

**[knowledge/landscape.md](knowledge/landscape.md)** is the map — written to be read straight
through once, so the individual specifications make sense when you meet them later. Everything else
is looked *up* rather than read.

Then [knowledge/index.md](knowledge/index.md) for the concept listing.

## What makes this different from a wiki

Every concept states where its facts came from, who checked them, and when they expire.

| Frontmatter | What it records |
|---|---|
| `sources` | the specific pages a concept draws on, each with an `id` |
| footnotes | per-claim attribution — `[^cdx-cbom]` keys into `sources[].id` |
| `verified` | confirmation events; absent means **nobody has checked this** |
| `stale_after` | when the concept stops being trustworthy |

A footnote whose label is not a `sources[].id` attributes nothing, and a concept past its
`stale_after` fails a gate. Both are **enforced by a checker, not asked for in prose** — the
checkers live alongside the private workspace this corpus was extracted from and are run against
this repository before publishing.

That discipline came from being burned: an earlier version of this corpus cited project homepages
for claims that needed specific pages, and one URL had been written from memory.

## Layout

```
knowledge/          the OKF bundle — everything this repository carries
  landscape.md      the explanation; type: Explanation
  index.md          concept listing, for progressive disclosure
  log.md            what changed in the bundle, and when
  bom-types/ naming/ formats/ licensing/
  intelligence/ provenance/ distribution/ tools/
```

Knowledge and nothing else. Tooling and decision records live in the meta-project this was
extracted from.

## Reading it as an agent

The bundle is designed for grounding. `index.md` files exist for progressive disclosure — read
those to decide what to load, rather than loading the tree. Concepts cross-link with bundle-relative
paths (`/naming/purl.md`), which are interpreted from `knowledge/`.

Treat `verified: absent` as unverified. Most of this corpus is migrated prose whose claims have not
been re-checked; the concepts that *have* been checked say so.

## Licence

**[CC BY 4.0](LICENSES/CC-BY-4.0.txt)** — use it, quote it, build on it, with attribution.

Declared per-file in [`REUSE.toml`](REUSE.toml) and enforced by `reuse lint`.

Facts drawn from upstream sources remain theirs; each concept names them. The upstream set is
permissively licensed throughout — Apache-2.0, CC0-1.0, and US government works — with no
share-alike obligation.
