# x07-platform-contracts

Source-of-truth repo for the public `lp.*` contracts used by X07 Platform.

If `x07-platform` is the runtime and control plane, this repo is the public language those tools speak. It keeps the schema layer explicit so the CLI, UI, MCP tools, and downstream consumers can all operate on the same data model.

**Start here:** [`spec/schemas/`](spec/schemas/) · [`docs/`](docs/) · [`x07lang/x07-platform`](https://github.com/x07lang/x07-platform)

## What Lives Here

- public `lp.*` JSON Schemas
- schema indexing and compatibility checks
- contract docs and reason-code references
- export helpers for downstream schema mirrors

## When To Use It

Use `x07-platform-contracts` when you need to:

- add or review a public platform schema
- validate compatibility for a same-version schema change
- export the public schema slice into downstream repos
- understand the stable contract layer without reading runtime implementation code

Most end users will feel this repo indirectly through `x07-platform`, `x07lang-mcp`, and `x07.io`.

## Quick Start

Generate and check the schema index:

```sh
./scripts/gen_schema_index.sh
./scripts/gen_schema_index.sh --check
./scripts/check_compat.sh
```

Export the schema bundle:

```sh
python3 scripts/export_registry_web_platform_specs.py \
  --schema-dir spec/schemas \
  --out-dir registry/export/spec
```

## Boundary Rules

- public stable `lp.*` schemas are authored here
- runtimes and hosted systems consume these contracts
- hosted-only private schemas belong in `lpcloud.*`, not `lp.*`

## How It Fits The X07 Ecosystem

- [`x07-platform`](https://github.com/x07lang/x07-platform) executes lifecycle workflows using these contracts
- [`x07-registry-web`](https://github.com/x07lang/x07-registry-web) mirrors part of the public schema slice
- [`x07`](https://github.com/x07lang/x07) and related tooling consume the contract layer where platform-facing workflows need it
