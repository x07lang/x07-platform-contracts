# Waiver: `lp.workload.describe.result.schema.json`

This file keeps the stable `@0.1.0` public schema path while widening the workload
describe response additively.

Approved same-path edits:

- add desired versus observed state summaries
- add runtime cell metadata for API, event, and scheduled workloads
- add rollout, autoscaling, and binding probe details used by hosted control-plane
  queries

Reason:

- workload inspection now reflects reconciled runtime state through the established
  public schema URL.
