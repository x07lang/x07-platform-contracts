# Waiver: `lp.incident.bundle.schema.json`

This file version-forwards the public incident bundle line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.incident.bundle@0.2.0`
- add `release_plan_id` and `release_exec_id`
- add `native_context`

Reason:

- device-native incidents must stay inside the shared `lp.incident.*` family without changing the published bundle URL.
