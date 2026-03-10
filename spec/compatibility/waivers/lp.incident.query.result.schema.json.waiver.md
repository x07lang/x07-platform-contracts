# Waiver: `lp.incident.query.result.schema.json`

This file version-forwards the public incident query line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.incident.query.result@0.2.0`
- add `release_plan_id`
- add `native_context`
- replace the legacy device-native classifications with the M1 `native_*` taxonomy
- update nested device-release refs to the native-aware shape

Reason:

- incident query consumers need the unified M1 incident model without moving off the published `lp.incident.query.result` URL.
