# Contracts

Authoritative public platform schemas live under `spec/schemas/` and are indexed by `spec/schemas/index.json`.

Current public contract groups:

- core lifecycle: `lp.change_request@0.1.0`, `lp.pipeline.run@0.1.0`, `lp.decision.record@0.1.0`
- deploy execution: `lp.deploy.execution@0.1.0`, `lp.deploy.execution.meta.local@0.1.0`, `lp.deploy.execution.meta.remote@0.1.0`, `lp.deploy.query.result@0.1.0`, `lp.deploy.push.result@0.1.0`, `lp.deploy.remote.result@0.1.0`
- device release: `lp.device.store.provider.profile@0.1.0`, `lp.device.release.plan@0.2.0`, `lp.device.release.execution@0.2.0`, `lp.device.release.query.result@0.2.0`, `lp.device.release.run.result@0.2.0`
- remote streams: `lp.remote.events.result@0.1.0`, `lp.remote.logs.result@0.1.0`
- incidents and regressions: `lp.incident.bundle@0.2.0`, `lp.incident.bundle.meta.local@0.2.0`, `lp.incident.bundle.meta.remote@0.2.0`, `lp.incident.query.result@0.2.0`, `lp.regression.request@0.2.0`, `lp.regression.run.result@0.2.0`
- target and adapter contracts: `lp.target.profile@0.1.0`, `lp.target.list.result@0.1.0`, `lp.remote.capabilities.response@0.1.0`, `lp.adapter.capabilities@0.1.0`, `lp.adapter.conformance.report@0.1.0`
- workload delivery draft set: `lp.workload.describe.result@0.1.0`, `lp.workload.list.result@0.1.0`, `lp.workload.pack.manifest@0.1.0`, `lp.topology.preview.result@0.1.0`, `lp.binding.requirements.result@0.1.0`, `lp.binding.status.result@0.1.0`, `lp.scale.profile@0.1.0`, `lp.release.submit.request@0.1.0`, `lp.release.query.result@0.1.0`, `lp.release.evidence.bundle@0.1.0`, `lp.release.decision.record@0.1.0`
- CLI and control: `lp.cli.report@0.1.0`, `lp.control.action.result@0.1.0`, `lp.app.list.result@0.1.0`
- shared hosted-facing public contracts: `lp.auth.*`, `lp.org.list.result@0.1.0`, `lp.project.list.result@0.1.0`, `lp.environment.list.result@0.1.0`, `lp.hosted.entitlements.result@0.1.0`, `lp.usage.summary.result@0.1.0`, `lp.secret.list.result@0.1.0`, `lp.metering.event@0.1.0`

Notes:

- `lp.deploy.execution@0.1.0` executes `x07.deploy.plan@0.2.0`.
- `lp.device.release.plan@0.2.0` references `lp.device.store.provider.profile@0.1.0`, sealed `x07.device.package.manifest@0.1.0` inputs, and freezes the package-derived `native_summary` plus machine-readable `release_readiness`.
- `lp.device.release.plan@0.2.0` keeps the first-class `metrics.eval` step that references a sealed `x07.slo.profile@0.1.0` threshold artifact instead of embedding raw metrics.
- `lp.device.release.execution@0.2.0` and `lp.device.release.query.result@0.2.0` capture the provider-neutral release trail plus the latest metrics snapshot, native health rollup, latest native incident linkage, and latest regression linkage used by CLI, MCP, and UI surfaces.
- `lp.incident.*@0.2.0` keeps device incidents inside the shared incident family, adds sanitized `native_context`, and uses the stable native classification set `native_runtime_error`, `native_policy_violation`, `native_bridge_timeout`, `native_host_crash`, and `native_permission_blocked`.
- `lp.regression.*@0.2.0` keeps incident-driven regression generation generic while adding `native_replay_hints`, replay target metadata, and structured generated native replay artifact refs.
- Runtime permission state belongs in `lp.incident.*@0.2.0` via `native_context`, not in `lp.device.release.*@0.2.0` release metadata.
- D-OSS remote deploy v1 accepts `x07.app.pack@0.1.0` only.
- The workload/topology/binding/release set is draft and experimental. It freezes public naming and wire shape for service-oriented backend delivery without claiming that every downstream runtime path is GA-stable yet.
- `lp.target.profile@0.1.0` now keeps the hardened self-hosted remote path under `kind = "oss_remote"` and adds additive `kind = "hosted" | "k8s" | "wasmcloud"` hints over the same authenticated creator-side profile shape.
- `lp.target.profile@0.1.0` now defines the hardened self-hosted remote path:
  - `base_url` must be `https://...` unless it targets loopback `http://127.0.0.1` or `http://localhost`
  - `tls.mode = "ca_bundle"` requires `tls.ca_bundle_path`
  - `tls.mode = "pinned_spki"` requires `tls.pinned_spki_sha256`
  - `oci_registry` requires `oci_auth` and `oci_tls`
- `lp.remote.capabilities.response@0.1.0` includes `features.authenticated_oci_push` and `features.registry_tls` so clients can preflight the registry path before deploy.
- `lp.deploy.execution.meta.remote@0.1.0` preserves the target TLS and OCI trust/auth references carried by the accepted target profile so remote query artifacts stay self-describing.
- `lp.org.list.result@0.1.0`, `lp.project.list.result@0.1.0`, and `lp.environment.list.result@0.1.0` provide the shared hosted context tables used by `x07lp` and hosted console onboarding.
- `lp.hosted.entitlements.result@0.1.0` exposes the hosted plan, quota limits, capability flags, and current deployment or SQLite usage for the selected context.
- `lp.usage.summary.result@0.1.0` exposes the hosted usage window totals materialized from `lp.metering.event@0.1.0` plus the current deployment and SQLite counts used by quota enforcement.
- `lp.secret.list.result@0.1.0` provides the shared hosted secret inventory table used by `x07lp` and hosted console metadata views without exposing secret values.
- Public schemas, examples, and reason codes must not expose internal milestone naming.
