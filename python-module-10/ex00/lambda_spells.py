#!/usr/bin/env python3

from typing import List, Dict, Any


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
    mages: List[Dict[str, Any]],
    min_power: int
) -> List[Dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, float]:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = round(
        sum(map(lambda x: x["power"], mages)) / len(mages),
        2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
    ]

    mages = [
        {"name": "Aelion", "power": 90, "element": "fire"},
        {"name": "Lyra", "power": 70, "element": "water"},
        {"name": "Thorn", "power": 50, "element": "earth"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power)"
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
