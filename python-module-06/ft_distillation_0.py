from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    """Test Distillation 0 with direct module access."""
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
