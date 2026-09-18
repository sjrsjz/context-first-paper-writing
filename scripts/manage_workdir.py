#!/usr/bin/env python3
"""Create and safely clean ephemeral context-first writing work directories."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile


TOOL = "context-first-paper-writing"
VERSION = 1
SENTINEL = ".context-first-workdir.json"


def slug(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-._")
    return cleaned[:64] or fallback


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def default_root() -> Path:
    return Path(tempfile.gettempdir()) / TOOL


def is_descendant(path: Path, root: Path) -> bool:
    return path != root and path.is_relative_to(root)


def init_workdir(args: argparse.Namespace) -> int:
    project = Path(args.project).expanduser().resolve()
    root = Path(args.root).expanduser().resolve() if args.root else default_root().resolve()
    project_hash = hashlib.sha256(str(project).encode("utf-8")).hexdigest()[:10]
    project_key = f"{slug(project.name, 'project')}-{project_hash}"
    task_key = slug(args.task, "task")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    workdir = (root / project_key / f"{task_key}-{stamp}").resolve()

    if not is_descendant(workdir, root):
        print("error: generated work directory is outside the work root", file=sys.stderr)
        return 2
    if workdir.exists():
        print(f"error: work directory already exists: {workdir}", file=sys.stderr)
        return 2

    workdir.mkdir(parents=True)
    manifest = {
        "tool": TOOL,
        "version": VERSION,
        "root": str(root),
        "workdir": str(workdir),
        "project": str(project),
        "task": args.task,
        "created_at": utc_now(),
        "status": "active",
    }
    (workdir / SENTINEL).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(workdir)
    return 0


def load_and_verify(workdir_arg: str) -> tuple[Path, Path, dict[str, object]]:
    raw = Path(workdir_arg).expanduser()
    if raw.is_symlink():
        raise ValueError("work directory must not be a symbolic link")
    workdir = raw.resolve(strict=True)
    if not workdir.is_dir():
        raise ValueError("work directory is not a directory")

    sentinel = workdir / SENTINEL
    if not sentinel.is_file() or sentinel.is_symlink():
        raise ValueError(f"missing safe-cleanup sentinel: {SENTINEL}")
    manifest = json.loads(sentinel.read_text(encoding="utf-8"))
    if manifest.get("tool") != TOOL or manifest.get("version") != VERSION:
        raise ValueError("sentinel tool or version mismatch")

    recorded_workdir = Path(str(manifest.get("workdir", ""))).resolve()
    root = Path(str(manifest.get("root", ""))).resolve()
    if recorded_workdir != workdir:
        raise ValueError("sentinel work directory does not match requested directory")
    if not is_descendant(workdir, root):
        raise ValueError("refusing to clean the root or a directory outside it")
    return workdir, root, manifest


def remove_child(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def cleanup_workdir(args: argparse.Namespace) -> int:
    try:
        workdir, _root, manifest = load_and_verify(args.workdir)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    if args.keep_summary:
        summary = workdir / "summary.md"
        if not summary.is_file() or summary.is_symlink():
            print("error: --keep-summary requires a regular summary.md", file=sys.stderr)
            return 2
        for child in list(workdir.iterdir()):
            if child.name not in {SENTINEL, "summary.md"}:
                remove_child(child)
        manifest["status"] = "cleaned-summary-retained"
        manifest["cleaned_at"] = utc_now()
        (workdir / SENTINEL).write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(summary)
        return 0

    shutil.rmtree(workdir)
    print(f"removed: {workdir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage safe temporary work directories for context-first writing."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create a marked work directory")
    init_parser.add_argument("--project", required=True, help="project root or identifier path")
    init_parser.add_argument("--task", required=True, help="short task name")
    init_parser.add_argument("--root", help="optional work root; defaults to the OS temp directory")
    init_parser.set_defaults(handler=init_workdir)

    cleanup_parser = subparsers.add_parser(
        "cleanup", help="safely remove a marked work directory"
    )
    cleanup_parser.add_argument("workdir")
    cleanup_parser.add_argument(
        "--keep-summary",
        action="store_true",
        help="remove intermediates but retain summary.md and the cleanup sentinel",
    )
    cleanup_parser.set_defaults(handler=cleanup_workdir)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
