# Waiver: `lp.remote.capabilities.response.schema.json`

This rollout extends `lp.remote.capabilities.response@0.1.0` in place.

Approved same-version edits:

- add `features.authenticated_oci_push`
- add `features.registry_tls`

Reason:

- D-OSS GA hardening needs a stable preflight surface for authenticated OCI publish and registry trust.
