---
type: BOM Type
title: CBOM
description: Cryptographic Bill of Materials — algorithms, keys and certificates, and their relationships to software components.
resource: https://cyclonedx.org/capabilities/cbom/
tags:
  - bom-type
  - cbom
  - cryptography
  - post-quantum
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
  - by: claude/opus-5
    at: '2026-08-01T12:41:35Z'
stale_after: 2027-02-01
sources:
  - id: cdx-cbom
    title: 'CycloneDX: CBOM'
    resource: https://cyclonedx.org/capabilities/cbom/
  - id: cdx-schema-17
    title: 'CycloneDX 1.7 JSON schema: cryptoProperties'
    resource: https://github.com/CycloneDX/specification/blob/master/schema/bom-1.7.schema.json
---

**"Detailed representation of cryptographic assets within a system. This includes algorithms,
keys, certificates, and their relationships to software components."**[^cdx-cbom]

The relationships are the load-bearing part: not just *which* algorithms exist, but **where each
one is used** — this certificate signed with that algorithm, provided by that library, used by that
service. That is what makes the blast radius of retiring an algorithm computable.

# Schema

The capability page names algorithms, keys and certificates. **The schema is broader**, and is the
authority: `cryptoProperties.assetType` takes exactly four values, **identical in CycloneDX 1.6 and
1.7**, each with its own properties object.[^cdx-schema-17]

| `assetType` | Covers |
|---|---|
| `algorithm` | the primitives themselves |
| `certificate` | X.509 and friends |
| `protocol` | how the primitives are used on the wire |
| `related-crypto-material` | keys and other secret or derived material |

Two corrections follow, and both matter for how a CBOM is read:

- **Protocols *are* first-class**, with a `protocolProperties.type` enum: `tls`, `ssh`, `ipsec`,
  `ike`, `sstp`, `wpa`, `dtls`, `quic`, `eap-aka`, `eap-aka-prime`, `prins`, `5g-aka`, `other`,
  `unknown`. The capability page simply does not enumerate them.
- **"Keys" is not an asset type.** Keys are `related-crypto-material`, whose `type` enum spans
  `private-key`, `public-key`, `secret-key`, `key`, `ciphertext`, `signature`, `digest`,
  `initialization-vector`, `nonce`, `seed`, `salt`, `shared-secret`, `tag`, `additional-data`,
  `password`, `credential`, `token`, `other`, `unknown`.

So the accurate short form is **algorithms, certificates, protocols, and related material
(including keys)** — not the three the capability page lists, and not the loose "algorithms,
protocols, keys, certificates" either.

# Why this one has a deadline

CycloneDX frames CBOM around the **post-quantum transition**, naming compliance with the US
National Security Memorandum on Post-Quantum Cryptography, and positions it as helping organisations
move to quantum-safe practice.[^cdx-cbom]

The reasoning behind that deadline — why a quantum computer breaks current cryptography, and why
"harvest now, decrypt later" makes it urgent for anything needing long-term confidentiality — is
durable rationale and lives in
[the landscape explanation](/landscape.md#cbom--finding-the-crypto-before-it-breaks),
not here.

# A worked line item

This workspace's own private git server negotiates a classical, non-post-quantum SSH key exchange.
As a CBOM entry that is one component with `assetType: protocol` and
`protocolProperties.type: ssh`, related to the algorithm assets it negotiates — which is what makes
"where is the classical crypto" a query rather than an audit.

# Related

- [SBOM](sbom.md) — CBOM assets are related back to software components
- [cdxgen](/tools/cdxgen.md) — generates CBOM

[^cdx-cbom]: [CycloneDX: CBOM](https://cyclonedx.org/capabilities/cbom/)
[^cdx-schema-17]: [CycloneDX 1.7 JSON schema](https://github.com/CycloneDX/specification/blob/master/schema/bom-1.7.schema.json)
