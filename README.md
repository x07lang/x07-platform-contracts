# x07-platform-contracts

`x07-platform-contracts` is the source of truth for public X07 Platform contracts.

Contents:

- public `lp.*` JSON Schemas under `spec/schemas/`
- schema index generation and compatibility checks under `scripts/`
- contract docs and reason-code references under `docs/`
- registry export helpers under `registry/export/`

D-OSS public additions include:

- target profiles and listing contracts
- remote upload and remote deploy result contracts
- remote execution and incident companion metadata
- remote event and log stream contracts
- remote capabilities and adapter conformance contracts
- device release orchestration, observability, and control contracts

Rules:

- Public stable `lp.*` schemas are authored here, not in `x07-platform` or `x07-platform-cloud`.
- `x07-platform` and `x07-platform-cloud` consume these contracts.
- Hosted-only private schemas belong in `lpcloud.*`, not `lp.*`.
- Device release metrics gates, incident linkage, and observe/stop/rerun controls stay in `lp.*`; device package and host-facing artifacts stay in `x07.device.*`.

Developer commands:

- Generate schema index: `./scripts/gen_schema_index.sh`
- Check schema index drift: `./scripts/gen_schema_index.sh --check`
- Check same-version schema edits/removals: `./scripts/check_compat.sh`
- Build registry export bundle: `python3 scripts/export_registry_web_platform_specs.py --schema-dir spec/schemas --out-dir registry/export/spec`
- Sync the x07.io schema mirror: `python3 scripts/export_registry_web_platform_specs.py --schema-dir spec/schemas --registry-web-spec-dir ../x07-registry-web/static/spec`
