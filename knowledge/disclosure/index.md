# Disclosure documents

Documentation that travels *with* an artifact, describing what it is for and where it fails.

* [Model cards](model-cards.md) - Intended use, performance variation, limitations. Lineage in the frontmatter.
* [Datasheets for datasets](datasheets-for-datasets.md) - Motivation, composition, collection, maintenance.

# Not bills of materials

A BOM says what an artifact is **made of**. These say what it is **for** — and, more usefully, what
it is *not* for. Neither replaces the other, and neither is a substitute for the structured
equivalents in [SPDX's AI and Dataset profiles](/formats/spdx-ai-profile.md), which cover much of
the same ground as queryable fields rather than prose.

Both originate as narrative, human-first documents. That is a strength when a practitioner is
deciding whether to use something, and a weakness when an auditor needs an answer a machine can
produce.
