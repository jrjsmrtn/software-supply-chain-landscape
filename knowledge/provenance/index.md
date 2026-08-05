# Signing

* [Sigstore](sigstore.md) - Keyless signing: short-lived certificates bound to an OIDC identity, logged publicly.
* [cosign](cosign.md) - The Sigstore client, and why verification without an expected identity proves nothing.
* [model-signing (OMS)](model-signing.md) - Signs a directory tree by hashing every component into a manifest. Not only for models.

# Provenance and attestation

* [Developer Certificate of Origin (DCO)](dco.md) - A contributor's self-certification of the right to submit. Asserts the right, never authorship — and its text may not be modified.
* [Contributor License Agreement (CLA)](cla.md) - A signed contract granting the steward copyright and patent licences. Its employer clause, not its licence grant, is what blocks contributors.
* [SLSA](slsa.md) - Graded requirements for build provenance. Grades the process, not the code.
* [in-toto](in-toto.md) - Layout, link metadata, and the attestation envelope SLSA provenance travels inside.

The three are a stack rather than alternatives: SLSA says what to record, in-toto says how to wrap
it, Sigstore says how to sign it.

The DCO sits outside that stack: it records a **human claim** about the right to submit, where the
others produce machine-checkable evidence about how an artifact was built. Nothing verifies a
sign-off; its value is that the claim is attributable and on the record.
