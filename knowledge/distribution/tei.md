---
type: Identifier
title: TEI (Transparency Exchange Identifier)
description: The identifier that resolves to a specific Product Release — what makes automated artifact retrieval possible.
resource: https://github.com/CycloneDX/transparency-exchange-api
tags:
  - distribution
  - identifier
  - tea
status: draft
generated:
  by: claude/opus-5
  at: '2026-08-01T12:40:00Z'
stale_after: 2026-11-01
sources:
  - id: tea-repo
    title: CycloneDX/transparency-exchange-api
    resource: https://github.com/CycloneDX/transparency-exchange-api
---

The **Transparency Exchange Identifier** resolves to a specific Product Release. It is what makes
automated retrieval possible at all: without a resolvable identifier, [TEA](tea.md) would be an API
with no way to address anything.[^tea-repo]

Its role in the landscape mirrors [purl](/naming/purl.md)'s — purl names a *component* so documents
can join; TEI names a *release* so its documents can be found.

# Deliberately not documented here

**Identifier syntax and the resolution mechanism are not restated.** They were still moving at the
time of writing and could not be verified against the specification, and a paraphrase of a moving
target is the failure mode this bundle exists to avoid.

Consult the specification repository's `doc/` directory for the current form.

This concept therefore records **what TEI is for and that its details are unstable** — which is the
honest content available. When the syntax settles, this is the concept to fill in, and its
`stale_after` is set short for that reason.

# Related

- [TEA](tea.md) — the API this addresses into
- [purl](/naming/purl.md) — the component-level analogue

[^tea-repo]: [CycloneDX/transparency-exchange-api](https://github.com/CycloneDX/transparency-exchange-api)
