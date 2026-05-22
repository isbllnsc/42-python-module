import alchemy


def main() -> None:
    """Test Alembic 4 using module import."""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    try:
        # erro esperado
        print(
            "Testing the hidden create_earth: "
            f"{alchemy.create_earth()}"  # type: ignore[attr-defined]
        )
    except AttributeError as exc:
        print(exc)


if __name__ == "__main__":
    main()
