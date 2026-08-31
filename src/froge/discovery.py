"""Environment discovery — inspect OS, runtimes, paths, versions."""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
from dataclasses import dataclass, field
from typing import Any, Optional

from froge.results import OperationResult, Status
from froge.state import ComponentState


@dataclass
class DiscoveredItem:
    """Result of discovering one dependency / executable."""

    id: str
    name: str
    state: ComponentState
    version: Optional[str] = None
    path: Optional[str] = None
    details: dict[str, Any] = field(default_factory=dict)


def _run(cmd: list[str], timeout: int = 15) -> tuple[int, str, str]:
    try:
        p = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except FileNotFoundError:
        return 127, "", "not found"
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"
    except Exception as exc:
        return 1, "", str(exc)


def discover_executable(exe_name: str, version_args: Optional[list[str]] = None) -> DiscoveredItem:
    """Locate an executable and optionally query its version."""
    path = shutil.which(exe_name)
    if path is None:
        return DiscoveredItem(
            id=exe_name,
            name=exe_name,
            state=ComponentState.MISSING,
        )
    version = None
    if version_args is not None:
        code, out, err = _run([path] + version_args)
        version = out or err or None
        if code != 0 and version is None:
            return DiscoveredItem(
                id=exe_name,
                name=exe_name,
                state=ComponentState.BROKEN,
                path=path,
                details={"exit_code": code, "stderr": err},
            )
    return DiscoveredItem(
        id=exe_name,
        name=exe_name,
        state=ComponentState.INSTALLED,
        version=version,
        path=path,
    )


def discover_environment() -> OperationResult:
    """Run a standard set of environment discoveries."""
    items: list[DiscoveredItem] = []

    items.append(
        DiscoveredItem(
            id="os",
            name="Operating System",
            state=ComponentState.INSTALLED,
            version=platform.platform(),
            details={
                "system": platform.system(),
                "release": platform.release(),
                "machine": platform.machine(),
                "python": platform.python_version(),
            },
        )
    )

    for exe, vargs in [
        ("python", ["--version"]),
        ("python3", ["--version"]),
        ("pip", ["--version"]),
        ("pip3", ["--version"]),
        ("git", ["--version"]),
        ("node", ["--version"]),
        ("npm", ["--version"]),
        ("docker", ["--version"]),
        ("pwsh", ["--version"]),
        ("powershell", ["-Command", "$PSVersionTable.PSVersion"]),
    ]:
        items.append(discover_executable(exe, vargs))

    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    data = {
        "items": [
            {
                "id": i.id,
                "state": i.state.value,
                "version": i.version,
                "path": i.path,
                "details": i.details,
            }
            for i in items
        ],
        "path_entries": len(path_dirs),
        "platform": platform.system(),
    }

    missing = [i for i in items if i.state == ComponentState.MISSING]
    broken = [i for i in items if i.state == ComponentState.BROKEN]
    status = Status.PASS
    msg = f"Discovered {len(items)} items; missing={len(missing)}, broken={len(broken)}"
    if broken:
        status = Status.FAIL
        msg += " (broken components present)"

    result = OperationResult(
        operation="discovery.environment",
        status=status,
        message=msg,
        data=data,
    )
    for i in items:
        result.add_evidence(
            "discovery",
            summary=f"{i.id}: {i.state.value}",
            version=i.version,
            path=i.path,
        )
    return result
