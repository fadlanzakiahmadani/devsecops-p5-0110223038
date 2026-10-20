from validators import validate_title


def sanitize_task_title(title: str) -> str:
    """Validate and normalize a task title."""
    return validate_title(title)