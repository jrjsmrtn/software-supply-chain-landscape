---
type: Organization
title: EEF Ægis
description: The Erlang Ecosystem Foundation's security initiative for the BEAM ecosystem, of which its CNA is one workstream.
resource: https://security.erlef.org/
tags:
  - vulnerability
  - organization
  - beam
  - elixir
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T22:45:00Z\'
stale_after: 2027-02-01
sources:
  - id: aegis
    title: EEF Security WG
    resource: https://security.erlef.org/
  - id: eef-cna
    title: Erlang Ecosystem Foundation CNA
    resource: https://cna.erlef.org/
---

The Erlang Ecosystem Foundation's security initiative for the BEAM ecosystem.[^aegis] Its
[CNA](cna.md) is one workstream within it.

| | |
|---|---|
| Authorized as a CNA | 2025-05 — from the ecosystem announcement; **not stated on the CNA's own pages**, so treat the month as secondary-sourced |
| Scope | active packages on Hex.pm; projects under `elixir-lang`, `erlang`, `erlef`, `erlef-cna`, `gleam-lang` |
| Fallback | acts as CNA for all Hex.pm packages outside a more specific scope |
| Publication | records are also published to OSV |
| Embargo | *"The maximum embargo period is 3 months."*[^eef-cna] |

# Why it is named here

It is the worked example closest to this portfolio's Elixir projects. **The general pattern is what
transfers**, not the specific initiative: an ecosystem foundation taking ownership of disclosure for
its own registry, and feeding the result into [osv.dev](osv-dev.md) rather than only into CVE.

The fallback role is the part worth copying. Covering "all Hex.pm packages" by default means a
package with no dedicated CNA still has somewhere to go, which is exactly the gap that produces
inferred version ranges elsewhere.

# Related

- [CNA](cna.md) — the general mechanism
- [osv.dev](osv-dev.md) — where the records land

[^aegis]: [EEF Security WG](https://security.erlef.org/)
[^eef-cna]: [Erlang Ecosystem Foundation CNA](https://cna.erlef.org/)
