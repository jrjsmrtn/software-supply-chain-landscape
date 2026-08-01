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
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:58:00Z'
stale_after: 2026-11-01
sources:
  - id: tea-repo
    title: CycloneDX/transparency-exchange-api
    resource: https://github.com/CycloneDX/transparency-exchange-api
  - id: tea-discovery
    title: 'TEA Discovery: the TEI URN, types and DNS resolution'
    resource: https://github.com/CycloneDX/transparency-exchange-api/blob/main/discovery/readme.md
    last_modified: '2026-05-20'
---

The **Transparency Exchange Identifier** resolves to a specific Product Release. It is what makes
automated retrieval possible at all: without a resolvable identifier, [TEA](tea.md) would be an API
with no way to address anything.[^tea-repo]

Its role in the landscape mirrors [purl](/naming/purl.md)'s — purl names a *component* so documents
can join; TEI names a *release* so its documents can be found.

# Schema

**The syntax has since settled and is recorded here.** An earlier revision of this concept
deliberately omitted it as a moving target; the discovery specification now defines
it.[^tea-discovery]

```text
urn:tei:<type>:<domain-name>:<unique-identifier>
```

| Part | Meaning |
|---|---|
| `type` | defines the syntax of the identifier part — `purl`, `swid`, `uuid` among them |
| `domain-name` | resolves to a web server, **not necessarily the API host**. Uniqueness is registered when the TEI is created |
| `unique-identifier` | unique *within that domain*. A UUID is recommended, but an existing article code works |

```text
urn:tei:purl:cyclonedx.org:pkg:pypi/cyclonedx-python-lib@8.4.0?extension=whl&qualifier=py3-none-any
urn:tei:uuid:products.example.com:d4d9f54a-abcf-11ee-ac79-1a52914d44b1
```

Note the nesting in the first: a [purl](/naming/purl.md) sits inside the TEI as its identifier
component. TEI names a *release*; purl names a *component*.

> The TEI URN scheme **requires registration with IANA**, which is still outstanding.

# Resolution is DNS plus `.well-known`

The `domain-name` is queried in DNS — `A`, `AAAA` and `CNAME` records — giving the hosts serving
that product's transparency information. The client connects over HTTPS, **validates the
certificate**, and appends `/.well-known/tea`:[^tea-discovery]

```text
https://products.example.com/.well-known/tea
```

Which explains the design: a manufacturer publishes a TEI on an invoice, a QR code or an About box,
and a consumer's tooling turns it into an API endpoint with no prior agreement. The TEI is defined
by the manufacturer and **cannot generally be derived from information you already have** — it has
to be communicated.

# Related

- [TEA](tea.md) — the API this addresses into
- [purl](/naming/purl.md) — the component-level analogue

[^tea-repo]: [CycloneDX/transparency-exchange-api](https://github.com/CycloneDX/transparency-exchange-api)
[^tea-discovery]: [TEA Discovery specification](https://github.com/CycloneDX/transparency-exchange-api/blob/main/discovery/readme.md)
