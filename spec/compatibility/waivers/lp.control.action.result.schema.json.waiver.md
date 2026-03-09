# Waiver: `lp.control.action.result.schema.json`

This rollout extends `lp.control.action.result@0.1.0` in place.

Approved same-version edits:

- add manual device-release control kinds
- add `scope = "device_release"`
- add `target.release_exec_id`

Reason:

- device-release pause, resume, halt, complete, and rollback actions must reuse the published control result surface.
