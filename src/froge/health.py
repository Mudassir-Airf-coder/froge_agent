"""Health / verification engine — multi-level ladder (docs/health.md)."""

from __future__ import annotations

import shutil
import subprocess
from typing import Optional

from froge.manifest import ToolManifest
from froge.results import OperationResult, Status
from froge.state import ComponentState


def _run(cmd: list[str], timeout: int = 30) -> tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except FileNotFoundError:
        return 127, "", "not found"
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"
    except Exception as exc:
        return 1, "", str(exc)


def verify_tool(tool: ToolManifest, levels: Optional[list[int]] = None) -> OperationResult:
    """Run verification ladder. Unsupported levels are SKIP, not FAIL."""
    if levels is None:
        levels = [1, 2, 3, 4, 5, 6]

    result = OperationResult(operation="health.verify", status=Status.PASS, component=tool.id, message="")
    level_results: dict[str, str] = {}
    overall_state = ComponentState.UNKNOWN

    if 1 in levels:
        path = shutil.which(tool.executable) if tool.executable else None
        if tool.executable is None and tool.installation_method == "unknown":
            level_results["L1_existence"] = "SKIP"
            result.add_evidence("L1_existence", summary="no executable defined (REQUIRES VALIDATION)")
        elif path:
            level_results["L1_existence"] = "PASS"
            result.add_evidence("L1_existence", summary=f"found at {path}", path=path)
            overall_state = ComponentState.INSTALLED
        else:
            level_results["L1_existence"] = "FAIL"
            result.add_evidence("L1_existence", summary="executable not found")
            result.status = Status.FAIL
            result.state = ComponentState.MISSING.value
            result.message = f"{tool.id}: MISSING"
            result.data["levels"] = level_results
            return result

    if 2 in levels and tool.executable:
        cmd = tool.version_command or [tool.executable, "--version"]
        code, out, err = _run(cmd)
        ver = out or err
        if code == 0 or ver:
            level_results["L2_version"] = "PASS"
            result.add_evidence("L2_version", summary=(ver or "ok")[:200], exit_code=code)
            overall_state = ComponentState.INSTALLED
        else:
            level_results["L2_version"] = "FAIL"
            result.add_evidence("L2_version", summary="version check failed", exit_code=code, stderr=err)
            result.status = Status.FAIL
            overall_state = ComponentState.BROKEN

    if 3 in levels and tool.executable and level_results.get("L1_existence") == "PASS":
        level_results["L3_invocation"] = level_results.get("L2_version", "PASS")
        result.add_evidence("L3_invocation", summary="covered by version check")

    if 4 in levels:
        if tool.configuration:
            level_results["L4_config"] = "SKIP"
            result.add_evidence("L4_config", summary="config validation not yet implemented")
        else:
            level_results["L4_config"] = "PASS"
            result.add_evidence("L4_config", summary="no config required")

    if 5 in levels:
        if tool.gateway:
            level_results["L5_gateway"] = "SKIP"
            result.add_evidence("L5_gateway", summary="gateway check not yet implemented")
        else:
            level_results["L5_gateway"] = "PASS"
            result.add_evidence("L5_gateway", summary="no gateway defined")

    if 6 in levels:
        ft = tool.functional_test
        if ft and ft.command:
            parts = ft.command.split()
            code, out, err = _run(parts, timeout=ft.timeout_seconds)
            if code == ft.expected_exit_code:
                level_results["L6_functional"] = "PASS"
                result.add_evidence("L6_functional", summary=(out or "ok")[:200], exit_code=code)
                if result.status == Status.PASS:
                    overall_state = ComponentState.HEALTHY
            else:
                level_results["L6_functional"] = "FAIL"
                result.add_evidence("L6_functional", summary="functional test failed", exit_code=code, stderr=err)
                result.status = Status.FAIL
                overall_state = ComponentState.DEGRADED
        else:
            level_results["L6_functional"] = "SKIP"
            result.add_evidence("L6_functional", summary="no functional test defined")

    result.state = overall_state.value
    result.data["levels"] = level_results
    if result.status == Status.PASS:
        result.message = f"{tool.id}: {overall_state.value}"
    else:
        result.message = f"{tool.id}: verification failed ({overall_state.value})"
    return result
