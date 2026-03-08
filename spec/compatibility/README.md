# Compatibility

Compatibility checks are waiver-based:

- new schemas may be added without a waiver
- removing a public schema requires `_removed_<schema>.waiver.md`
- editing a same-version schema requires `<schema>.waiver.md`

Run `./scripts/check_compat.sh` to enforce this policy.

