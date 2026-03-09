# API

Public self-hosted remote control-plane APIs are defined by schema contracts in `spec/schemas/`.

Key D-OSS response/result schemas:

- `lp.remote.capabilities.response@0.1.0`
- `lp.deploy.push.result@0.1.0`
- `lp.deploy.remote.result@0.1.0`
- `lp.incident.query.result@0.1.0`
- `lp.regression.run.result@0.1.0`

The canonical endpoint set is implemented by `x07-platform/x07lpd`, but public wire-shape compatibility is governed here.

Key D-OSS request/profile contracts:

- `lp.target.profile@0.1.0` for creator-side remote target configuration

Remote clients are expected to honor the target profile trust settings and OCI registry requirements before calling the self-hosted API surface.
