"""User Portal after merging the login and profile features."""

from logging_config import configure_logging
from login import LoginService
from profile import Profile


def main() -> int:
    """Demonstrate login and profile features."""
    configure_logging()
    login_service = LoginService({"asha": "python123"})
    profile = Profile("asha", "Asha Kumar", "Python learner")

    print("User Portal")
    print(f"Login successful: {login_service.authenticate('asha', 'python123')}")
    print(profile.display())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
