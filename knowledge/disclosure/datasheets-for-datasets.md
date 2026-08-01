---
type: Practice
title: Datasheets for datasets
description: Documentation travelling with a dataset — why it was collected, what is in it, how it was gathered, and who maintains it.
resource: https://arxiv.org/abs/1803.09010
tags:
  - disclosure
  - dataset
  - documentation
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T22:13:20Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T22:13:20Z'
stale_after: 2027-08-01
sources:
  - id: gebru
    title: 'Gebru et al., Datasheets for Datasets'
    resource: https://arxiv.org/abs/1803.09010
    last_modified: '2018-03'
---

Proposed by Gebru et al., **explicitly modelled on electronics datasheets**: a component you might
solder into a circuit ships with operating conditions and tolerances, and a dataset you might train
on should too.[^gebru]

A datasheet documents a dataset's **motivation, composition, collection process, labelling,
distribution, and maintenance** — organised as questions the creator answers rather than fields to
fill.[^gebru]

# Why the dataset needs its own document

A dataset is not an implementation detail of a model. It **outlives the models built from it** and
is reused across them, carrying its licensing, consent and collection circumstances into every one.
A [model card](model-cards.md) that names a training set without describing it passes the hardest
questions downstream.

Those questions are also the ones that cannot be reconstructed later. Whether subjects consented,
whether collection was representative, whether scraping respected terms — none is recoverable by
inspecting the data afterwards. Provenance here has to be recorded at collection time or not at all.

# The structural echo

This is the same split [SPDX](/formats/spdx-ai-profile.md) makes: an **AI** profile for the model
and a **Dataset** profile for the data, rather than one document for both. The datasheet is the
narrative form; the profile turns the same questions into
fields — `dataCollectionProcess`, `knownBias`, `hasSensitivePersonalInformation`,
`anonymizationMethodUsed`, `confidentialityLevel`.

[CycloneDX](/formats/cyclonedx.md) folds datasets into its ML-BOM instead. Which is right depends on
whether the dataset is a subject in its own right, and for anything with consent or licensing
questions attached, it is.

# Related

- [Model cards](model-cards.md) — the counterpart for the model
- [SPDX AI and Dataset profiles](/formats/spdx-ai-profile.md) — the structured expression
- [ML-BOM](/bom-types/ml-bom.md)

[^gebru]: [Gebru et al., *Datasheets for Datasets*](https://arxiv.org/abs/1803.09010)
