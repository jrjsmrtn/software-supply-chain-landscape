---
type: Practice
title: Provisional identifiers for unregistered purl types
description: What to emit when an ecosystem has no registered purl type, and why an unregistered purl is worse than an obviously wrong one.
tags:
  - identifier
  - naming
  - practice
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:37:22Z'
stale_after: 2026-12-01
sources:
  - id: type-definitions
    title: purl type definitions directory
    resource: https://github.com/package-url/purl-spec/tree/main/types
  - id: ansible-bom-adr-0004
    title: 'ansible-bom ADR-0004: Provisional pkg:ansible Identifiers, and a Gated 1.0'
    resource: https://github.com/jrjsmrtn/ansible-bom/blob/main/docs/adr/0004-provisional-purl-identifiers.md
    last_modified: '2026-08-01'
---

purl covers far fewer ecosystems than exist, so a producer will eventually need to name components
in one with no registered type.[^type-definitions]

# The trap: unregistered types fail silently

The purl grammar accepts **any** type string. `pkg:whatever/foo@1.0` parses cleanly and passes BOM
schema validation. Nothing rejects it.

What happens instead is worse than rejection. Consumers that key on type return an **empty result,
not an error**: a component with an unregistered type reports no known vulnerabilities,
indistinguishable in the output from one that genuinely has none.

This is the concrete reason a BOM with wrong identifiers is worse than no BOM — it looks
authoritative and joins to nothing.

# What to do instead

| | |
|---|---|
| **Conform to the open proposal**, if there is one | A third syntax matching neither the proposal nor anything else is not more honest than provisional alignment — just harder to migrate and impossible to join |
| **Vendor the proposal and test against its examples** | A paraphrase in prose drifts silently, because nothing can contradict it. A round-trip test over the published examples fails when either side moves |
| **Label the output provisional** | In the document itself, not only in the README — the document outlives the context it was generated in |
| **Do not fall back to `pkg:generic`** | It joins to nothing anyway, and creates a second scheme to migrate off later |
| **Gate 1.0 on approved *and* implemented** | An approved type that no consumer recognises produces the same empty joins as an unregistered one |

Declaring coverage status in the output is the companion control: if no advisory source covers the
ecosystem, say so rather than emitting a clean scan.

# Worked example

`ansible-bom` faced exactly this for the proposed `ansible` type. Its ADR-0004 records the decision
and, more usefully, records that an earlier revision **claimed conformance while emitting a
different shape**, and that the claim survived for months because the proposal had been paraphrased
into prose with nothing able to contradict it. The fix was structural — vendor the proposal, and
round-trip its published examples in a test — not editorial.[^ansible-bom-adr-0004]

# Related

- [purl](purl.md)
- [purl type definitions](purl-type-definitions.md) — where the examples that drive the test come from

[^type-definitions]: [purl type definitions](https://github.com/package-url/purl-spec/tree/main/types)
[^ansible-bom-adr-0004]: `ansible-bom` ADR-0004
