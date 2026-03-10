# Waiver: `lp.regression.run.result.schema.json`

This file version-forwards the public regression run-result line from `@0.1.0` to `@0.2.0` while keeping the stable x07.io schema path and `$id`.

Approved same-path edits:

- change the public contract metadata to `lp.regression.run.result@0.2.0`
- allow both `app regress from-incident` and `device regress from-incident`
- add `replay_target_kind`, `replay_mode`, and `replay_synthesis_status`
- add structured generated native replay artifact refs

Reason:

- the public regression result URL stays stable, but M1 needs explicit native replay reporting semantics on the same path.
