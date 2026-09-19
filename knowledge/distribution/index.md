# Transparency Exchange

* [TEA (Transparency Exchange API)](tea.md) - Format-agnostic discovery and retrieval of a release's supply-chain artifacts.
* [TEI (Transparency Exchange Identifier)](tei.md) - The `tei://` URL a consumer resolves to reach a Product Release.

Both carry `status: draft` and a short `stale_after`. TEA is at Beta 2 and unratified — the least
settled layer in the landscape, and the only part of this bundle where the specification is
expected to move before the concepts expire.

**That expectation was met on 2026-09-18**, when the TEI syntax changed from a URN to a URL —
a breaking change to an identifier, 42 days before these concepts were due for review. Nothing in
this bundle would have flagged it; a scheduled re-read did. Treat anything built on these two as a
bet on a moving specification, and re-read before relying on either.
