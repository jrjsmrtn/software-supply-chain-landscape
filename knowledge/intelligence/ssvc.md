---
type: Practice
title: SSVC (Stakeholder-Specific Vulnerability Categorization)
description: A decision model that outputs an action rather than a score — Track, Track*, Attend, Act. The "stakeholder-specific" half is why a central publisher can only ever fill in part of it.
resource: https://certcc.github.io/SSVC/
tags:
  - triage
  - vulnerability
  - prioritisation
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-07T09:15:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-07T09:15:00Z'
stale_after: 2027-02-01
sources:
  - id: certcc-ssvc
    title: 'SSVC — CERT Coordination Center, Carnegie Mellon University'
    resource: https://certcc.github.io/SSVC/
  - id: cisa-ssvc
    title: 'CISA Stakeholder-Specific Vulnerability Categorization Guide'
    resource: https://www.cisa.gov/sites/default/files/publications/cisa-ssvc-guide%20508c.pdf
---

**SSVC is a decision model, not a scoring system.** Where CVSS produces a number that an organisation
must then convert into an action by policy, SSVC walks a decision tree and produces the action
directly.[^certcc-ssvc]

It is a **CERT Coordination Center / Carnegie Mellon University** model.[^certcc-ssvc] CISA operates a
customised tree over it and publishes a guide for that tree[^cisa-ssvc] — the same distinction the
corpus draws for [the six SBOM types](/formats/sbom-types.md): the operator and the author are not
the same party, and "CISA's SSVC" is one instantiation of a model owned elsewhere.

# The output is four decisions

| Outcome | CISA's remediation guidance[^cisa-ssvc] |
|---|---|
| **Track** | No action now; reassess if new information appears. Remediate "within standard update timelines" |
| **Track\*** | Characteristics that "may require closer monitoring for changes". Still standard timelines |
| **Attend** | Needs supervisory-level attention, possibly a notification. "Sooner than standard update timelines" |
| **Act** | Supervisory *and* leadership attention, internal groups meet and agree a response. "As soon as possible" |

**These are organisational verbs, not severity bands.** "Attend" names who has to look at it; "Act"
names a meeting that has to happen. That is the substantive difference from a score — the output is
already the decision, so no local policy layer has to translate it.

# The decision points, and which are yours

CISA's tree uses these:[^cisa-ssvc]

| Decision point | Values |
|---|---|
| **(State of) Exploitation** | `None`, `Public PoC`, `Active` |
| **Technical Impact** | `Partial`, `Total` |
| **Automatable** | `No`, `Yes` |
| **Mission Prevalence** | `Minimal`, `Support`, `Essential` |
| **Public Well-Being Impact** | `Minimal`, `Material`, `Irreversible` |

**The split matters more than the list.** The first three are properties of the *vulnerability* —
anyone analysing it reaches the same answer. The last two are properties of *your deployment*: whether
the vulnerable component supports your mission-essential functions, and what harm follows in your
context.

This is precisely why the [CISA ADP](adp.md) publishes **only the first three** into CVE records.
A central publisher can answer questions about the flaw; it cannot answer questions about your
mission. **The name is the design** — the model is stakeholder-*specific*, so the stakeholder must
supply the half that depends on them.

# Two properties worth knowing before relying on it

**There is no "unknown" value, deliberately.** From the guide: *"One important omission from the
values for each decision point below is an 'unknown' option. Instead of declaring a decision point as
'unknown,' CISA identifies the value that is the most reasonable assumption based on prior
events."*[^cisa-ssvc] The guide immediately qualifies it — the approach "requires reliable historical
evidence and future events may change these assumptions over time."

So a published decision point is **an assumption where evidence was thin**, not necessarily an
observation. That is a defensible design for a model that must always produce an answer, and a trap
for anyone reading the values as measurements.

**Exploitation is a present-tense observation with a shelf life.** It "does not predict future
exploitation" and reflects "information at time of analysis"; because the state changes, "answers
should be time-stamped".[^cisa-ssvc] An `Exploitation: None` from six months ago asserts nothing about
today.

# Related

- [ADP](adp.md) — the container through which CISA publishes three of these decision points per CVE
- [CISA](cisa.md) — and [KEV](cisa.md), which is the same signal as `Exploitation: Active` reached by a
  different route
- [VEX](vex.md) — the adjacent question. VEX asks *does this vulnerability affect my product at all*;
  SSVC asks *given that it does, what should I do*. Neither substitutes for the other

[^certcc-ssvc]: [SSVC — CERT Coordination Center, Carnegie Mellon University](https://certcc.github.io/SSVC/)
[^cisa-ssvc]: [CISA Stakeholder-Specific Vulnerability Categorization Guide](https://www.cisa.gov/sites/default/files/publications/cisa-ssvc-guide%20508c.pdf)
