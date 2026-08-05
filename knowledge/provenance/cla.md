---
type: Practice
title: Contributor License Agreement (CLA)
description: A signed contract granting a steward copyright and patent licences over contributions — unlike the DCO it grants rights rather than certifying them, and its employer clause is where contributors get blocked.
resource: https://www.apache.org/licenses/contributor-agreements.html
tags:
  - provenance
  - licensing
  - attestation
  - contribution
  - patents
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T06:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T06:45:00Z'
stale_after: 2027-08-01
sources:
  - id: apache-icla
    title: Apache Individual Contributor License Agreement V2.2
    resource: https://www.apache.org/licenses/icla.pdf
  - id: apache-agreements
    title: Contributor License Agreements — The Apache Software Foundation
    resource: https://www.apache.org/licenses/contributor-agreements.html
---

A **signed contract** between a contributor and a project's steward, executed once and held on file.
Where the [DCO](dco.md) is a certification the contributor *makes*, a CLA is a set of rights the
contributor *grants*.

There is no single CLA. Each steward publishes its own, and they differ in what they take. The
worked example here is Apache's **ICLA V2.2**, quoted throughout — it is the most widely encountered
and the most legible.[^apache-icla]

## It licenses; it does not assign

The most persistent misconception about CLAs is that they take ownership. Apache's does not:

> Except for the license granted herein to the Foundation and recipients of software distributed by
> the Foundation, You reserve all right, title, and interest in and to Your
> Contributions.[^apache-icla]

The copyright grant (§2) is *"a perpetual, worldwide, non-exclusive, no-charge, royalty-free,
irrevocable copyright license to reproduce, prepare derivative works of, publicly display, publicly
perform, sublicense, and distribute Your Contributions and such derivative works."*[^apache-icla]

**This is a property of Apache's agreement, not of CLAs as a category.** Others assign copyright, or
grant relicensing rights that permit proprietary redistribution. The actionable rule is that *"does
this project have a CLA?"* is not a useful question — **read the specific agreement**, because the
category tells you nothing about the terms.

## The patent grant is the part the DCO has no equivalent for

§3 grants a separate patent licence — *"to make, have made, use, offer to sell, sell, import, and
otherwise transfer the Work"* — limited to claims *"necessarily infringed by Your Contribution(s)
alone or by combination of Your Contribution(s) with the Work"*.[^apache-icla]

It carries **defensive termination**: if any entity brings patent litigation alleging that the
Contribution or the Work infringes, *"then any patent licenses granted to that entity under this
Agreement for that Contribution or Work shall terminate as of the date such litigation is
filed."*[^apache-icla]

The DCO grants no patent rights at all. For a steward whose risk model includes patents, that gap —
not authorship tracking — is usually the reason for requiring a CLA.

## §4 is where contributors get blocked

> You represent that you are legally entitled to grant the above license. If your employer(s) has
> rights to intellectual property that you create that includes your Contributions, you represent
> that you have received permission to make Contributions on behalf of that employer, that your
> employer has waived such rights for your Contributions to the Foundation, or that your employer
> has executed a separate Corporate CLA with the Foundation.[^apache-icla]

This is the practical difference from the DCO, and the reason a CLA belongs on a pre-work checklist
rather than a pre-merge one. A missing `Signed-off-by` is fixable in minutes by amending a commit.
A §4 problem requires **your employer** to act — waive rights, or sign a Corporate CLA — and that is
a process measured in weeks, if it succeeds at all.

A Corporate CLA does not substitute for the individual one: *"a Corporate CLA does not remove the
need for every developer to sign their own ICLA as an individual."*[^apache-agreements]

## Two clauses that create ongoing duties

- **§7 — third-party work is a separate submission.** Work that is not your original creation *"may
  submit it to the Foundation separately from any Contribution"*, identifying its source and any
  licence or restriction, *"conspicuously marking the work as 'Submitted on behalf of a
  third-party: [named here]'."*[^apache-icla] Compare the DCO's clause (c), which handles
  pass-through inline via the sign-off chain.
- **§8 — a continuing obligation.** *"You agree to notify the Foundation of any facts or
  circumstances of which you become aware that would make these representations inaccurate in any
  respect."*[^apache-icla] The agreement does not end at signature.

Contributions are also provided *"on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND"*, and support is explicitly not expected (§6).[^apache-icla]

## It is a personal legal instrument

The form states plainly: *"This is a legal contract containing Personally Identifiable
Information."*[^apache-icla] Starred fields *"will become part of your public profile"*, and Apache
recommends contributors *"use their personal email addresses in the contact details, rather than
their @work addresses"*, since the ICLA *"is not tied to any employer they may
have."*[^apache-agreements]

That advice is worth noting for its logic: the agreement follows the *person*, so binding it to an
employer address misrepresents what was signed and breaks when the job changes.

## DCO or CLA

| | [DCO](dco.md) | CLA |
|---|---|---|
| Contributor's act | certifies a right to submit | **grants** licences |
| Copyright | untouched | licensed (Apache) — varies by steward |
| Patents | silent | explicit grant, defensive termination (Apache) |
| Employer | not addressed | §4 representation — the common hard stop |
| Text | fixed, unmodifiable | per-steward, must be read individually |
| Mechanics | one line per commit, fixable after the fact | one signed contract, on file before contributing |
| Verification | none; a human claim | none; a human claim |

Neither is verified by anything. Both are self-representations, and the difference is in what is
represented and how expensive it is to get wrong.

## Related

- [DCO](dco.md) — the lighter-weight alternative most projects choose.
- Where organisations land on **AI-generated contributions** is a separate matter, decided partly
  through these instruments; the per-organisation records are in `ai-contribution-policies`
  (<https://github.com/jrjsmrtn/ai-contribution-policies>).

## Re-verification notes

Apache's forms are **versioned** (ICLA V2.2 at the time of writing) and are PDFs at stable URLs.
Note that `cla-corporate.txt` and its siblings **no longer exist** — plain-text forms now redirect
to a one-line notice pointing at the PDF, so a fetch that succeeds may still return no agreement.
Check for the clause text, not the HTTP status.

Everything quoted here is Apache-specific. Do not generalise the licence-not-assignment finding, the
patent grant or the §4 wording to another steward's agreement without reading that agreement.

[^apache-icla]: [Apache Individual Contributor License Agreement V2.2](https://www.apache.org/licenses/icla.pdf)
[^apache-agreements]: [Contributor License Agreements — The Apache Software Foundation](https://www.apache.org/licenses/contributor-agreements.html)
