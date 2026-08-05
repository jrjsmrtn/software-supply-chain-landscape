---
type: Practice
title: Commit trailers as provenance metadata
description: Git standardises the shape of trailers and nothing about their meaning — so every token's semantics, including the three rival AI-attribution tags, is per-project convention.
resource: https://git-scm.com/docs/git-interpret-trailers
tags:
  - provenance
  - attestation
  - attribution
  - contribution
  - ai
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:00:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:00:00Z'
stale_after: 2027-08-01
sources:
  - id: git-trailers
    title: git-interpret-trailers — Git documentation
    resource: https://git-scm.com/docs/git-interpret-trailers
  - id: kernel-submitting-patches
    title: 'Submitting patches — Linux kernel documentation'
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst
  - id: kernel-coding-assistants
    title: 'AI Coding Assistants — Linux kernel documentation'
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst
  - id: asf-generative-tooling
    title: Generative Tooling Guidance — The Apache Software Foundation
    resource: https://www.apache.org/legal/generative-tooling.html
  - id: openinfra-ai-policy
    title: AI Generated Content Policy — OpenInfra Foundation
    resource: https://openinfra.org/legal/ai-policy
---

The `Key: value` lines at the foot of a commit message — `Signed-off-by:`, `Reviewed-by:`,
`Fixes:` — are where most projects record contribution provenance. Git standardises **their shape
and nothing about their meaning**, which is the single most useful fact about them.

## What git actually defines

Trailers *"look similar to RFC 822 e-mail headers, at the end of the otherwise free-form part of a
commit message"*, rendered as `key: value` — *"one colon followed by one
space"*.[^git-trailers]

The parsing rules are stricter than they look, and worth knowing because a malformed block is
silently *not* a trailer block:[^git-trailers]

- **No whitespace before or inside the key.** Space and tab are allowed between key and separator.
- **The block must be preceded by one or more blank lines**, and must be at the end of the message
  or the last non-whitespace lines before a line starting with `---`.
- **A group qualifies if it is all trailers, or** *"contains at least one Git-generated or
  user-configured trailer and consists of at least 25% trailers."*
- Values may fold across lines, RFC 822 style, if continuation lines begin with whitespace.

That 25% threshold is the trap. A footer mixing trailers with prose can fall below it, at which
point **none** of the lines are trailers as far as tooling is concerned — while still looking
correct to a human reader.

Git is explicit that the resemblance to mail headers is partial: trailers *"do not follow (nor are
they intended to follow) many of the rules for RFC 822 headers."*[^git-trailers]

**Git defines no tokens.** `Signed-off-by:` has no more standing in git than `Banana:` does. Every
semantic below is project convention layered on top.

## The Linux kernel's vocabulary, and what each token means

The kernel's definitions are the de facto reference, because most other projects borrowed
them.[^kernel-submitting-patches]

| Token | Means |
|---|---|
| `Signed-off-by:` | the signer *"was involved in the development of the patch, or … was in the patch's delivery path"* — see [DCO](dco.md) |
| `Co-developed-by:` | *"the patch was co-created by multiple developers"* — **denotes authorship** |
| `Acked-by:` | approval by someone *"not directly involved in the preparation or handling"*; *"not as formal as Signed-off-by"* and *"also less formal than Reviewed-by"* |
| `Cc:` | a party was included in the discussion |
| `Assisted-by:` | an advanced coding tool was used — see below |

Two details that change how these should be read:

**`Acked-by:` may cover only part of a patch.** *"If a patch affects multiple subsystems and has an
Acked-by: from one subsystem maintainer then this usually indicates acknowledgement of just the part
which affects that maintainer's code."* A `# Suffix` can disambiguate:
`Acked-by: The Stakeholder <stakeholder@example.org> # As primary user`.[^kernel-submitting-patches]

**`Co-developed-by:` is structurally coupled to sign-off.** *"Since Co-developed-by: denotes
authorship, every Co-developed-by: must be immediately followed by a Signed-off-by: of the
associated co-author"*, and *"the last Signed-off-by: must always be that of the developer
submitting the patch."*[^kernel-submitting-patches]

## Naming a person in a trailer needs their permission

> Be careful in the addition of the aforementioned tags to your patches, as all except for `Cc:`,
> `Reported-by:`, and `Suggested-by:` need explicit permission of the person
> named.[^kernel-submitting-patches]

