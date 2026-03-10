# Waiver: `lp.device.release.execution.schema.json`

This file version-forwards the public device-release execution line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.device.release.execution@0.2.0`
- add `native_summary` and `release_readiness` to execution metadata
- add `latest_native_health_rollup`, `latest_native_incident_id`, `latest_regression_id`, and `latest_regression_status`

Reason:

- the public execution path stays stable by URL, but M1 needs a coherent native-aware execution contract line.
