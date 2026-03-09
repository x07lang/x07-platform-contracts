# Contracts

Authoritative public platform schemas live under `spec/schemas/` and are indexed by `spec/schemas/index.json`.

Current public contract groups:

- core lifecycle: `lp.change_request@0.1.0`, `lp.pipeline.run@0.1.0`, `lp.decision.record@0.1.0`
- deploy execution: `lp.deploy.execution@0.1.0`, `lp.deploy.execution.meta.local@0.1.0`, `lp.deploy.execution.meta.remote@0.1.0`, `lp.deploy.query.result@0.1.0`, `lp.deploy.push.result@0.1.0`, `lp.deploy.remote.result@0.1.0`
- device release: `lp.device.store.provider.profile@0.1.0`, `lp.device.release.plan@0.1.0`, `lp.device.release.execution@0.1.0`, `lp.device.release.query.result@0.1.0`, `lp.device.release.run.result@0.1.0`
- remote streams: `lp.remote.events.result@0.1.0`, `lp.remote.logs.result@0.1.0`
- incidents and regressions: `lp.incident.bundle@0.1.0`, `lp.incident.bundle.meta.local@0.1.0`, `lp.incident.bundle.meta.remote@0.1.0`, `lp.incident.query.result@0.1.0`, `lp.regression.request@0.1.0`, `lp.regression.run.result@0.1.0`
- target and adapter contracts: `lp.target.profile@0.1.0`, `lp.target.list.result@0.1.0`, `lp.remote.capabilities.response@0.1.0`, `lp.adapter.capabilities@0.1.0`, `lp.adapter.conformance.report@0.1.0`
- CLI and control: `lp.cli.report@0.1.0`, `lp.control.action.result@0.1.0`, `lp.app.list.result@0.1.0`
- shared hosted-facing public contracts reserved for later layers: `lp.auth.*`, `lp.metering.event@0.1.0`

Notes:

- `lp.deploy.execution@0.1.0` executes `x07.deploy.plan@0.2.0`.
- `lp.device.release.plan@0.1.0` references `lp.device.store.provider.profile@0.1.0` and sealed `x07.device.package.manifest@0.1.0` inputs.
- `lp.device.release.plan@0.1.0` now includes a first-class `metrics.eval` step that references a sealed `x07.slo.profile@0.1.0` threshold artifact instead of embedding raw metrics.
- `lp.device.release.execution@0.1.0` and `lp.device.release.query.result@0.1.0` capture the provider-neutral release trail plus the latest metrics snapshot, SLO evaluation outcome, and linked incidents used by CLI, MCP, and UI surfaces.
- `lp.incident.bundle.meta.local@0.1.0` and `lp.incident.query.result@0.1.0` can describe either deploy-linked incidents or device-release-linked incidents without minting a second incident system.
- D-OSS remote deploy v1 accepts `x07.app.pack@0.1.0` only.
- `lp.target.profile@0.1.0` now defines the hardened self-hosted remote path:
  - `base_url` must be `https://...` unless it targets loopback `http://127.0.0.1` or `http://localhost`
  - `tls.mode = "ca_bundle"` requires `tls.ca_bundle_path`
  - `tls.mode = "pinned_spki"` requires `tls.pinned_spki_sha256`
  - `oci_registry` requires `oci_auth` and `oci_tls`
- `lp.remote.capabilities.response@0.1.0` includes `features.authenticated_oci_push` and `features.registry_tls` so clients can preflight the registry path before deploy.
- `lp.deploy.execution.meta.remote@0.1.0` preserves the target TLS and OCI trust/auth references carried by the accepted target profile so remote query artifacts stay self-describing.
- Public schemas, examples, and reason codes must not expose internal milestone naming.
