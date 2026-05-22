from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    """Brew a healing potion."""
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    """Brew a strength potion."""
    return (
        f"Strength potion brewed with '{create_fire()}' "
        f"and '{create_water()}'"
    )
