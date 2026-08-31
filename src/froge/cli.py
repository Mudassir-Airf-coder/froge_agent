"""FROGE command-line interface."""

from __future__ import annotations

import argparse
import json
import sys

from froge import __version__
from froge.bootstrap import run_bootstrap
from froge.config import load_settings
from froge.discovery import discover_environment
from froge.health import verify_tool
from froge.logging_setup import setup_logging
from froge.manifest import default_registry
from froge.persistence import load_state
from froge.planner import build_plan
from froge.results import Status


def _print_json(obj) -> None:
    if hasattr(obj, "model_dump"):
        print(json.dumps(obj.model_dump(mode="json"), indent=2, default=str))
    else:
        print(json.dumps(obj, indent=2, default=str))


def cmd_version(_: argparse.Namespace) -> int:
    print(f"froge {__version__}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    settings = load_settings()
    setup_logging(settings.log_level)
    reg = default_registry()
    result = reg.validate()
    store = load_state(settings)
    payload = {
        "version": __version__,
        "data_dir": str(settings.data_dir),
        "dry_run": settings.dry_run,
        "tools_registered": len(reg),
        "registry_status": result.status.value,
        "state": store.summary(),
        "tools": [
            {
                "id": t.id,
                "role": t.role,
                "method": t.installation_method,
                "validation_status": t.validation_status,
            }
            for t in reg.list()
        ],
    }
    if getattr(args, "json", False):
        _print_json(payload)
        return 0 if result.is_success() else 1
    print(f"FROGE {__version__}")
    print(f"Data dir     : {settings.data_dir}")
    print(f"State file   : {store.path}")
    print(f"Dry run      : {settings.dry_run}")
    print(f"Tools registered: {len(reg)}")
    print(f"Registry     : {result.status.value} — {result.message}")
    print(f"Persisted components: {store.summary()['component_count']}")
    print("\nRegistered tools:")
    for t in reg.list():
        note = " [REQUIRES VALIDATION]" if t.validation_status == "requires_validation" else ""
        print(f"  - {t.id:16} role={t.role or '-':40} method={t.installation_method}{note}")
    return 0 if result.is_success() else 1


def cmd_tools(args: argparse.Namespace) -> int:
    reg = default_registry()
    for t in reg.list():
        print(json.dumps(t.model_dump(mode="json"), indent=2, default=str))
        print("---")
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    settings = load_settings()
    setup_logging(settings.log_level)
    result = discover_environment()
    if getattr(args, "json", False):
        _print_json(result)
        return 0 if result.status != Status.ERROR else 1
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
    if getattr(args, "json", False):
        _print_json(result)
        return 0 if result.is_success() else 1
    print(f"FROGE plan — {result.status.value}")
    print(result.message)
    print()
    for step in result.data.get("steps", []):
        print(f"  {step['tool_id']:16} state={step['current_state']:12} → action={step['action']}")
    return 0 if result.is_success() else 1


def cmd_bootstrap(args: argparse.Namespace) -> int:
    dry = not getattr(args, "apply", False)
    settings = load_settings(dry_run=dry)
    setup_logging(settings.log_level)
    print(f"FROGE bootstrap (dry_run={settings.dry_run})")
    result = run_bootstrap(settings=settings, verify=not getattr(args, "no_verify", False))
    if getattr(args, "json", False):
        _print_json(result)
        return 0 if result.is_success() else 1
    print(f"\n{result.message}")
    print(f"Status: {result.status.value}")
    print(f"State : {result.data.get('state_path')}")
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
    return 0 if result.is_success() else 1


def cmd_state(args: argparse.Namespace) -> int:
    settings = load_settings()
    store = load_state(settings)
    summary = store.summary()
    if getattr(args, "json", False):
        _print_json(summary)
        return 0
    print(f"State file: {summary['path']}")
    print(f"Components: {summary['component_count']}")
    print(f"Operations: {summary['operation_count']}")
    for tid, info in summary.get("components", {}).items():
        print(
            f"  {tid:16} state={info.get('state')} ver={info.get('version')} "
            f"last_verify={info.get('last_verification_status')}"
        )
    if getattr(args, "ops", False):
        print("\nRecent operations:")
        for op in store.list_operations(20):
            print(f"  {op['timestamp']} {op['component']:12} {op['action']:10} {op['status']}")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    reg = default_registry()
    tool_id = getattr(args, "tool", None)
    tools = [reg.get(tool_id)] if tool_id else reg.list(enabled_only=True)
    tools = [t for t in tools if t is not None]
    results = []
    for t in tools:
        r = verify_tool(t)
        results.append(r)
        if not getattr(args, "json", False):
            print(f"{t.id:16} {r.status.value:6} state={r.state} — {r.message}")
            for k, v in (r.data.get("levels") or {}).items():
                print(f"    {k}: {v}")
    if getattr(args, "json", False):
        _print_json([r.model_dump(mode="json") for r in results])
    return 0 if all(r.is_success() or r.status == Status.SKIP for r in results) else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="froge", description="FROGE Agent — AI Development Control Plane"
    )
    parser.add_argument("--version", action="store_true")
    sub = parser.add_subparsers(dest="command")

    for name, help_, fn in [
        ("status", "Show status", cmd_status),
        ("tools", "List manifests", cmd_tools),
        ("doctor", "Environment discovery", cmd_doctor),
        ("plan", "Desired-state plan", cmd_plan),
        ("bootstrap", "Bootstrap orchestrator", cmd_bootstrap),
        ("state", "Show persistent state", cmd_state),
        ("verify", "Run health verification", cmd_verify),
        ("version", "Show version", cmd_version),
    ]:
        p = sub.add_parser(name, help=help_)
        p.set_defaults(func=fn)
        if name in ("status", "doctor", "plan", "bootstrap", "state", "verify"):
            p.add_argument("--json", action="store_true")
        if name == "bootstrap":
            p.add_argument("--dry-run", action="store_true", default=True)
            p.add_argument("--apply", action="store_true")
            p.add_argument("--no-verify", action="store_true")
        if name == "state":
            p.add_argument("--ops", action="store_true", help="Show recent operations")
        if name == "verify":
            p.add_argument("--tool", help="Verify a single tool id")

    args = parser.parse_args(argv)
    if args.version or args.command is None:
        return cmd_version(args)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
