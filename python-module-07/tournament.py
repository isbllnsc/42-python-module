from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategies import BattleStrategy
from ex0.factories import CreatureFactory
from ex2.errors import InvalidStrategyError


Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                strat1.act(c1)
                strat2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:

    print("Tournament 0 (basic)")
    t0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    battle(t0)

    print("\nTournament 1 (error)")
    t1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    battle(t1)

    print("\nTournament 2 (multiple)")
    t2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    battle(t2)


if __name__ == "__main__":
    main()
