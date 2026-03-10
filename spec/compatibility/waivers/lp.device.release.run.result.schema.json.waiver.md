# Waiver: `lp.device.release.run.result.schema.json`

This file version-forwards the public device-release run result line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.device.release.run.result@0.2.0`
- add `native_summary` and `release_readiness`
- add the latest native incident, regression, and native health linkage fields
- retarget the embedded execution ref to `lp.device.release.execution@0.2.0`

Reason:

- the CLI result surface must stay on the same published path while the public device-release contract line moves forward.
