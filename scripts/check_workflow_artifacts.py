#!/usr/bin/env python3
"""Check that context-first writing workflow artifacts exist and are nontrivial."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


WRITING_FILES = (
    "01-context-and-mainline.md",
    "02-paragraph-map.md",
    "03-propositions.md",
    "04-context-and-relations.md",
    "05-connected-skeleton.md",
    "06-expanded-draft.md",
    "07-readback.md",
)

TRANSLATION_FILES = (
    "00-source-version.md",
    "01-context-and-mainline.md",
    "02-source-paragraph-map.md",
    "03-source-propositions-and-evidence.md",
    "04-target-paragraph-map.md",
    "05-target-skeleton.md",
    "06-target-context-and-relations.md",
    "07-expanded-translation.md",
    "08-bilingual-proposition-map.md",
    "09-target-readback.md",
    "10-cross-version-audit.md",
    "terminology.md",
)

PLACEHOLDERS = ("TODO", "TBD", "[fill", "待填写", "待补充")
MIN_CHARS = 80


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing: {path.name}"]
    text = path.read_text(encoding="utf-8-sig").strip()
    if len(text) < MIN_CHARS:
        errors.append(f"too short ({len(text)} chars): {path.name}")
    lowered = text.casefold()
    for marker in PLACEHOLDERS:
        if marker.casefold() in lowered:
            errors.append(f"unfinished marker {marker!r}: {path.name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate required artifacts for context-first paper writing."
    )
    parser.add_argument("artifact_directory", type=Path)
    parser.add_argument(
        "--mode", choices=("writing", "translation"), default="writing"
    )
    args = parser.parse_args()

    root = args.artifact_directory.resolve()
    if not root.is_dir():
        print(f"error: artifact directory does not exist: {root}", file=sys.stderr)
        return 2

    required = WRITING_FILES if args.mode == "writing" else TRANSLATION_FILES
    errors: list[str] = []
    for name in required:
        errors.extend(check_file(root / name))

    if errors:
        print(f"{args.mode} workflow artifacts failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"{args.mode} workflow artifacts present: {len(required)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
