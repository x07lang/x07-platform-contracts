# Registry Export

This directory contains the generated platform-schema export used to mirror public `lp.*` schemas into `x07-registry-web/static/spec/`.

Generate it with:

```bash
python3 scripts/export_registry_web_platform_specs.py --schema-dir spec/schemas --out-dir registry/export/spec
```
