# Waiver: `lp.deploy.execution.meta.remote.schema.json`

This branch already extends `lp.deploy.execution.meta.remote@0.1.0` in place.

Approved same-version edits:

- remove internal milestone wording from the public description
- add remote target TLS metadata
- add OCI auth and OCI TLS metadata
- add `lattice_id`
- add `telemetry_collector_hint`

Reason:

- the published remote execution companion schema must match the hardened remote deploy metadata carried by the platform.
