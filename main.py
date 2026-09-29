"""Final User Portal containing all three merged features."""

from dashboard import build_dashboard
from logging_config import configure_logging
from login import LoginService
from profile import Profile


def main() -> int:
    """Demonstrate login, profile, and dashboard features."""
    configure_logging()
    login_service = LoginService({"asha": "python123"})
    profile = Profile("asha", "Asha Kumar", "Python learner")

    print("User Portal")
    print(f"Login successful: {login_service.authenticate('asha', 'python123')}")
    print(profile.display())
    print(build_dashboard("asha", active_courses=2, completed_courses=5))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
