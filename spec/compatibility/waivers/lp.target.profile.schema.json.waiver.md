# Waiver: `lp.target.profile.schema.json`

This rollout tightens the existing `lp.target.profile@0.1.0` contract in place.

Approved same-version edits:

- reject non-loopback `http://` `base_url` values
- require `tls.ca_bundle_path` when `tls.mode = "ca_bundle"`
- require `tls.pinned_spki_sha256` when `tls.mode = "pinned_spki"`
- add `oci_auth` and `oci_tls`, and require both when `oci_registry` is set
- require `oci_tls.ca_bundle_path` when `oci_tls.mode = "ca_bundle"`

Reason:

- D-OSS GA hardening needs the published contract to match the production path enforced by `x07lp`.
