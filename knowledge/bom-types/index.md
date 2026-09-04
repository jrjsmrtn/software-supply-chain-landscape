# The xBOM family

A bill of materials is an inventory of what a thing is made of. The variants differ in what "thing"
means — and, less obviously, in whether they describe an *artifact*, a *deployment*, or a *process*.

* [SBOM](sbom.md) - Software components, services, and the dependency relationships between them.
* [HBOM](hbom.md) - Physical hardware components **and their firmware**, for embedded and connected devices.
* [OBOM](obom.md) - Full-stack inventory of a runtime environment: OS, hardware, configuration, dependencies.
* [SaaSBOM](saasbom.md) - Services, endpoints, data flows and their classifications.
* [CBOM](cbom.md) - Cryptographic assets and where each is used.
* [ML-BOM](ml-bom.md) - Datasets, models and configurations, with dataset provenance.
* [MBOM](mbom.md) - Declared and observed production formulations and workflows.

# What each one describes

| | Describes | Goes stale when |
|---|---|---|
| SBOM, HBOM, CBOM, ML-BOM | an **artifact** | the artifact is rebuilt |
| OBOM, SaaSBOM | a **deployment** | the next deploy |
| MBOM | a **process** | the process changes |

That split matters more than the subject matter. A deployment-scoped BOM is short-lived by
construction and environment-specific; treating it like a released artifact's SBOM produces
documents that are confidently wrong.

Why the family exists at all, and CBOM's post-quantum deadline, are durable rationale and live in
[the landscape explanation](/landscape.md#the-xbom-family--whats-in-the-box).

# A separate axis: where the data came from

This page classifies by **what is inventoried**. It says nothing about **how the inventory was
produced** — and that is an independent question with its own answer, the six SBOM types (Design,
Source, Build, Analyzed, Deployed, Runtime): see [the six SBOM types](/formats/sbom-types.md).

Knowing a document is an SBOM does not tell you whether its contents were read off the source tree,
emitted by the build, or inferred from a finished binary, and those differ in what they can be
trusted to have seen. Two SBOMs of one artifact can disagree without either being wrong. The
CISA document is scoped to SBOMs; it does not extend the six types to the other members of the
family above.
