def is_age_suitable(age_range: str, user_age: int) -> bool:
    """Checks if the medicine is suitable for the given age."""
    if not age_range or age_range == "all":
        return True
    try:
        min_age, max_age = map(int, age_range.split('-'))
        return min_age <= user_age <= max_age
    except ValueError:
        return True  # Fallback if age_range is incorrectly formatted