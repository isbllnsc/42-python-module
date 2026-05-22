#!/usr/bin/env python3

import time
from functools import wraps
from collections.abc import Callable
from typing import TypeVar, Any

T = TypeVar("T")


def spell_timer(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        print(f"Casting {func.__name__}...")
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[
    [Callable[..., T]], Callable[..., T]
]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[
    [Callable[..., T]], Callable[..., T]
]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:
    raise ValueError("Boom!")


def main() -> None:
    print("Testing spell timer...")
    print("Result:", fireball())

    print("\nTesting retrying spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("x1"))

    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))


if __name__ == "__main__":
    main()
