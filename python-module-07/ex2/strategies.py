from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .errors import InvalidStrategyError


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )

        # 👇 agora o mypy entende o tipo
        transform_creature: TransformCapability = creature

        print(transform_creature.transform())
        print(creature.attack())
        print(transform_creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )

        # 👇 tipagem explícita
        healer: HealCapability = creature

        print(creature.attack())
        print(healer.heal())
