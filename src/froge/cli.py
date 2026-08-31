"""FROGE command-line interface."""

from __future__ import annotations

import argparse
import json
import sys

from froge import __version__
from froge.bootstrap import run_bootstrap
from froge.config import load_settings
from froge.discovery import discover_environment
from froge.logging_setup import setup_logging
from froge.manifest import default_registry
from froge.planner import build_plan
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
        note = " [REQUIRES VALIDATION]" if t.validation_status == "requires_validation" else ""
        print(f"  - {t.id:16} role={t.role or '-':40} method={t.installation_method}{note}")
    return 0 if result.is_success() else 1


def cmd_tools(_: argparse.Namespace) -> int:
    reg = default_registry()
    for t in reg.list():
        print(json.dumps(t.model_dump(mode="json"), indent=2, default=str))
        print("---")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
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
        print(f"  {item['id']:14} {state:12} version={str(ver)[:60]}  path={path}")
    return 0 if result.status != Status.ERROR else 1


def cmd_plan(args: argparse.Namespace) -> int:
    settings = load_settings(dry_run=True)
    setup_logging(settings.log_level)
    reg = default_registry()
    result = build_plan(reg, settings)
    print(f"FROGE plan — {result.status.value}")
    print(result.message)
    print()
    for step in result.data.get("steps", []):
        print(f"  {step['tool_id']:16} state={step['current_state']:12} → action={step['action']}")
    if getattr(args, "json", False):
        print(json.dumps(result.data, indent=2, default=str))
    return 0 if result.is_success() else 1


def cmd_bootstrap(args: argparse.Namespace) -> int:
    dry = not getattr(args, "apply", False)
    settings = load_settings(dry_run=dry)
    setup_logging(settings.log_level)
    print(f"FROGE bootstrap (dry_run={settings.dry_run})")
    result = run_bootstrap(settings=settings, verify=not getattr(args, "no_verify", False))
    print(f"\n{result.message}")
    print(f"Status: {result.status.value}")
    print()
    for entry in result.data.get("execution", []):
        vs = entry.get("verify_status", "-")
        vst = entry.get("verify_state", "-")
        print(
            f"  {entry['tool_id']:16} action={entry['planned_action']:10} "
            f"result={entry['result_status']:6} verify={vs}/{vst}"
        )
        print(f"    {entry['message']}")
    if result.errors:
        print("\nErrors:")
        for e in result.errors:
            print(f"  - {e}")
    if getattr(args, "json", False):
        print(json.dumps(result.model_dump(mode="json"), indent=2, default=str))
    return 0 if result.is_success() else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="froge", description="FROGE Agent — AI Development Control Plane")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Show status and registered tools").set_defaults(func=cmd_status)
    sub.add_parser("tools", help="List tool manifests as JSON").set_defaults(func=cmd_tools)
    sub.add_parser("doctor", help="Environment discovery").set_defaults(func=cmd_doctor)

    p_plan = sub.add_parser("plan", help="Build desired-state plan")
    p_plan.add_argument("--json", action="store_true")
    p_plan.set_defaults(func=cmd_plan)

    p_boot = sub.add_parser("bootstrap", help="Run bootstrap orchestrator")
    p_boot.add_argument("--dry-run", action="store_true", default=True)
    p_boot.add_argument("--apply", action="store_true", help="Actually mutate (disables dry-run)")
    p_boot.add_argument("--no-verify", action="store_true")
    p_boot.add_argument("--json", action="store_true")
    p_boot.set_defaults(func=cmd_bootstrap)

    sub.add_parser("version", help="Show version").set_defaults(func=cmd_version)

    args = parser.parse_args(argv)
    if args.version or args.command is None:
        return cmd_version(args)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
