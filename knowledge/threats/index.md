# How malicious code gets in

The rest of this bundle describes artifacts, names them, and reports what is known to be wrong with
them. These concepts cover the step before all of that: how something hostile enters a dependency
graph in the first place.

* [SLSA supply-chain threat model](slsa-threat-model.md) - The A-H taxonomy, and the threats SLSA v1.0 explicitly does not address.
* [Dependency confusion](dependency-confusion.md) - A public package under an internal name, chosen because its version is higher.
* [Typosquatting](typosquatting.md) - A name a character or two away from a popular one.
* [Maintainer compromise](maintainer-compromise.md) - The legitimate publisher, operated by someone else.
* [Instruction payloads](instruction-payloads.md) - Artifacts whose payload is prose, so code scanners see nothing.

# The common thread

**All three defeat the controls the rest of this bundle documents.** A BOM records the substitution
faithfully; a signature attests the attacker's identity correctly; provenance proves the build was
honest. Inventory, identity and provenance answer *what* and *where from* - never *whether it was
benign*.

The mitigations that work are resolution-side and time-side: scoped namespaces, lockfiles,
[cooldowns](/tools/update-cooldown.md), and consuming `MAL-` malicious-package records rather than
vulnerability advisories alone.
