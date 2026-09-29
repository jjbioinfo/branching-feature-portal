"""Login feature implemented on the feature-login branch."""

import logging

logger = logging.getLogger(__name__)


class LoginService:
    """Authenticate users against an in-memory demonstration account store."""

    def __init__(self, accounts: dict[str, str]) -> None:
        self._accounts = dict(accounts)

    def authenticate(self, username: str, password: str) -> bool:
        """Return True when the supplied demonstration credentials match."""
        if not isinstance(username, str) or not username.strip():
            raise ValueError("username cannot be empty")
        if not isinstance(password, str) or not password:
            raise ValueError("password cannot be empty")
        authenticated = self._accounts.get(username.strip()) == password
        logger.info(
            f"Login attempted: username={username.strip()!r}, "
            f"authenticated={authenticated}"
        )
        return authenticated
