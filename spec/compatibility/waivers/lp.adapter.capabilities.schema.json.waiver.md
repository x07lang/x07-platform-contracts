# Waiver: `lp.adapter.capabilities.schema.json`

This rollout extends `lp.adapter.capabilities@0.1.0` in place.

Approved same-version edits:

- add the optional `device_release` capability block
- expose supported device targets, lanes, operations, and manual-control support flags

Reason:

- the device-release control surface needs a stable provider capability summary without minting a parallel adapter contract.
