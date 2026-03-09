# Waiver: `lp.incident.query.result.schema.json`

This rollout extends `lp.incident.query.result@0.1.0` in place.

Approved same-version edits:

- add device-release resolution by `release_exec_id`
- allow device-release-linked incident items alongside deploy-linked incidents
- add device incident classifications and sources

Reason:

- device release automation must reuse the published incident query contract instead of creating a second incident API.
