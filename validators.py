def validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise ValueError("Title must be a string")

    cleaned = title.strip()

    if not cleaned:
        raise ValueError("Title cannot be empty")

    if len(cleaned) > 120:
        raise ValueError("Title must not exceed 120 characters")

    return cleaned