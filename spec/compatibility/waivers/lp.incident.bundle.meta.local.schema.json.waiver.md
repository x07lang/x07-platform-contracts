# Waiver: `lp.incident.bundle.meta.local.schema.json`

This file version-forwards the public local incident-meta line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.incident.bundle.meta.local@0.2.0`
- replace the legacy device-native classifications with the M1 `native_*` taxonomy
- add `release_plan_id`
- add `native_context`
- update the nested device-release shape to expose `target_kind` and `package_manifest_sha256`

Reason:

- local incident metadata must stay on the shared published path while the M1 device-native incident model lands.
