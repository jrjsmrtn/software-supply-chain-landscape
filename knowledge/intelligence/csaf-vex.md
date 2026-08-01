---
type: Format
title: CSAF VEX
description: A VEX profile of OASIS CSAF — heavier than the alternatives, and favoured by large vendors.
resource: https://oasis-open.github.io/csaf-documentation/
tags:
  - vex
  - format
  - oasis
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:10:00Z'
stale_after: 2027-02-01
sources:
  - id: csaf
    title: 'OASIS CSAF: Common Security Advisory Framework'
    resource: https://oasis-open.github.io/csaf-documentation/
---

A **profile of CSAF** — the OASIS Common Security Advisory Framework — rather than a format of its
own.[^csaf] Heavier than [OpenVEX](openvex.md), and favoured by large vendors.

The weight is the point rather than an accident: CSAF is a full advisory framework with product
trees, branches and relationships, built for organisations publishing advisories across large
product portfolios. VEX is one profile of that machinery.

**Choose it when a consumer requires it.** Where the publisher is a small project and the consumer
is a scanner, OpenVEX or CycloneDX VEX carries the same verdict at a fraction of the authoring
cost. Where the consumer is a regulated buyer with a CSAF pipeline, none of that matters.

# Related

- [VEX](vex.md) — the concept and the state vocabularies
- [OpenVEX](openvex.md) — the minimal alternative

[^csaf]: [OASIS CSAF documentation](https://oasis-open.github.io/csaf-documentation/)
