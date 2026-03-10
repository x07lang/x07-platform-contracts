# Waiver: `lp.incident.bundle.meta.remote.schema.json`

This file version-forwards the public remote incident-meta line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.incident.bundle.meta.remote@0.2.0`
- add release linkage fields for device-native incidents
- add `native_context`
- add the nested device-release summary
- extend the classification set with the M1 `native_*` taxonomy

Reason:

- D-OSS mirrors need the same incident contract line as local consumers without minting a second remote-only native incident family.
