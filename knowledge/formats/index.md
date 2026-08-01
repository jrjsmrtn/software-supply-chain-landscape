# BOM interchange formats

* [CycloneDX](cyclonedx.md) - OWASP's security-first format; the whole xBOM family in one schema, with native VEX.
* [SPDX](spdx.md) - The Linux Foundation format, grown out of license compliance; ISO/IEC 5962.

# Document practices

* [Declaring BOM completeness (`compositions`)](bom-completeness.md) - Saying a BOM is partial, so its silence is not read as assurance.
* [Merging BOMs](bom-merging.md) - Flat versus hierarchical, and why linking is usually better.

VEX interchange formats (OpenVEX, CSAF VEX) are **not** here. They are inseparable from the VEX
state vocabularies and migrate with `intelligence/`.
