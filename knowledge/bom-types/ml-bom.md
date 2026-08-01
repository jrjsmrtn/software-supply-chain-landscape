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

# Related

- [SBOM](sbom.md) — the framework and library dependencies underneath a model still need one
- [cdxgen](/tools/cdxgen.md) — generates AI-BOM

[^cdx-mlbom]: [CycloneDX: ML-BOM](https://cyclonedx.org/capabilities/mlbom/)
