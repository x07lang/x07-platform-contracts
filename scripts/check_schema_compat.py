#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def try_sh(*args: str) -> str | None:
    try:
        return sh(*args)
    except subprocess.CalledProcessError:
        return None


def resolve_base() -> str | None:
    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        remote_ref = f"origin/{base_ref}"
        if try_sh("git", "rev-parse", "--verify", remote_ref):
            return sh("git", "merge-base", "HEAD", remote_ref)
    if try_sh("git", "rev-parse", "--verify", "HEAD^"):
        return sh("git", "rev-parse", "HEAD^")
    return None


def schema_id_from_text(text: str) -> str | None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    value = data.get("$id")
    return value if isinstance(value, str) else None


def main() -> int:
    base = resolve_base()
    if not base:
        print("compatibility: no base revision found; skipping")
        return 0

    diff = sh("git", "diff", "--name-status", "--no-renames", f"{base}...HEAD", "--", "spec/schemas")
    lines = [line for line in diff.splitlines() if line.strip()]
    failures: list[str] = []
    waiver_dir = Path("spec/compatibility/waivers")

    for line in lines:
        status, path = line.split("\t", 1)
        if not path.endswith(".schema.json"):
            continue
        basename = Path(path).name
        waiver = waiver_dir / f"{basename}.waiver.md"
        remove_waiver = waiver_dir / f"_removed_{basename}.waiver.md"

        if status == "A":
            continue
        if status == "D":
            if not remove_waiver.exists():
                failures.append(f"removed public schema without waiver: {basename} (expected {remove_waiver})")
            continue
        if status != "M":
            continue

        old_text = sh("git", "show", f"{base}:{path}")
        new_text = Path(path).read_text(encoding="utf-8")
        old_id = schema_id_from_text(old_text)
        new_id = schema_id_from_text(new_text)
        if old_id != new_id and new_id:
            continue
        if not waiver.exists():
            failures.append(
                f"same-version schema edit without waiver: {basename} (expected {waiver})"
            )

    if failures:
        print("schema compatibility check failed:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    print("ok: contracts compatibility")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
