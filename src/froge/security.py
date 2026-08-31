"""Secret handling helpers — detect keys, never log values."""

from __future__ import annotations

import os
import re
from typing import Iterable

_SECRET_NAME_HINTS = (
    "API_KEY",
    "APIKEY",
    "SECRET",
    "TOKEN",
    "PASSWORD",
    "PASSWD",
    "PRIVATE_KEY",
    "ACCESS_KEY",
    "AUTH",
    "CREDENTIAL",
)

_REDACT_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*\S+"),
    re.compile(r"(?i)bearer\s+[a-z0-9._\-]+"),
    re.compile(r"sk-[a-zA-Z0-9]{10,}"),
]


def is_secret_env_name(name: str) -> bool:
    upper = name.upper()
    return any(h in upper for h in _SECRET_NAME_HINTS)


def secret_env_present(names: Iterable[str]) -> dict[str, bool]:
    """Return whether each env var *name* is set — never the value."""
    return {n: bool(os.environ.get(n)) for n in names}


def redact(text: str) -> str:
    """Redact likely secret material from a string before logging."""
    if not text:
        return text
    out = text
    out = re.sub(r"(?i)bearer\s+[a-z0-9._\-]+", "Bearer ***REDACTED***", out)
    out = re.sub(r"sk-[a-zA-Z0-9]{10,}", "sk-***REDACTED***", out)
    out = re.sub(
        r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*\S+",
        r"\1=***REDACTED***",
        out,
    )
    return out
