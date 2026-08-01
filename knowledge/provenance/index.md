# Signing

* [Sigstore](sigstore.md) - Keyless signing: short-lived certificates bound to an OIDC identity, logged publicly.
* [cosign](cosign.md) - The Sigstore client, and why verification without an expected identity proves nothing.
* [model-signing (OMS)](model-signing.md) - Signs a directory tree by hashing every component into a manifest. Not only for models.

# Provenance and attestation

* [SLSA](slsa.md) - Graded requirements for build provenance. Grades the process, not the code.
* [in-toto](in-toto.md) - Layout, link metadata, and the attestation envelope SLSA provenance travels inside.

The three are a stack rather than alternatives: SLSA says what to record, in-toto says how to wrap
it, Sigstore says how to sign it.
