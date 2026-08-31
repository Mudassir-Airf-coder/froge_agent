"""Structured result and evidence contracts."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"


class Evidence(BaseModel):
    """Observable evidence produced by an operation."""

    kind: str = Field(..., description="Evidence type, e.g. command_output, http_response")
    summary: str = ""
    data: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class OperationResult(BaseModel):
    """Standard result returned by every major FROGE operation."""

    operation: str
    status: Status
    message: str = ""
    data: dict[str, Any] = Field(default_factory=dict)
    errors: list[str] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    component: Optional[str] = None
    state: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def add_evidence(self, kind: str, summary: str = "", **data: Any) -> None:
        self.evidence.append(Evidence(kind=kind, summary=summary, data=data))

    def is_success(self) -> bool:
        return self.status in (Status.PASS, Status.SKIP)

    def to_report_line(self) -> str:
        return f"{self.operation}: {self.status.value} — {self.message}"
