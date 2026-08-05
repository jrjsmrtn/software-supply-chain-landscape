---
type: Practice
title: Developer Certificate of Origin (DCO)
description: A 200-word certificate a contributor attests to with a Signed-off-by line — it asserts the right to submit, never authorship, and its text may not be modified.
resource: https://developercertificate.org/
tags:
  - provenance
  - licensing
  - attestation
  - contribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T06:30:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T06:30:00Z'
stale_after: 2027-08-01
sources:
  - id: dco-canonical
    title: Developer Certificate of Origin 1.1
    resource: https://developercertificate.org/
  - id: kernel-submitting-patches
    title: 'Submitting patches — Linux kernel documentation (section: Sign your work)'
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst
---

A short certificate — four clauses, about 200 words — that a contributor attests to by adding one
line to a commit message. Version 1.1, *"Copyright (C) 2004, 2006 The Linux Foundation and its
contributors."*[^dco-canonical]

The attestation is the line itself:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```

`git commit -s` adds it; `git revert -s` does the same for reverts.[^kernel-submitting-patches]

## What it actually certifies

Read the clauses for what they claim, because the common summary — *"I wrote this"* — is not what
any of them says:[^dco-canonical]

- **(a)** the contribution *"was created in whole or in part by me and I have the right to submit it
  under the open source license indicated in the file"*; **or**
- **(b)** it is *"based upon previous work that, to the best of my knowledge, is covered under an
  appropriate open source license"* and the contributor has the right under that licence to submit
  it, with modifications, under the same licence; **or**
- **(c)** it *"was provided directly to me by some other person who certified (a), (b) or (c) and I
  have not modified it"*; **and**
- **(d)** the contributor understands the contribution and its record — *"including all personal
  information I submit with it, including my sign-off"* — is public and *"maintained
  indefinitely"*.

**(a), (b) and (c) are alternatives.** Only (a) mentions creating anything, and even it says *"in
whole or in part"*. The load-bearing assertion across all three is **the right to submit under the
stated licence**. (c) covers pure pass-through of work you did not write and did not touch.

Clause (d) is the one contributors overlook: it is a **standing consent to permanent publication of
personal data**, which is why sign-off requires *"a known identity (sorry, no anonymous
contributions.)"*[^kernel-submitting-patches]

## The text may not be modified

> Everyone is permitted to copy and distribute verbatim copies of this license document, but
> changing it is not allowed.[^dco-canonical]

A project adopts the DCO as-is or adopts something else. There is no house variant, and a "modified
DCO" is a contradiction rather than a stricter policy.

A project needing different terms needs a **[CLA](cla.md)** — a different instrument entirely, which
*grants* rights to a steward rather than certifying a contributor's right to submit, and whose
employer clause can be a hard stop for contributors bound by one.

## Its stated purpose is tracking, not enforcement

The kernel introduced sign-off *"to improve tracking of who did what, especially with patches that
can percolate to their final resting place in the kernel through several layers of
maintainers."*[^kernel-submitting-patches]

That framing matters for how much weight a DCO can bear. It is a **self-certification**: nothing
verifies it, and no third party attests to it. Compare [SLSA](slsa.md), which grades a *build
process*, and [in-toto](in-toto.md), which wraps machine-checkable attestations. The DCO records a
human claim, and its value is that the claim is on the record and attributable — not that anyone
checked it.

## Sign-off chains carry routing information

Beyond the first line, the chain is a provenance record in its own right:[^kernel-submitting-patches]

- *"Any further SoBs … following the author's SoB are from people handling and transporting the
  patch, but were not involved in its development."*
- *"SoB chains should reflect the **real** route a patch took"*, with *"the first SoB entry
  signalling primary authorship of a single author."*
- Extra tags after a sign-off *"will just be ignored for now"*, but may mark internal company
  procedures.

So a multi-SoB commit is not multiple authors — it is a custody trail. Reading it as co-authorship
misattributes the work to maintainers who only forwarded it.

## Where it is load-bearing, and where it is not

The DCO's four clauses are the pivot in most projects' reasoning about **AI-generated
contributions**, because clauses (a)–(c) all require knowing the licence status of what you submit.
That reasoning does not resolve one way: organisations reading the same certificate reach
prohibition, volume-scoped caution, relocated certification, and permission-on-other-grounds.

Those are decisions about policy rather than facts about the instrument, and they live in the
`ai-contribution-policies` bundle
(<https://github.com/jrjsmrtn/ai-contribution-policies>) — one record per organisation, with its own
sourcing and expiry. **The DCO does not by itself determine a stance**, which is the most useful
thing to know about it in that context.

## Related

- [SLSA](slsa.md) — grades the build process; the DCO says nothing about how an artifact was built.
- [in-toto](in-toto.md) — machine-verifiable attestation, where the DCO is a human claim.
- [REUSE](../licensing/reuse.md) — the other short, adopt-verbatim convention in this corpus; it
  makes *file-level licensing* explicit where the DCO makes *the right to submit* explicit.

## Re-verification notes

The canonical text is at `developercertificate.org` and is reproduced identically in the kernel's
`Documentation/process/submitting-patches.rst`; **the two agreeing is itself the check**, since a
divergence would mean one had been edited despite the no-modification clause. Version 1.1 has been
stable since 2006, so treat any version change as significant rather than routine. The *procedural*
material — `git commit -s`, chain semantics, the anonymity rule — is kernel-specific practice around
a shared certificate; other projects adopt the certificate without necessarily adopting the chain
conventions.

[^dco-canonical]: [Developer Certificate of Origin 1.1](https://developercertificate.org/)
[^kernel-submitting-patches]: [Submitting patches — Linux kernel documentation (section: Sign your work)](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst)
