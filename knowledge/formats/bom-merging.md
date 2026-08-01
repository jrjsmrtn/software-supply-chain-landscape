---
type: Practice
title: Merging BOMs
description: Combining partial BOMs is a tooling operation with two modes, and there is no "fragment" object in the specification.
tags:
  - bom
  - cyclonedx
  - practice
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:00:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:05:00Z\'
stale_after: 2027-08-01
sources:
  - id: cyclonedx-cli
    title: cyclonedx-cli
    resource: https://github.com/CycloneDX/cyclonedx-cli
---

**There is no "fragment" object in the CycloneDX specification.** The term appears constantly in
tool documentation and means one of three real mechanisms — a partial BOM later merged, the
[`compositions`](bom-completeness.md) field declaring a portion incomplete, or a
[BOM-Link](/naming/bom-link.md) reference between separate documents. When a tool says "fragment",
it almost always means the first.

Combining partial BOMs is therefore a **tooling operation**, not a format feature
(`cyclonedx-cli merge`, among others).[^cyclonedx-cli]

# Schema

| Mode | Behaviour | Use when |
|---|---|---|
| **Flat** | components from all inputs collapse into one list | one consolidated inventory; structure is not needed |
| **Hierarchical** | each input's `metadata.component` is retained as an assembly | system structure must survive the merge |

The choice is not cosmetic. Flat merging discards which artifact each component came from, so
"which of our services ships the vulnerable library" stops being answerable from the merged
document.

# Practice

Prefer **linking over merging** where the inputs are separately maintained. A merge produces a
document someone must now keep current; a [BOM-Link](/naming/bom-link.md) reference lets each
document stay owned by whoever knows the truth about it.

Merge when you need a single artifact to hand to a consumer who will not chase references — and
when you do, keep the hierarchical mode unless you are certain nobody will need provenance back to
the source document.

# Related

- [Declaring BOM completeness](bom-completeness.md) — what the inputs should have said about themselves
- [BOM-Link](/naming/bom-link.md) — the alternative to merging
- [CycloneDX](cyclonedx.md)

[^cyclonedx-cli]: [cyclonedx-cli](https://github.com/CycloneDX/cyclonedx-cli)
