# Waiver: `lp.device.release.plan.schema.json`

This rollout extends `lp.device.release.plan@0.1.0` in place.

Approved same-version edits:

- add the `metrics.eval` step kind
- require `window_seconds`, `thresholds`, and `on_fail` for `metrics.eval`
- allow release-oriented `on_fail` values on public device-release steps

Reason:

- device release observability must reuse the published release-plan contract instead of creating a second control document.
