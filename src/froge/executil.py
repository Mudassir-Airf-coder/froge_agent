"""Safe subprocess execution — argument arrays preferred, full evidence."""

from __future__ import annotations

import shutil
import subprocess
from typing import Optional

from froge.errors import ErrorKind, classify_exit, recoverability
from froge.results import OperationResult, Status


def run_command(
    cmd: list[str],
    *,
    timeout: int = 120,
    cwd: Optional[str] = None,
    env: Optional[dict] = None,
    operation: str = "exec.run",
    component: str = "",
) -> OperationResult:
    """Execute a command as an argument array. Never shell=True."""
    if not cmd:
        return OperationResult(
            operation=operation,
            status=Status.FAIL,
            component=component,
            message="empty command",
            errors=["empty command"],
        )
    exe = cmd[0]
    if shutil.which(exe) is None and "/" not in exe and "\\" not in exe:
        result = OperationResult(
            operation=operation,
            status=Status.FAIL,
            component=component,
            message=f"command not found: {exe}",
            errors=[f"COMMAND_NOT_FOUND: {exe}"],
            data={"cmd": cmd, "error_kind": ErrorKind.COMMAND_NOT_FOUND.value},
        )
        result.add_evidence("exec", summary=f"not found: {exe}", cmd=cmd)
        return result

    try:
        p = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            cwd=cwd,
            env=env,
            shell=False,
        )
        code = p.returncode
        out = (p.stdout or "").strip()
        err = (p.stderr or "").strip()
        kind = classify_exit(code, err, out) if code != 0 else None
        status = Status.PASS if code == 0 else Status.FAIL
        result = OperationResult(
            operation=operation,
            status=status,
            component=component,
            message=f"exit={code}",
            data={
                "cmd": cmd,
                "exit_code": code,
                "stdout": out[:2000],
                "stderr": err[:2000],
                "error_kind": kind.value if kind else None,
                "recoverability": recoverability(kind).value if kind else None,
            },
            errors=[err] if code != 0 and err else ([f"exit {code}"] if code != 0 else []),
        )
        result.add_evidence(
            "exec",
            summary=" ".join(cmd),
            exit_code=code,
            stdout=out[:500],
            stderr=err[:500],
        )
        return result
    except subprocess.TimeoutExpired:
        result = OperationResult(
            operation=operation,
            status=Status.FAIL,
            component=component,
            message=f"timeout after {timeout}s",
            errors=["TIMEOUT"],
            data={"cmd": cmd, "error_kind": ErrorKind.TIMEOUT.value},
        )
        result.add_evidence("exec", summary="timeout", cmd=cmd)
        return result
    except Exception as exc:
        result = OperationResult(
            operation=operation,
            status=Status.ERROR,
            component=component,
            message=str(exc),
            errors=[str(exc)],
            data={"cmd": cmd, "error_kind": ErrorKind.UNKNOWN.value},
        )
        result.add_evidence("exec", summary=str(exc), cmd=cmd)
        return result
