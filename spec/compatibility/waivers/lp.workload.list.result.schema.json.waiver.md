# Waiver: `lp.workload.list.result.schema.json`

This file keeps the stable `@0.1.0` public schema path while widening the workload
list response additively.

Approved same-path edits:

- add desired versus observed state rollups
- add runtime class summaries for API, event, and scheduled workloads
- add optional rollout and readiness fields surfaced by the hosted control plane

Reason:

- workload inventory consumers need the richer hosted state summary without moving
  the published schema endpoint.
