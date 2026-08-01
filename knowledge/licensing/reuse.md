---
type: Practice
title: REUSE
description: The FSFE convention and toolchain for making copyright and licensing machine-readable in the source tree, enforced by a failing lint.
resource: https://reuse.software/
tags:
  - licensing
  - practice
  - tool
  - fsfe
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T11:55:00Z'
stale_after: 2027-02-01
sources:
  - id: reuse
    title: REUSE — FSFE
    resource: https://reuse.software/
  - id: reuse-action
    title: fsfe/reuse-action
    resource: https://github.com/fsfe/reuse-action
---

The FSFE convention for making copyright and licensing machine-readable **in the source tree**, so
a BOM generator reads facts rather than inferring them.[^reuse]

It attacks [declared-versus-concluded](declared-vs-concluded.md) at the root: the licence stops
being a manifest claim about a whole package and becomes a per-file fact.

# Schema

Repository layout it expects:

| Path | Contents |
|---|---|
| source files | inline `SPDX-FileCopyrightText` and `SPDX-License-Identifier` headers |
| `LICENSES/` | one full licence text per SPDX identifier used |
| `REUSE.toml` | bulk annotations — docs trees, generated files, and vendored code that must stay byte-pristine |

The `REUSE.toml` bulk-annotation path is what makes vendored third-party trees workable: they can
be attributed correctly without editing a single upstream file.

# Commands

| Command | Purpose |
|---|---|
| `reuse lint` | the gate — non-zero exit when any file lacks copyright/licence information |
| `reuse annotate --license <SPDX> --copyright "<holder>" <paths>` | add SPDX headers in bulk |
| `reuse download <SPDX>` | fetch a licence text into `LICENSES/` |
| `reuse spdx` | emit an SPDX document for the repository's own files |

# Examples

Enforce in both places — a hook *and* a CI job. Prose asking contributors to add headers does not
survive contact with a pull request; a failing check does.

```yaml
# .lefthook.yml
reuse:
  run: reuse lint
```

```yaml
# .github/workflows/ci.yml — SHA-pin the action
- uses: fsfe/reuse-action@<sha>   # v5
```

# What it is not

`reuse spdx` covers **the repository's own files**, not its dependency tree. It is not a substitute
for `syft` or `cdxgen`.[^reuse-action] The two answer different questions: *what did we write, and
under what terms* versus *what did we pull in*. A project needs both, and conflating them produces
an SBOM that is confidently wrong about everything it did not author.

# Related

- [Declared versus concluded](declared-vs-concluded.md) — the problem this is upstream of
- [SPDX License List](spdx-license-list.md) — the identifiers the headers carry
- [Copyleft floor](copyleft-floor.md) — REUSE attributes the components; the floor is what they add up to

[^reuse]: [REUSE — FSFE](https://reuse.software/)
[^reuse-action]: [fsfe/reuse-action](https://github.com/fsfe/reuse-action)
