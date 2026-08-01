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
