def main() -> None:
    """Test Kaboom 1: circular import explosion."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    # NÃO colocar try/except se quiser seguir exatamente o enunciado
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Darkness", "bats"))


if __name__ == "__main__":
    main()
