from froge.errors import ErrorKind, classify_exit, recoverability, Recoverability


def test_classify_not_found():
    assert classify_exit(127, "command not found") == ErrorKind.COMMAND_NOT_FOUND


def test_classify_timeout():
    assert classify_exit(124, "timeout") == ErrorKind.TIMEOUT


def test_recoverability_install_failed():
    assert recoverability(ErrorKind.INSTALL_FAILED) == Recoverability.RECOVERABLE


def test_recoverability_auth():
    assert recoverability(ErrorKind.AUTH_ERROR) == Recoverability.REQUIRES_MANUAL
