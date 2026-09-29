"""User Portal after merging the login feature."""

from logging_config import configure_logging
from login import LoginService


def main() -> int:
    """Demonstrate the login feature."""
    configure_logging()
    login_service = LoginService({"asha": "python123"})
    print("User Portal")
    print(f"Login successful: {login_service.authenticate('asha', 'python123')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
