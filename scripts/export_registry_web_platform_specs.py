#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path


def load_schema_id(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    schema_id = data.get("$id")
    if not isinstance(schema_id, str) or not schema_id:
        raise SystemExit(f"missing or invalid $id in {path}")
    return schema_id


def build_export(schema_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for path in sorted(schema_dir.glob("lp*.schema.json")):
        target = out_dir / path.name
        shutil.copy2(path, target)
        entries.append({"id": load_schema_id(path), "path": path.name})
    entries.sort(key=lambda item: item["id"])
    (out_dir / "index.platform.json").write_text(
        json.dumps({"schemas": entries}, indent=2) + "\n",
        encoding="utf-8",
    )


def compare_dirs(expected_dir: Path, actual_dir: Path) -> bool:
    expected = sorted(p.name for p in expected_dir.iterdir() if p.is_file())
    actual = sorted(p.name for p in actual_dir.iterdir() if p.is_file()) if actual_dir.exists() else []
    if expected != actual:
        print("registry export file set drift detected", file=sys.stderr)
        print(f"expected: {expected}", file=sys.stderr)
        print(f"actual:   {actual}", file=sys.stderr)
        return False
    for name in expected:
        if (expected_dir / name).read_text(encoding="utf-8") != (actual_dir / name).read_text(encoding="utf-8"):
            print(f"registry export drift detected: {name}", file=sys.stderr)
            return False
    return True


def build_merged_schema_index(spec_dir: Path) -> str:
    entries = []
    for path in sorted(spec_dir.glob("*.schema.json")):
        entries.append({"id": load_schema_id(path), "path": path.name})
    entries.sort(key=lambda item: item["id"])
    return json.dumps({"schemas": entries}, indent=2) + "\n"


def sync_registry_web(schema_dir: Path, spec_dir: Path) -> None:
    spec_dir.mkdir(parents=True, exist_ok=True)
    source_names = {path.name for path in schema_dir.glob("lp*.schema.json")}
    for existing in spec_dir.glob("lp*.schema.json"):
        if existing.name not in source_names:
            existing.unlink()
    for path in sorted(schema_dir.glob("lp*.schema.json")):
        shutil.copy2(path, spec_dir / path.name)
    (spec_dir / "index.json").write_text(
        build_merged_schema_index(spec_dir),
        encoding="utf-8",
    )


def check_registry_web(schema_dir: Path, spec_dir: Path) -> bool:
    ok = True
    source_files = {path.name: path for path in schema_dir.glob("lp*.schema.json")}
    actual_lp_files = {path.name: path for path in spec_dir.glob("lp*.schema.json")} if spec_dir.exists() else {}
    if sorted(source_files) != sorted(actual_lp_files):
        print("registry-web lp schema file set drift detected", file=sys.stderr)
        print(f"expected: {sorted(source_files)}", file=sys.stderr)
        print(f"actual:   {sorted(actual_lp_files)}", file=sys.stderr)
        ok = False
    for name, source_path in sorted(source_files.items()):
        actual_path = spec_dir / name
        if not actual_path.exists():
            continue
        if source_path.read_text(encoding="utf-8") != actual_path.read_text(encoding="utf-8"):
            print(f"registry-web lp schema drift detected: {name}", file=sys.stderr)
            ok = False
    with tempfile.TemporaryDirectory(prefix="x07-platform-contracts-registry-check-") as tmp:
        tmp_dir = Path(tmp)
        if spec_dir.exists():
            for existing in spec_dir.iterdir():
                if existing.is_file():
                    shutil.copy2(existing, tmp_dir / existing.name)
        sync_registry_web(schema_dir, tmp_dir)
        expected_index = build_merged_schema_index(tmp_dir)
    index_path = spec_dir / "index.json"
    actual_index = index_path.read_text(encoding="utf-8") if index_path.exists() else None
    if expected_index != actual_index:
        print("registry-web schema index drift detected: index.json", file=sys.stderr)
        ok = False
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema-dir", default="spec/schemas")
    parser.add_argument("--out-dir", default="dist/registry-web/spec")
    parser.add_argument(
        "--registry-web-spec-dir",
        default=None,
        help="Optional x07-registry-web static/spec directory to sync in place.",
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    schema_dir = Path(args.schema_dir)
    out_dir = Path(args.out_dir)
    registry_web_spec_dir = Path(args.registry_web_spec_dir) if args.registry_web_spec_dir else None

    if registry_web_spec_dir is not None:
        if args.check:
            ok = check_registry_web(schema_dir, registry_web_spec_dir)
            if ok:
                print("ok: registry-web platform schema mirror")
                return 0
            print(
                "run: python3 scripts/export_registry_web_platform_specs.py "
                f"--schema-dir {schema_dir} --registry-web-spec-dir {registry_web_spec_dir}",
                file=sys.stderr,
            )
            return 1
        sync_registry_web(schema_dir, registry_web_spec_dir)
        print(f"wrote: {registry_web_spec_dir}")
        return 0

    with tempfile.TemporaryDirectory(prefix="x07-platform-contracts-export-") as tmp:
        tmp_dir = Path(tmp)
        build_export(schema_dir, tmp_dir)
        if args.check:
            ok = compare_dirs(tmp_dir, out_dir)
            if ok:
                print("ok: contracts registry export")
                return 0
            print("run: python3 scripts/export_registry_web_platform_specs.py", file=sys.stderr)
            return 1
        if out_dir.exists():
            shutil.rmtree(out_dir)
        shutil.copytree(tmp_dir, out_dir)
        print(f"wrote: {out_dir}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
