# Waiver: `lp.release.query.result.schema.json`

This file keeps the stable `@0.1.0` public schema path while widening the release
query response additively.

Approved same-path edits:

- add `state_version`
- add release state fields needed by durable review and rollout workflows without
  removing existing properties

Reason:

- hosted release queries need optimistic state tracking and richer public status
  reporting through the existing schema URL.
