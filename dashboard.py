"""Dashboard feature implemented on the feature-dashboard branch."""


def build_dashboard(
    username: str, active_courses: int, completed_courses: int
) -> str:
    """Return a dashboard summary for one user."""
    if not isinstance(username, str) or not username.strip():
        raise ValueError("username cannot be empty")
    for value, field_name in (
        (active_courses, "active courses"),
        (completed_courses, "completed courses"),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{field_name} must be a whole number")
        if value < 0:
            raise ValueError(f"{field_name} cannot be negative")
    return (
        f"Dashboard for {username.strip()}\n"
        f"Active Courses: {active_courses}\n"
        f"Completed Courses: {completed_courses}"
    )
