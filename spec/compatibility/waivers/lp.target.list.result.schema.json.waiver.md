# Waiver: `lp.target.list.result.schema.json`

This file keeps the stable `@0.1.0` public schema path while widening the target
inventory response additively.

Approved same-path edits:

- add optional target health and deployment summary fields
- add durable inventory metadata used by hosted target management

Reason:

- hosted target inventory needs richer summaries without breaking existing clients
  or changing the published schema path.
