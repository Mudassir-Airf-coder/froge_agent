"""FROGE command-line interface."""

from __future__ import annotations

import argparse
import json
import sys

from froge import __version__
from froge.config import load_settings
from froge.discovery import discover_environment
from froge.logging_setup import setup_logging
from froge.manifest import default_registry
from froge.results import Status


def cmd_version(_: argparse.Namespace) -> int:
    print(f"froge {__version__}")
    return 0


def cmd_status(_: argparse.Namespace) -> int:
    settings = load_settings()
    setup_logging(settings.log_level)
    reg = default_registry()
    result = reg.validate()
    print(f"FROGE {__version__}")
    print(f"Data dir     : {settings.data_dir}")
    print(f"Dry run      : {settings.dry_run}")
    print(f"Tools registered: {len(reg)}")
    print(f"Registry     : {result.status.value} — {result.message}")
    if result.errors:
        for e in result.errors:
            print(f"  ERROR: {e}")
    print("\nRegistered tools:")
    for t in reg.list():
        print(f"  - {t.id:16} role={t.role or '-':40} method={t.installation_method}")
    return 0 if result.is_success() else 1


def cmd_tools(_: argparse.Namespace) -> int:
    reg = default_registry()
    for t in reg.list():
        print(json.dumps(t.model_dump(mode="json"), indent=2, default=str))
        print("---")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    """Run environment discovery and print a diagnostic report."""
    settings = load_settings()
    setup_logging(settings.log_level)
    result = discover_environment()
    print(f"FROGE doctor — {result.status.value}")
    print(result.message)
    print()
    for item in result.data.get("items", []):
        state = item["state"]
        ver = item.get("version") or "-"
        path = item.get("path") or "-"
        print(f"  {item['id']:14} {state:12} version={ver[:60]}  path={path}")
    return 0 if result.status != Status.ERROR else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="froge",
        description="FROGE Agent — AI Development Control Plane",
    )
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    sub = parser.add_subparsers(dest="command")

    p_status = sub.add_parser("status", help="Show FROGE status and registered tools")
    p_status.set_defaults(func=cmd_status)

    p_tools = sub.add_parser("tools", help="List tool manifests as JSON")
    p_tools.set_defaults(func=cmd_tools)

    p_doctor = sub.add_parser("doctor", help="Environment discovery / diagnostics")
    p_doctor.set_defaults(func=cmd_doctor)

    p_ver = sub.add_parser("version", help="Show version")
    p_ver.set_defaults(func=cmd_version)

    args = parser.parse_args(argv)
    if args.version or args.command is None:
        return cmd_version(args)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
