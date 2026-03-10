# Waiver: `lp.device.release.query.result.schema.json`

This file version-forwards the public device-release query line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.device.release.query.result@0.2.0`
- add `native_summary` and `release_readiness`
- add `latest_native_health_rollup`, `latest_native_incident_id`, `latest_regression_id`, and `latest_regression_status`
- tighten linked incident classifications to the native-aware public taxonomy

Reason:

- query consumers need the M1 native release state without moving the published schema URL.
