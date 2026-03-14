# Waiver: `lp.incident.bundle.schema.json`

This file version-forwards the public incident bundle line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.incident.bundle@0.2.0`
- add `release_plan_id` and `release_exec_id`
- add `native_context`
- add normalized top-level bundle provenance fields: `native_classification`, `provider_kind`, `target_kind`, and `package_manifest_sha256`
- allow native-context package manifests to use prefixed `sha256:` digests and keep nullable lifecycle/connectivity snapshots from device-host captures

Reason:

- device-native incidents must stay inside the shared `lp.incident.*` family, including package provenance emitted by device-host captures, without changing the published bundle URL.
