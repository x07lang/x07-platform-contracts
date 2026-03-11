# API

Public self-hosted remote control-plane APIs are defined by schema contracts in `spec/schemas/`.

Key D-OSS response/result schemas:

- `lp.remote.capabilities.response@0.1.0`
- `lp.deploy.push.result@0.1.0`
- `lp.deploy.remote.result@0.1.0`
- `lp.device.release.run.result@0.2.0`
- `lp.device.release.query.result@0.2.0`
- `lp.incident.query.result@0.2.0`
- `lp.regression.run.result@0.2.0`

Key hosted response/result schemas:

- `lp.auth.token.response@0.1.0`
- `lp.auth.whoami.result@0.1.0`
- `lp.org.list.result@0.1.0`
- `lp.project.list.result@0.1.0`
- `lp.environment.list.result@0.1.0`
- `lp.secret.list.result@0.1.0`

The canonical endpoint set is implemented by `x07-platform/x07lpd`, but public wire-shape compatibility is governed here.

Key D-OSS request/profile contracts:

- `lp.target.profile@0.1.0` for creator-side remote target configuration
- `lp.device.store.provider.profile@0.1.0` for creator-side device store/provider configuration
- `lp.device.release.plan@0.2.0` for machine-readable device release requests tied to a sealed `x07.device.package.manifest@0.1.0` and its normalized `native_summary`
- `lp.control.action.result@0.1.0` for deploy and device-release observe/stop/rerun/pause/halt/rollback controls
- `lp.regression.request@0.2.0` for regression generation requests against deploy or device package artifacts, including optional `native_replay_hints`

Remote clients are expected to honor the target profile trust settings and OCI registry requirements before calling the self-hosted API surface.

Hosted clients use the shared `lp.auth.*` contracts for browser and device login session bootstrap, then use the hosted list-result contracts to create, list, and select org/project/environment context and inspect hosted secret metadata without introducing a separate public schema family.

Device-release consumers should treat the `@0.2.0` line as the public native-aware contract surface:

- `lp.device.release.*@0.2.0` exposes `native_summary`, `release_readiness`, and the latest native health and regression linkage.
- `lp.incident.*@0.2.0` exposes `release_plan_id` plus sanitized `native_context` under the shared incident system.
- `lp.regression.*@0.2.0` exposes target-aware native replay hints and replay synthesis metadata without requiring a raw event dump.
