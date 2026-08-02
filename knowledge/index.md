---
okf_version: "0.2"
---

# Start here

* [Understanding the Software Supply Chain Landscape](landscape.md) - The map. Read straight through once; everything below is looked *up*.

# Subdirectories

* [bom-types](bom-types/index.md) - The xBOM family: what each variant inventories, and whether it describes an artifact, a deployment or a process.
* [disclosure](disclosure/index.md) - Documents that travel with an artifact saying what it is for, and where it fails.
* [distribution](distribution/index.md) - How a consumer discovers and retrieves a release's artifacts.
* [formats](formats/index.md) - The BOM interchange formats, and the document-level practices that go with them.
* [intelligence](intelligence/index.md) - Vulnerability and lifecycle data, who issues it, and how findings are triaged.
* [licensing](licensing/index.md) - Licence identifiers and expressions, and the practices that make them trustworthy.
* [naming](naming/index.md) - How components and vulnerabilities are identified, and the registries behind those identifiers.
* [provenance](provenance/index.md) - How an artifact's origin is recorded, wrapped, and signed.
* [regulation](regulation/index.md) - Instruments that change what a bill of materials must contain, or when one must exist.
* [threats](threats/index.md) - How malicious code enters a dependency graph, and why inventory and provenance do not stop it.
* [tools](tools/index.md) - The runnable things, and the practices that make them safe.

# About this bundle

Every concept carries its own `sources`, its review state in `verified`, and an expiry in
`stale_after`. Facts are footnoted to the specific source that supports them, keyed to
`sources[].id`. A concept past its `stale_after` fails this repository's pre-commit gate — see
[`log.md`](log.md) for what has changed. Why the bundle is shaped this way is recorded in the
`supplychain-workspace` meta-project's decision log, which is private.
