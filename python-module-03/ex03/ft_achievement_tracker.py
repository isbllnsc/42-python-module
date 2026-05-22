import random

print("=== Achievement Tracker System ===")


def gen_player_achievements() -> set[str]:
    all_achievements = [
        "First Steps", "Survivor", "Speed Runner", "Master Explorer",
        "Treasure Hunter", "Crafting Genius", "Strategist",
        "Untouchable", "Boss Slayer", "World Savior",
        "Sharp Mind", "Collector Supreme", "Unstoppable",
        "Hidden Path Finder",
    ]

    count = random.randint(3, 8)
    return set(random.sample(all_achievements, count))


players: dict[str, set[str]] = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements(),
}

# Mostrar jogadores
for name in players:
    print(f"Player {name}: {players[name]}")

# União (todos distintos)
all_achievements: set[str] = set()
for s in players.values():
    all_achievements = all_achievements.union(s)

print("All distinct achievements:", all_achievements)

# Interseção (comum a todos)
if len(players) > 0:
    iterator = iter(players.values())
    common = next(iterator)

    for s in players.values():
        common = common.intersection(s)

    print("Common achievements:", common)

# Só um jogador tem
for name in players:
    others: set[str] = set()
    for other_name in players:
        if other_name != name:
            others = others.union(players[other_name])

    unique = players[name].difference(others)
    print(f"Only {name} has:", unique)

# Faltando para completar tudo
for name in players:
    missing = all_achievements.difference(players[name])
    print(f"{name} is missing:", missing)
