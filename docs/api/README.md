# API

Public self-hosted remote control-plane APIs are defined by schema contracts in `spec/schemas/`.

Key D-OSS response/result schemas:

- `lp.remote.capabilities.response@0.1.0`
- `lp.deploy.push.result@0.1.0`
- `lp.deploy.remote.result@0.1.0`
- `lp.device.release.run.result@0.1.0`
- `lp.device.release.query.result@0.1.0`
- `lp.incident.query.result@0.1.0`
- `lp.regression.run.result@0.1.0`

The canonical endpoint set is implemented by `x07-platform/x07lpd`, but public wire-shape compatibility is governed here.

Key D-OSS request/profile contracts:

- `lp.target.profile@0.1.0` for creator-side remote target configuration
- `lp.device.store.provider.profile@0.1.0` for creator-side device store/provider configuration
- `lp.device.release.plan@0.1.0` for machine-readable device release requests tied to a sealed `x07.device.package.manifest@0.1.0`
- `lp.control.action.result@0.1.0` for deploy and device-release observe/stop/rerun/pause/halt/rollback controls
- `lp.regression.request@0.1.0` for regression generation requests against deploy or device package artifacts

Remote clients are expected to honor the target profile trust settings and OCI registry requirements before calling the self-hosted API surface.
