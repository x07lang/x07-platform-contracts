# Waiver: `lp.device.release.execution.schema.json`

This rollout extends `lp.device.release.execution@0.1.0` in place.

Approved same-version edits:

- add latest metrics snapshot tracking
- add latest SLO evaluation report tracking
- add latest metrics evaluation outcome tracking

Reason:

- device release execution state must expose the closed-loop metrics gate state used by CLI, MCP, and UI surfaces.
