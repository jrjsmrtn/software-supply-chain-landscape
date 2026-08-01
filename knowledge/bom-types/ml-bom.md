---
type: BOM Type
title: ML-BOM
description: Machine Learning Bill of Materials — datasets, models and configurations for AI and ML systems, with dataset provenance.
resource: https://cyclonedx.org/capabilities/mlbom/
tags:
  - bom-type
  - ml-bom
  - ai
  - machine-learning
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-01T12:37:50Z'
verified:
  - by: claude/opus-5
    at: '2026-08-01T12:37:50Z'
stale_after: 2027-02-01
sources:
  - id: cdx-mlbom
    title: 'CycloneDX: ML-BOM'
    resource: https://cyclonedx.org/capabilities/mlbom/
  - id: spdx-ai
    title: 'SPDX 3.0.1: AI profile'
    resource: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/
---

CycloneDX calls it **ML-BOM** (Machine Learning Bill of Materials), also written
**AI/ML-BOM**.[^cdx-mlbom]

It represents **"datasets, models, and configurations for AI and machine learning systems"** —
including the provenance of datasets, training methodologies, and the configuration of AI
frameworks.

# It documents ethics, not only composition

The distinguishing claim upstream makes: an ML-BOM **"documents provenance and ethical
considerations for datasets"**.[^cdx-mlbom]

No other member of the family carries a field for that, and it reflects what actually goes wrong
with ML systems. The failure is rarely a CVE in a library; it is a dataset whose licensing,
consent, or representativeness cannot be established after the fact. Provenance of *training data*
is the supply-chain question here, and it is the one hardest to reconstruct later.

Models and datasets are inventoried; **training data is covered through dataset provenance rather
than as a separate category**.

# The two formats model this differently

This is the BOM type where CycloneDX and SPDX diverge most, and it is worth knowing which one
answers your question before picking.[^spdx-ai]

| | CycloneDX | SPDX 3.0 |
|---|---|---|
| Shape | one **ML-BOM** covering datasets, models and configurations | **two profiles** — AI for the model, Dataset for the data |
| Governance data | narrative "provenance and ethical considerations" | structured fields: `knownBias`, `safetyRiskAssessment`, `modelExplainability`, `anonymizationMethodUsed` |
| Energy | not modelled | six properties, split by training / fine-tuning / inference |

The split matters beyond tidiness: a dataset outlives and is reused across models, with its own
licensing and consent story. SPDX lets it be a first-class subject; CycloneDX describes it in the
model's document.

If an auditor must be answered mechanically rather than by reading prose, that is the deciding
difference — see [SPDX AI and Dataset profiles](/formats/spdx-ai-profile.md).

# Related

- [SBOM](sbom.md) — the framework and library dependencies underneath a model still need one
- [cdxgen](/tools/cdxgen.md) — generates AI-BOM
- [SPDX AI and Dataset profiles](/formats/spdx-ai-profile.md) — the other expression
- [Model cards](/disclosure/model-cards.md) · [Datasheets for datasets](/disclosure/datasheets-for-datasets.md)
  — the narrative counterparts: a BOM says what a model is made of, a card says what it is for

[^cdx-mlbom]: [CycloneDX: ML-BOM](https://cyclonedx.org/capabilities/mlbom/)
[^spdx-ai]: [SPDX 3.0.1 AI profile](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/)
