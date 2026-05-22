from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("Testing Creature with healing capability")

    factory = HealingCreatureFactory()

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())  # type: ignore[attr-defined]

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())  # type: ignore[attr-defined]


def test_transform() -> None:
    print("Testing Creature with transform capability")

    factory = TransformCreatureFactory()

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())  # type: ignore[attr-defined]
    print(base.attack())
    print(base.revert())  # type: ignore[attr-defined]

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())  # type: ignore[attr-defined]
    print(evolved.attack())
    print(evolved.revert())  # type: ignore[attr-defined]


def main() -> None:
    test_healing()
    test_transform()


if __name__ == "__main__":
    main()
