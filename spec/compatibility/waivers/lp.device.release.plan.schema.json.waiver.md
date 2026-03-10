# Waiver: `lp.device.release.plan.schema.json`

This file version-forwards the public device-release plan line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.device.release.plan@0.2.0`
- add `native_summary`
- add `release_readiness`

Reason:

- compatibility checks key off stable schema paths in this repo, so a real contract-line forward still needs a same-path waiver.
