from alchemy.elements import create_air


def main() -> None:
    """Test Alembic 3 using from-import on package."""
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
