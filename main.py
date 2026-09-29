"""Initial User Portal application on the main branch."""

from logging_config import configure_logging


def main() -> int:
    """Display the initial application before feature development."""
    configure_logging()
    print("User Portal")
    print("Features will be developed on separate Git branches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
