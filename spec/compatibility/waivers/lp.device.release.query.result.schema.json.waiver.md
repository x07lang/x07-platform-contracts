# Waiver: `lp.device.release.query.result.schema.json`

This rollout extends `lp.device.release.query.result@0.1.0` in place.

Approved same-version edits:

- add latest metrics snapshot and latest SLO evaluation report fields
- add latest metrics evaluation outcome field
- add linked incident summaries to the query result

Reason:

- device release query responses must show the current metrics gate state and linked incidents without inventing a second query contract.
