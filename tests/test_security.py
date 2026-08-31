from froge.security import is_secret_env_name, redact, secret_env_present


def test_is_secret_env_name():
    assert is_secret_env_name("OPENAI_API_KEY")
    assert is_secret_env_name("MY_TOKEN")
    assert not is_secret_env_name("PATH")


def test_redact_api_key():
    s = redact("api_key=sk-abc1234567890xyz")
    assert "***REDACTED***" in s


def test_redact_bearer():
    s = redact("Authorization: Bearer secretvalue123")
    assert "secretvalue123" not in s
    assert "REDACTED" in s


def test_secret_env_present_names_only(monkeypatch):
    monkeypatch.setenv("FROGE_TEST_SECRET", "super-secret-value")
    d = secret_env_present(["FROGE_TEST_SECRET", "MISSING_KEY"])
    assert d["FROGE_TEST_SECRET"] is True
    assert d["MISSING_KEY"] is False
    assert "super-secret-value" not in str(d)
