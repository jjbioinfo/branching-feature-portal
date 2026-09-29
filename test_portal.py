"""Tests for all three User Portal features."""

from dashboard import build_dashboard
from login import LoginService
from profile import Profile


def assert_raises(expected_exception, function, *arguments) -> None:
    """Confirm that a function raises the expected exception."""
    try:
        function(*arguments)
    except expected_exception:
        return
    except Exception as error:
        raise AssertionError(
            f"expected {expected_exception.__name__}, got {type(error).__name__}"
        ) from error
    raise AssertionError(f"expected {expected_exception.__name__}")


def test_login() -> None:
    service = LoginService({"asha": "python123"})
    assert service.authenticate("asha", "python123") is True
    assert service.authenticate("asha", "wrong") is False
    assert_raises(ValueError, service.authenticate, "", "password")
    assert_raises(ValueError, service.authenticate, "asha", "")


def test_profile() -> None:
    profile = Profile("asha", "Asha Kumar", "Python learner")
    assert "Username: asha" in profile.display()
    assert "Name: Asha Kumar" in profile.display()
    assert_raises(ValueError, Profile, "", "Asha", "Learner")


def test_dashboard() -> None:
    result = build_dashboard("asha", 2, 5)
    assert "Active Courses: 2" in result
    assert "Completed Courses: 5" in result
    assert_raises(ValueError, build_dashboard, "asha", -1, 0)
    assert_raises(TypeError, build_dashboard, "asha", 1.5, 0)


def run_tests() -> int:
    """Run all test groups and return the failure count."""
    tests = [test_login, test_profile, test_dashboard]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except Exception as error:
            failures += 1
            print(f"FAIL: {test.__name__}: {error}")
    print(f"Ran {len(tests)} test groups; failures={failures}")
    return failures


if __name__ == "__main__":
    raise SystemExit(run_tests())
