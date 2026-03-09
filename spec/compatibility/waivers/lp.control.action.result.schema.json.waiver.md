# Waiver: `lp.control.action.result.schema.json`

This rollout extends `lp.control.action.result@0.1.0` in place.

Approved same-version edits:

- add manual device-release control kinds
- add `scope = "device_release"`
- add `target.release_exec_id`
- add observe, stop, and rerun device-release actions
- allow a device-release state snapshot variant for `state_before` and `state_after`

Reason:

- device-release pause, resume, halt, complete, rollback, observe, stop, and rerun actions must reuse the published control result surface.