For those three, implicit permission suffices if the person used that name and address in the kernel
before and — for `Reported-by:` and `Suggested-by:` — reported or suggested in public. The kernel
also warns that bugzilla is public but the addresses used there are private, *"so do not expose them
in tags, unless the person used them in earlier contributions."*[^kernel-submitting-patches]

A trailer is not a neutral annotation: it publishes an association between a named person and a
change, permanently.

## The AI-attribution tags do not agree

Three conventions are in use, and they are **not** interchangeable spellings:

| Token | Used by | Value grammar |
|---|---|---|
| `Assisted-by:` | Linux kernel | `AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]`[^kernel-coding-assistants] |
| `Assisted-by:` | Ansible, Fedora | free-form tool name/version |
| `Generated-by:` | Apache Software Foundation | *"for future machine-parsable tracking"*[^asf-generative-tooling] |
| **both, distinguished** | OpenInfra | `Assisted-By:` for *predictive* tools, `Generated-By:` for *generative* ones[^openinfra-ai-policy] |

OpenInfra's split is the only stated semantics for the difference, and it is the one that makes
sense of the rest: *assisted* and *generated* name **two degrees of authorship**, so projects using
one token have adopted it for one degree and left the other unnamed. OpenInfra also treats its
labels as **mutable** — reviewers may remove one after substantial human rework — which is a
different theory of what a trailer is from everyone else's permanent-history reading.

In the kernel the tag is **required, not encouraged**: *"If you used any sort of advanced coding
tool in the creation of your patch, you need to acknowledge that use by adding an Assisted-by tag.
Failure to do so may impede the acceptance of your work."*[^kernel-submitting-patches]

### Why not `Co-developed-by:` for a tool

Because the kernel's own rules make it incoherent. `Co-developed-by:` *denotes authorship* and each
one *"must be immediately followed by a Signed-off-by: of the associated
co-author"*[^kernel-submitting-patches] — while the AI policy states that *"AI agents MUST NOT add
Signed-off-by tags. Only humans can legally certify the Developer Certificate of
Origin."*[^kernel-coding-assistants]

A `Co-developed-by:` naming a tool would therefore require a sign-off the policy forbids. The choice
of a distinct token is not stylistic: it is the only shape consistent with both rules. Guidance
recommending `Co-developed-by:` for AI attribution — which circulated widely before the kernel
policy landed — asks contributors to produce a structurally invalid trailer block.

## Practical consequences

- **Emit what the target project asks for.** There is no portable AI-attribution trailer, and a
  parser written for one grammar will not read another.
- **Do not invent tokens** expecting tooling to understand them. Git will happily carry
  `Vibes-by:`; nothing will act on it.
- **Keep the block clean.** Prose interleaved with trailers can drop the group below git's 25%
  threshold and make the whole block invisible to `git interpret-trailers`.
- **Check before naming a person.** Most tokens require their explicit permission.

## Related

- [DCO](dco.md) — what `Signed-off-by:` attests, and why sign-off chains are a custody trail rather
  than co-authorship.
- [CLA](cla.md) — the alternative instrument, which is a signed contract rather than a trailer.
- Which organisations require which AI trailer, and on what threshold, is recorded per-organisation
  in `ai-contribution-policies` (<https://github.com/jrjsmrtn/ai-contribution-policies>).

## Re-verification notes

Watch the **value grammars**, not just the token names — the kernel's
`AGENT_NAME:MODEL_VERSION [TOOLS]` shape is unusual, and a mechanically-emitted trailer that no
longer matches its spec is worse than none, because it looks compliant. The ASF describes
`Generated-by:` as anticipating machine-parsable tracking, so its grammar may tighten later.

Both kernel documents are in-tree, so `git log` on
`Documentation/process/submitting-patches.rst` and `coding-assistants.rst` is the audit trail and
outranks any rendered page.

[^git-trailers]: [git-interpret-trailers — Git documentation](https://git-scm.com/docs/git-interpret-trailers)
[^kernel-submitting-patches]: [Submitting patches — Linux kernel documentation](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst)
[^kernel-coding-assistants]: [AI Coding Assistants — Linux kernel documentation](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst)
[^asf-generative-tooling]: [Generative Tooling Guidance — The Apache Software Foundation](https://www.apache.org/legal/generative-tooling.html)
[^openinfra-ai-policy]: [AI Generated Content Policy — OpenInfra Foundation](https://openinfra.org/legal/ai-policy)
