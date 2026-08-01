# Generation

* [syft](syft.md) - Anchore's SBOM generator; images, filesystems, archives → CycloneDX, SPDX or Syft JSON.
* [cdxgen](cdxgen.md) - CycloneDX-native, and the only generator here covering the whole xBOM family.

# Scanning

* [grype](grype.md) - Anchore's scanner; takes an SBOM directly, filters with OpenVEX.
* [trivy](trivy.md) - Broad: vulnerabilities, misconfigurations, secrets and licences across five target types.
* [osv-scanner](osv-scanner.md) - First-party OSV client, with offline mode and guided remediation.

# BOM manipulation

* [cyclonedx-cli](cyclonedx-cli.md) - Convert, merge, diff, validate and sign existing BOMs.

# Standing infrastructure

* [Dependency-Track](dependency-track.md) - Stores BOMs and re-evaluates them as advisories arrive; a service, not a CLI.
* [OpenSSF Scorecard](scorecard.md) - Grades the process that produced the artifacts, not the artifacts.

# Update bots

* [Dependabot](dependabot.md) - GitHub's hosted bot; no infrastructure, GitHub only.
* [Renovate](renovate.md) - Forge-agnostic and self-hostable; the only option on a self-hosted forge.
* [Update cooldown](update-cooldown.md) - The control that makes automated updates net-positive. Not on by default.

# Elsewhere

[cosign](../provenance/cosign.md) is under `provenance/`, with the Sigstore keyless flow that gives
it meaning. [REUSE](../licensing/reuse.md) is under `licensing/`.
