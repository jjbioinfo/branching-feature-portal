"""Profile feature implemented on the feature-profile branch."""


def require_text(value: object, field_name: str) -> str:
    """Return non-empty text after removing surrounding spaces."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} cannot be empty")
    return cleaned_value


class Profile:
    """Represent a user's public profile."""

    def __init__(self, username: str, full_name: str, bio: str) -> None:
        self.username = require_text(username, "username")
        self.full_name = require_text(full_name, "full name")
        self.bio = require_text(bio, "bio")

    def display(self) -> str:
        """Return formatted profile details."""
        return (
            f"Username: {self.username}\n"
            f"Name: {self.full_name}\n"
            f"Bio: {self.bio}"
        )
