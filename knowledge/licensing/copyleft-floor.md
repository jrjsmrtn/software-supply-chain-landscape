---
type: Practice
title: Copyleft floor
description: A bundled or statically linked artifact is governed by its most restrictive component — the wrapper's own licence does not raise the floor.
tags:
  - licensing
  - practice
  - distribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:55:00Z'
verified:
  - by: claude/opus-5
    at: \'2026-08-01T23:12:00Z\'
stale_after: 2027-08-01
sources:
  - id: spdx-license-list
    title: SPDX License List
    resource: https://spdx.org/licenses/
---

Applies whenever an artifact **vendors, bundles, statically links, or ships a container or WASM
image** containing third-party code.

What you distribute is an **aggregate**. Its floor is the most restrictive licence in it, and the
wrapper's own licence does not raise that floor. A `LICENSE` file at the repository root describes
the code you wrote — not the thing you ship.

# Obligations by distribution mode

| Distribution mode | What the floor obliges |
|---|---|
| Self-hosted / internal use | attribution, if the floor is permissive |
| Redistributing the artifact | offer source for copyleft components; satisfy each licence's terms |
| Offering it as a network service | AGPL §13 source-offer, if any AGPL component is present |

AGPL-3.0 §13 is headed *"Remote Network Interaction; Use with the GNU General Public License"*
and requires a modified version to *"prominently offer all users interacting with it remotely
through a computer network"* access to the source. Interaction over a network is the trigger —
not distribution of a binary.

# Two consequences that catch people

- An Apache-2.0 wrapper **statically linked** against a GPL-3.0 library ships a **GPL-3.0**-floored
  artifact, whatever its own licence says.
- **The floor is a function of how you distribute**, not only of what you depend on. A pivot from
  self-hosting to SaaS can change the obligation with no dependency change at all — which is why
  teams discover the AGPL network clause after launching rather than before.

# Practice

Record the floor **and the intended distribution mode** in an ADR — the `setup-adrs` skill
specifies a `LICENSING.md` for this — so that a later pivot re-triggers the review instead of
silently invalidating the analysis.

Cross-check that document's component table against the SBOM's per-component licence data rather
than maintaining it by hand. A hand-maintained inventory of what you bundle is the same class of
artifact as a hand-maintained dependency list, and decays the same way.

Note that the licences must be read as an [SPDX expression](spdx-license-expression.md) across the
aggregate: bundling is an `AND`, and `AND` accumulates obligations.

# Related

- [SPDX licence expression](spdx-license-expression.md) — `AND` is the bundling operator
- [Declared versus concluded](declared-vs-concluded.md) — a wrong component licence produces a
  wrong floor
- [REUSE](reuse.md) — per-file attribution for the vendored trees that create the floor
