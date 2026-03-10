# Reason Codes

This directory holds canonical public diagnostic and reason-code references for `lp.*` contracts.

Current D-OSS additions:

- `LP_TARGET_INVALID`
- `LP_TARGET_UNREACHABLE`
- `LP_REMOTE_AUTH_FAILED`
- `LP_REMOTE_CAS_PROBE_FAILED`
- `LP_REMOTE_UPLOAD_FAILED`
- `LP_REMOTE_UPLOAD_DIGEST_MISMATCH`
- `LP_REMOTE_ACCEPT_FAILED`
- `LP_REMOTE_RUN_FAILED`
- `LP_REMOTE_QUERY_FAILED`
- `LP_REMOTE_SECRET_NOT_FOUND`
- `LP_REMOTE_TELEMETRY_EMIT_FAILED`
- `LP_REMOTE_COMPONENT_PUBLISH_FAILED`
- `LP_REMOTE_RUNTIME_DEPLOY_FAILED`
- `LP_REMOTE_ROUTER_BIND_FAILED`
- `LP_REMOTE_ADAPTER_CONFORMANCE_FAILED`
- `LP_REMOTE_CAPABILITIES_UNSUPPORTED`
- `LP_REMOTE_LEASE_CONFLICT`

The runtime repo may emit these codes, but the public contract wording is maintained here.

Native/device additions in the `@0.2.0` contract line reserve the following public diagnostic families:

- `LP_DEVICE_RELEASE_NATIVE_*` for `lp.device.release.*@0.2.0` native-summary and readiness diagnostics
- `LP_DEVICE_RELEASE_READINESS_*` for blocking or warning readiness checks surfaced through `release_readiness`
- `LP_INCIDENT_NATIVE_*` for `lp.incident.*@0.2.0` native-context capture and validation diagnostics
- `LP_REGRESSION_NATIVE_REPLAY_*` for `lp.regression.*@0.2.0` native replay-hint validation and replay synthesis diagnostics

The `native_*` incident values are public classification enums, not reason codes.
