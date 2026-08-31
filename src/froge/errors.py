"""Structured error classification for FROGE operations."""

from __future__ import annotations

from enum import Enum


class ErrorKind(str, Enum):
    COMMAND_NOT_FOUND = "COMMAND_NOT_FOUND"
    TIMEOUT = "TIMEOUT"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    INVALID_CONFIGURATION = "INVALID_CONFIGURATION"
    DEPENDENCY_FAILURE = "DEPENDENCY_FAILURE"
    NETWORK_ERROR = "NETWORK_ERROR"
    AUTH_ERROR = "AUTH_ERROR"
    VERSION_MISMATCH = "VERSION_MISMATCH"
    INSTALL_FAILED = "INSTALL_FAILED"
    HEALTH_CHECK_FAILED = "HEALTH_CHECK_FAILED"
    FUNCTIONAL_TEST_FAILED = "FUNCTIONAL_TEST_FAILED"
    CYCLE_DETECTED = "CYCLE_DETECTED"
    REQUIRES_VALIDATION = "REQUIRES_VALIDATION"
    REQUIRES_MANUAL_INTERVENTION = "REQUIRES_MANUAL_INTERVENTION"
    UNKNOWN = "UNKNOWN"


class Recoverability(str, Enum):
    RECOVERABLE = "RECOVERABLE"
    NON_RECOVERABLE = "NON_RECOVERABLE"
    REQUIRES_VALIDATION = "REQUIRES_VALIDATION"
    REQUIRES_MANUAL = "REQUIRES_MANUAL"


def classify_exit(exit_code: int, stderr: str = "", stdout: str = "") -> ErrorKind:
    text = f"{stderr} {stdout}".lower()
    if exit_code == 127 or "not found" in text or "is not recognized" in text:
        return ErrorKind.COMMAND_NOT_FOUND
    if exit_code == 124 or "timeout" in text:
        return ErrorKind.TIMEOUT
    if exit_code in (126, 5) or "permission" in text or "access is denied" in text:
        return ErrorKind.PERMISSION_DENIED
    if "network" in text or "connection" in text or "could not resolve" in text:
        return ErrorKind.NETWORK_ERROR
    if "auth" in text or "unauthorized" in text or "401" in text or "403" in text:
        return ErrorKind.AUTH_ERROR
    if exit_code != 0:
        return ErrorKind.INSTALL_FAILED
    return ErrorKind.UNKNOWN


def recoverability(kind: ErrorKind) -> Recoverability:
    if kind in (
        ErrorKind.TIMEOUT,
        ErrorKind.NETWORK_ERROR,
        ErrorKind.INSTALL_FAILED,
        ErrorKind.HEALTH_CHECK_FAILED,
        ErrorKind.FUNCTIONAL_TEST_FAILED,
    ):
        return Recoverability.RECOVERABLE
    if kind in (ErrorKind.REQUIRES_VALIDATION,):
        return Recoverability.REQUIRES_VALIDATION
    if kind in (
        ErrorKind.AUTH_ERROR,
        ErrorKind.INVALID_CONFIGURATION,
        ErrorKind.CYCLE_DETECTED,
        ErrorKind.REQUIRES_MANUAL_INTERVENTION,
    ):
        return Recoverability.REQUIRES_MANUAL
    if kind == ErrorKind.COMMAND_NOT_FOUND:
        return Recoverability.RECOVERABLE
    return Recoverability.NON_RECOVERABLE
