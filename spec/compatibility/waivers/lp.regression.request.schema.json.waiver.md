# Waiver: `lp.regression.request.schema.json`

This file version-forwards the public regression request line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.regression.request@0.2.0`
- retarget incident refs to `lp.incident.bundle@0.2.0`
- add `replay_target_kind`
- add `native_replay_hints`

Reason:

- device-native incidents must flow through the shared regression request contract without changing the published schema URL.
