# Waiver: `lp.pipeline.run.schema.json`

This rollout extends `lp.pipeline.run@0.1.0` in place.

Approved same-version edits:

- accept `x07.device.package.manifest@0.1.0` as a pipeline input artifact
- add device-release step kinds for validation, execution, control, and provider calls

Reason:

- device releases must appear in the same pipeline run and decision trail used by the existing platform flow.
