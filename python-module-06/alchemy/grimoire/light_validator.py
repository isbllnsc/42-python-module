def light_spell_allowed_ingredients() -> list[str]:
    """Return allowed ingredients for light magic."""
    return ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for light spells."""
    allowed = light_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
