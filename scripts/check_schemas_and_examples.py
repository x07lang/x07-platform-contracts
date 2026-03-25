#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def schema_name_from_example_filename(filename: str) -> str:
    if ".example" not in filename or not filename.endswith(".json"):
        raise ValueError(f"not an example json file: {filename}")
    return filename.split(".example", 1)[0]


def iter_schema_files(schema_dir: Path) -> list[Path]:
    return sorted(schema_dir.glob("*.schema.json"))


def iter_example_files(example_dir: Path) -> list[Path]:
    return sorted(example_dir.glob("*.example*.json"))


def main() -> int:
    try:
        import jsonschema
    except Exception as e:  # pragma: no cover
        print(f"error: missing python dependency 'jsonschema': {e}", file=sys.stderr)
        print("hint: python3 -m pip install jsonschema", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    schema_dir = root / "spec" / "schemas"
    example_dir = root / "spec" / "examples"

    failures: list[str] = []

    # Validate all schemas.
    for schema_path in iter_schema_files(schema_dir):
        schema = load_json(schema_path)
        validator_cls = jsonschema.validators.validator_for(schema)
        try:
            validator_cls.check_schema(schema)
        except Exception as e:
            failures.append(f"invalid schema {schema_path}: {e}")

    # Validate all examples against their schema.
    for example_path in iter_example_files(example_dir):
        schema_name = schema_name_from_example_filename(example_path.name)
        schema_path = schema_dir / f"{schema_name}.schema.json"
        if not schema_path.exists():
            failures.append(
                f"example {example_path} has no matching schema {schema_path}"
            )
            continue

        schema = load_json(schema_path)
        instance = load_json(example_path)
        validator_cls = jsonschema.validators.validator_for(schema)
        validator = validator_cls(schema)
        errors = sorted(validator.iter_errors(instance), key=str)
        if errors:
            for err in errors[:20]:
                failures.append(f"example {example_path} invalid: {err.message}")
            if len(errors) > 20:
                failures.append(
                    f"example {example_path} invalid: ... {len(errors) - 20} more"
                )

    if failures:
        for msg in failures:
            print(f"error: {msg}", file=sys.stderr)
        return 1

    print("ok: schemas and examples validate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
