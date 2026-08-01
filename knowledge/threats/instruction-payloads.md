---
type: Attack
title: Instruction payloads
description: Artifacts whose payload is natural-language instructions rather than code — so the attack surface is prose, and conventional scanning does not see it.
resource: https://owasp.org/www-project-agentic-skills-top-10/
tags:
  - threat
  - ai
  - agent
  - scanning
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T22:13:20Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:13:20Z'
stale_after: 2026-12-01
sources:
  - id: owasp-ast10
    title: 'OWASP Agentic Skills Top 10'
    resource: https://owasp.org/www-project-agentic-skills-top-10/
    last_modified: '2026-07-31'
  - id: cve-2026-25253
    title: 'CVE-2026-25253'
    resource: https://api.osv.dev/v1/vulns/CVE-2026-25253
---

A growing class of distributed artifact carries **instructions for an agent** rather than code for a
machine: agent skills, prompt templates, tool definitions — and, note, **OKF bundles like this
one**.

They are packaged like software. They are published to registries, resolved by name, versioned,
installed, and updated. Every supply-chain mechanism in this bundle applies to them.

# Why this needs its own entry

**The malicious payload is prose.**

A hostile dependency contains code — a `subprocess` call, an obfuscated blob, a network write.
Static analysis is imperfect at finding it but is looking at the right thing. A hostile instruction
artifact contains a *sentence*: read this file, send its contents there, ignore the instruction
above. There is no `eval()`, no import, no syscall. **A scanner that greps for dangerous constructs
sees a document and reports nothing.**

That is a genuinely different property from everything else in this bundle, and it inverts a working
assumption: that "no findings" from a code scanner is weak evidence of safety. Here it is no
evidence at all, because the scanner is not looking at the payload.

The second-order problem: the reviewer is also the target. Prose written to influence an agent is
often unremarkable to a person skimming a diff.

# It is a real class, not a projection

[OWASP runs an Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/), at v1
public review as of 2026-07, with per-risk codes `AST01`–`AST10`, an incident timeline, case studies
and threat intelligence.[^owasp-ast10] Agentic systems have begun accruing
CVEs — `CVE-2026-25253` is retrievable from OSV like any other.[^cve-2026-25253]

> **Scope.** Most of that Top 10 is *runtime* agent security — prompt injection, excessive
> permission, exfiltration — which is application security rather than supply chain and is not
> covered here. What belongs in this bundle is the **distribution** half: how a hostile instruction
> artifact reaches an installation in the first place.

# What carries over, and what does not

The distribution-side threats are the same ones, unchanged:

- [Typosquatting](typosquatting.md) and [dependency confusion](dependency-confusion.md) work
  identically against a skill marketplace — arguably better, since these registries are young and
  namespacing is thinner.
- [Maintainer compromise](maintainer-compromise.md) is unchanged.
- [Update cooldown](/tools/update-cooldown.md) and installing from a pinned manifest are the same
  mitigations.
- [model-signing](/provenance/model-signing.md) already works: a skill is a directory tree, and
  NVIDIA signs its catalogue that way.

What does **not** carry over is the detection layer. There is no equivalent of a vulnerability
database for prose, no `MAL-` feed for instruction artifacts, and no static analysis with the
soundness properties a compiler-oriented tool can offer.

# Practice

- **Read the artifact.** For an instruction payload this is not a fallback; it is the primary
  control. It is also tractable, because these files are short.
- **Pin and diff.** The change under review is prose, so review it as prose.
- **Sign and verify what you publish**, so consumers can at least establish that a reviewed artifact
  has not changed since — [model-signing](/provenance/model-signing.md).
- **Do not treat a clean scanner run as a signal.** It is measuring the wrong thing.

# Related

- [Typosquatting](typosquatting.md) · [Dependency confusion](dependency-confusion.md) ·
  [Maintainer compromise](maintainer-compromise.md) — the distribution threats, unchanged
- [model-signing](/provenance/model-signing.md) — directory-tree signing, already applicable
- [Update cooldown](/tools/update-cooldown.md)

[^owasp-ast10]: [OWASP Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/)
[^cve-2026-25253]: [CVE-2026-25253 in OSV](https://api.osv.dev/v1/vulns/CVE-2026-25253)
