---
type: Practice
title: Model cards
description: Documentation travelling with a trained model — intended use, the conditions under which performance varies, and known limitations.
resource: https://arxiv.org/abs/1810.03993
tags:
  - disclosure
  - ai
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
  - id: mitchell
    title: 'Mitchell et al., Model Cards for Model Reporting (FAT* 2019)'
    resource: https://arxiv.org/abs/1810.03993
    last_modified: '2019-01'
  - id: hf-model-cards
    title: 'Hugging Face: Model Cards'
    resource: https://huggingface.co/docs/hub/model-cards
---

Introduced by Mitchell et al. in 2019 and now the de-facto convention. A model card reports the
**type of model, its intended use cases, the attributes for which performance may vary, measures of
performance, and ethical considerations**.[^mitchell]

The load-bearing section is the one people skip: *intended use*, and its shadow, **out-of-scope
use**. A model that performs well on its evaluation set and badly on a population it was never
trained for is not defective — it is being used outside its card.

# What it is, concretely

On Hugging Face a model card **is the repository's `README.md`**: a markdown file with a YAML
frontmatter block.[^hf-model-cards] The split matters — the frontmatter is machine-readable, the
body is for people.

Frontmatter carries `license` (with `license_name` / `license_link` for custom terms), `datasets`,
`pipeline_tag`, `library_name`, `language`, `tags`, a `model-index` of structured evaluation
results, and `new_version`.

# Lineage is in the frontmatter

`base_model` records what a model was derived from, and `base_model_relation` types the edge —
`finetune`, `adapter`, `quantized`, or `merge`, the last taking a list of two or more
parents.[^hf-model-cards]

**That is a dependency graph for models**, in the same sense an [SBOM](/bom-types/sbom.md) carries
one for software — and it is the field to read when asking what a fine-tune inherited, including
whatever was wrong with its parent.

# Card versus BOM versus profile

Three artifacts describe a model and they are not interchangeable:

| | Answers |
|---|---|
| **Model card** | what is it *for*, and where does it fail |
| [**ML-BOM**](/bom-types/ml-bom.md) | what is it *made of* |
| [**SPDX AI profile**](/formats/spdx-ai-profile.md) | the same ground as the card, but as **queryable fields** rather than prose |

The card is narrative and human-first; the SPDX profile is structured and machine-first. An auditor
who must be answered mechanically needs the second. A practitioner deciding whether to use the
model reads the first.

Note the convergence: cards also carry CO2 guidance, and the SPDX AI profile models energy across
six properties. The same concern, one as prose and one as fields.

# Related

- [Datasheets for datasets](datasheets-for-datasets.md) — the counterpart for training data
- [ML-BOM](/bom-types/ml-bom.md) · [SPDX AI and Dataset profiles](/formats/spdx-ai-profile.md)
- [model-signing](/provenance/model-signing.md) — a card says what a model is; a signature says it
  has not changed since

[^mitchell]: [Mitchell et al., *Model Cards for Model Reporting*](https://arxiv.org/abs/1810.03993)
[^hf-model-cards]: [Hugging Face: Model Cards](https://huggingface.co/docs/hub/model-cards)
