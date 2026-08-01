---
type: Specification
title: SPDX AI and Dataset profiles
description: SPDX 3.0's structured metadata for AI systems and the datasets they are trained on — including energy, bias and safety fields CycloneDX has no equivalent for.
resource: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/
tags:
  - spdx
  - ai
  - dataset
  - ml-bom
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T21:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T21:50:00Z'
stale_after: 2027-02-01
sources:
  - id: spdx-ai
    title: 'SPDX 3.0.1: AI profile'
    resource: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/
  - id: spdx-dataset
    title: 'SPDX 3.0.1: Dataset profile'
    resource: https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Dataset/
  - id: lf-aibom
    title: 'Linux Foundation: Implementing AI Bill of Materials (AI BOM) with SPDX 3.0'
    resource: https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_spdx_aibom_102524a.pdf
---

Where [CycloneDX](cyclonedx.md) has one ML-BOM, [SPDX](spdx.md) 3.0 has **two profiles**: the model
is described by **AI**, the data it was trained on by **Dataset**. That split is the first thing to
know, and it is not cosmetic — a dataset has its own lifecycle, licensing and consent story
independent of any model built from it.[^spdx-ai][^spdx-dataset]

# AI profile

> "The AI Profile is designed to provide a standardized way of documenting and sharing information
> about AI software packages (i.e. systems)."[^spdx-ai]

Classes: `AIPackage`, `EnergyConsumption`, `EnergyConsumptionDescription`. Nineteen properties, two
vocabularies (`EnergyUnitType`, `SafetyRiskAssessmentType`).

| Grouping | Properties |
|---|---|
| Identity and behaviour | `typeOfModel`, `domain`, `autonomyType`, `informationAboutApplication`, `informationAboutTraining` |
| Training and evaluation | `hyperparameter`, `modelDataPreprocessing`, `metric`, `metricDecisionThreshold` |
| **Energy** | `energyConsumption`, `energyQuantity`, `energyUnit`, `trainingEnergyConsumption`, `finetuningEnergyConsumption`, `inferenceEnergyConsumption` |
| **Governance** | `limitation`, `modelExplainability`, `safetyRiskAssessment`, `standardCompliance`, `useSensitivePersonalInformation` |

# Dataset profile

> "The Dataset namespace defines concepts related to dataset, including its preparation process,
> its characteristics, and its access methods."[^spdx-dataset]

One class, `DatasetPackage`; three vocabularies (`ConfidentialityLevelType`,
`DatasetAvailabilityType`, `DatasetType`).

| Grouping | Properties |
|---|---|
| Characteristics | `datasetType`, `datasetSize`, `datasetNoise`, `intendedUse` |
| Provenance and upkeep | `dataCollectionProcess`, `dataPreprocessing`, `datasetUpdateMechanism`, `datasetAvailability`, `sensor` |
| **Privacy and fairness** | `hasSensitivePersonalInformation`, `anonymizationMethodUsed`, `confidentialityLevel`, `knownBias` |

# What is distinctive here

**Energy is first-class.** Six of nineteen AI properties describe it, separated by phase — training,
fine-tuning, inference. No other BOM format in this bundle models energy at all. That is a
sustainability and cost axis, and increasingly a reporting one.

**Governance is structured, not prose.** `knownBias`, `safetyRiskAssessment`, `modelExplainability`,
`useSensitivePersonalInformation`, `anonymizationMethodUsed`, `confidentialityLevel` are *fields*.
CycloneDX's ML-BOM documents "provenance and ethical considerations" as narrative; these are
queryable. For anyone facing an AI-governance regime, that difference decides which format can
answer an auditor mechanically.

**Neither profile replaces the other**, and neither replaces a software SBOM: a model ships inside
an application with ordinary dependencies. Expect all three.

# Related

- [ML-BOM](/bom-types/ml-bom.md) — the BOM type these express, alongside CycloneDX's
- [SPDX](spdx.md) — the profile mechanism and the full namespace list
- [CycloneDX](cyclonedx.md) — the other expression, stronger elsewhere

[^spdx-ai]: [SPDX 3.0.1 AI profile](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/)
[^spdx-dataset]: [SPDX 3.0.1 Dataset profile](https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Dataset/)
[^lf-aibom]: [Linux Foundation: Implementing AI BOM with SPDX 3.0](https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_spdx_aibom_102524a.pdf)
