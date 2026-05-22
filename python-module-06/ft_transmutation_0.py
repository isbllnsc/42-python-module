from alchemy.transmutation.recipes import lead_to_gold


def main() -> None:
    """Test Transmutation 0 with direct file import."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {lead_to_gold()}")


if __name__ == "__main__":
    main()
