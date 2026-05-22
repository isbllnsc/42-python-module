from alchemy.potions import strength_potion  # absoluto
from ..elements import create_air  # relativo
from elements import create_fire  # absoluto (raiz)


def lead_to_gold() -> str:
    """Transmute lead into gold."""
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
        f"and '{strength_potion()}' mixed with '{create_fire()}'"
    )
