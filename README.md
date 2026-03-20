# x07-platform-contracts

`x07-platform-contracts` is the source-of-truth repo for the public contracts used by `x07-platform`.

If `x07-platform` is the control plane that runs deployments and device releases, this repo is the public language those tools speak. It defines the `lp.*` schemas, indexes, and reason-code references that let the CLI, UI, MCP tools, and future hosted surfaces agree on the same data.

## What Is In This Repo

- **Public `lp.*` JSON Schemas** under `spec/schemas/`
- **Schema indexing and compatibility checks** under `scripts/`
- **Contract docs and reason-code references** under `docs/`
- **Registry export helpers** under `registry/export/`

## Vision

The vision is to keep platform operations boring and predictable.

An end user should be able to move between local demos, self-hosted targets, and hosted surfaces without learning a different contract each time. A coding agent should be able to consume platform state as stable JSON instead of reverse-engineering ad hoc CLI text or UI payloads.

That is why public platform contracts live here instead of being scattered across runtime repos.

## How It Fits The X07 Ecosystem

- [`x07`](https://github.com/x07lang/x07) is the core language and toolchain
- [`x07-wasm-backend`](https://github.com/x07lang/x07-wasm-backend) produces the app and device artifacts that the platform manages
- [`x07-platform`](https://github.com/x07lang/x07-platform) executes lifecycle workflows against those artifacts
- [`x07-registry-web`](https://github.com/x07lang/x07-registry-web) mirrors the public schema slice so the same contracts are visible on `x07.io`

This repo exists so the platform contract layer stays explicit and reusable across all of those surfaces.

The current draft expansion adds workload state, topology, binding probe, target health, and release control contracts for service-oriented backend delivery. Those lines stay public as `lp.*`, while hosted-only review, queue, provenance, and approval records remain private `lpcloud.*` surfaces outside this repo.

## Practical Usage

Use this repo when you need to:

- validate or review a public `lp.*` contract
- add a new platform result, event, or control schema
- check that a same-version schema edit is compatible
- export the public platform schema slice into downstream repos

Most end users will not work here directly. They will feel its effect through stable platform behavior in `x07-platform`, `x07lang-mcp`, and `x07.io`.

## Standalone Workflow

From the repo root:

```sh
./scripts/gen_schema_index.sh
./scripts/gen_schema_index.sh --check
./scripts/check_compat.sh
```

Build the registry export bundle:

```sh
python3 scripts/export_registry_web_platform_specs.py \
  --schema-dir spec/schemas \
  --out-dir registry/export/spec
```

Sync the `x07.io` mirror in a sibling checkout:

```sh
python3 scripts/export_registry_web_platform_specs.py \
  --schema-dir spec/schemas \
  --registry-web-spec-dir ../x07-registry-web/static/spec
```

## Repo Rules

- Public stable `lp.*` schemas are authored here, not in `x07-platform` or `x07-platform-cloud`
- `x07-platform` and `x07-platform-cloud` consume these contracts
- Hosted-only private schemas belong in `lpcloud.*`, not `lp.*`
- Device release metrics gates, incident linkage, and observe/stop/rerun controls stay in `lp.*`
- Device package and host-facing artifacts stay in `x07.device.*`

## Contract Coverage

D-OSS public additions include:

- target profiles and listing contracts
- remote upload and remote deploy result contracts
- remote execution and incident companion metadata
- remote event and log stream contracts
- remote capabilities and adapter conformance contracts
- device release orchestration, observability, and control contracts

Hosted public additions include:

- session and token exchange contracts for `x07lp` hosted login
- organization, project, and environment listing contracts for hosted context selection
- secret inventory contracts for hosted console and CLI metadata views
- entitlement and usage summary contracts for hosted quota and usage APIs
- workload, topology, target, binding, and release contracts for service-oriented backend delivery (`lp.workload.*`, `lp.topology.*`, `lp.target.*`, `lp.binding.*`, `lp.release.*`)

Recent additive public coverage includes:

- desired and observed workload state summaries for reconciler-driven control surfaces
- provider-neutral target health and binding probe results
- release gate request and decision contracts plus rollback execution results
