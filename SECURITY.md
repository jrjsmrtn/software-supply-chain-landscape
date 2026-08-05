# Security

This repository contains **documentation only** — Markdown knowledge concepts, no executable code,
no dependencies, no build. There is no attack surface in the usual sense, and a supported-versions
table would mean nothing.

What it can get wrong is a **claim**, and a wrong claim in a supply-chain reference has a real cost:
someone reads that a regulation requires X, or that a tool verifies Y, and acts on it. That is worth
reporting.

## Reporting an incorrect claim

Open an issue. Include:

- the concept, and the specific claim,
- the **primary source** that contradicts it — the specification, standard, enacting text or the
  tool's own documentation, not a summary,
- the date you read it.

Claims are corrected against primary sources only. A report without one is a useful prompt to
re-verify, but cannot itself change a concept.

**A concept past its `stale_after` is not a defect being hidden.** It is the mechanism working, and
the corpus is swept weekly for exactly that. Reporting a stale concept is still welcome — the sweep
says *when* to re-check, not *what changed*.

## Claims about tools and vulnerabilities

Concepts describe what tools and specifications do. If you believe a concept **understates a security
property** in a way that could lead someone to trust an artifact they should not — for example
describing a verification step as sufficient when it is not — say so explicitly in the report. That
class of error matters more than a stale version number.

Two known and deliberate limits, so they are not reported as defects: concepts state what an
instrument requires **of a document**, never whether it applies to your product or organisation; and
`cosign`'s concept records that verification without an expected identity proves nothing, which is a
property of the tool rather than an error here.

## Reporting a vulnerability

For anything genuinely security-relevant — a malicious link in a concept, or a supply-chain issue in
the gate tooling this repository invokes — use
[GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
rather than a public issue.

The gate scripts live in a separate repository and are not distributed with this bundle.
