# Waiver: `lp.binding.status.result.schema.json`

This file keeps the stable `@0.1.0` public schema path while widening the binding
status response shape additively.

Approved same-path edits:

- add binding health details for connector-backed readiness and probe results
- add optional live diagnostics fields that preserve existing consumers

Reason:

- hosted binding health now exposes durable probe output through the existing public
  result contract without forcing a path change.
