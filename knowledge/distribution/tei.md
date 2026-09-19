---
type: Identifier
title: TEI (Transparency Exchange Identifier)
description: The URL that resolves to a specific Product Release — what makes automated artifact retrieval possible. Its syntax changed from a URN to a URL on 2026-09-18.
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
  - by: claude/opus-5
    at: '2026-09-20T10:00:00Z'
stale_after: 2026-12-20
sources:
  - id: tea-repo
    title: CycloneDX/transparency-exchange-api
    resource: https://github.com/CycloneDX/transparency-exchange-api
  - id: tea-discovery
    title: 'TEA Discovery: the TEI URL, types and DNS resolution'
    resource: https://github.com/CycloneDX/transparency-exchange-api/blob/main/discovery/readme.md
    last_modified: '2026-09-18'
---

The **Transparency Exchange Identifier** resolves to a specific Product Release. It is what makes
automated retrieval possible at all: without a resolvable identifier, [TEA](tea.md) would be an API
with no way to address anything.[^tea-repo]

Its role in the landscape mirrors [purl](/naming/purl.md)'s — purl names a *component* so documents
can join; TEI names a *release* so its documents can be found.

# Schema

⚠⚠ **The syntax changed on 2026-09-18, from a URN to a URL.** This concept recorded
`urn:tei:<type>:<domain-name>:<unique-identifier>` — colon-separated, type before domain. The
discovery specification now defines:[^tea-discovery]

```text
tei://<domain-name>/<type>/<unique-identifier>
```

**Nothing about the old form survives**: the scheme, the separator and the order of the two
segments all changed. A TEI written against the previous revision does not parse under this one, and
anything that stored or emitted the URN form has to be rewritten rather than migrated.

| Part | Meaning |
|---|---|
| `domain-name` | resolves to a web server, **not necessarily the API host**. Uniqueness is registered at creation. **A port number is not allowed** |
| `type` | defines the syntax of the identifier part. Types are declared in the specification; new ones go through Ecma TC54 |
| `unique-identifier` | unique *within that domain*. A UUID is recommended, but an existing article code works. Some types encode it **BASE64URL** (RFC 4648 §5) |

**Seven types are declared**, and the list is no longer software-shaped: `purl`, `hash`, `uuid`,
`ean`/`upc`, `gtin`, `asin`, `udi` — retail barcodes and a medical device identifier alongside the
package URL.[^tea-discovery] That breadth is the point of the `domain-name`-first design: a vendor
can address a release by whatever code it already prints on the box.

⚠ **`swid` is no longer among them.** An earlier revision of this concept listed it, and the
current document does not mention it at all — not as a type, not as deprecated. Note the contrast
with [purl](/naming/purl.md), which does still register a
[`swid` type](/naming/purl-type-definitions.md): the two identifier systems have diverged on it.

```text
tei://cyclonedx.org/purl/cGtnOnB5cGkvY3ljbG9uZWR4LXB5dGhvbi1saWJAOC40LjA_ZXh0ZW5zaW9uPXdobCZxdWFsaWZpZXI9cHkzLW5vbmUtYW55
tei://cyclonedx.org/uuid/d4d9f54a-abcf-11ee-ac79-1a52914d44b1
```

The first is `pkg:pypi/cyclonedx-python-lib@8.4.0?extension=whl&qualifier=py3-none-any`,
BASE64URL-encoded. A [purl](/naming/purl.md) still sits inside the TEI as its identifier component
— but it is **no longer readable in place**, which is a real loss for anyone eyeballing an
identifier and a real gain for anyone parsing one, since the purl's own `/`, `@` and `?` no longer
collide with the TEI's structure. That collision is the likeliest reason the form changed.

> The IANA note this concept carried — *the TEI URN scheme requires registration, still outstanding*
> — **is removed rather than updated.** It described a URN scheme that no longer exists, and the
> current document mentions IANA only to cite the `.well-known` URI registry. Whether the `tei://`
> URL scheme needs a registration of its own is not stated there, so nothing is claimed here.

# Resolution is DNS plus `.well-known`

The `domain-name` is queried in DNS — `A`, `AAAA` and `CNAME` records — giving the hosts serving
that product's transparency information. The client connects over HTTPS and **shall verify the
server certificate, including the server identity check of RFC 9525**, then appends
`/.well-known/tea`:[^tea-discovery]

```text
https://products.example.com/.well-known/tea
```

That endpoint returns a JSON document conforming to the **TEA Well-Known Schema**, listing the
available server endpoints **and the API versions each supports** — so version negotiation happens
at discovery rather than being assumed.[^tea-discovery]

Which explains the design: a manufacturer publishes a TEI on an invoice, a QR code or an About box,
and a consumer's tooling turns it into an API endpoint with no prior agreement. The TEI is defined
by the manufacturer and **cannot generally be derived from information you already have** — it has
to be communicated.

# Related

- [TEA](tea.md) — the API this addresses into
- [purl](/naming/purl.md) — the component-level analogue

[^tea-repo]: [CycloneDX/transparency-exchange-api](https://github.com/CycloneDX/transparency-exchange-api)
[^tea-discovery]: [TEA Discovery specification](https://github.com/CycloneDX/transparency-exchange-api/blob/main/discovery/readme.md)
