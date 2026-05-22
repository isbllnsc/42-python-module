import random

print("=== Game Data Alchemist ===")

players = [
    'Alice', 'bob', 'Charlie', 'dylan',
    'Emma', 'Gregory', 'john', 'kevin',
    'Liam'
]

print("Initial list of players:", players)

# Todos capitalizados
capitalized = [name.capitalize() for name in players]
print("New list with all names capitalized:", capitalized)

# Só os que já estavam capitalizados
only_capitalized = [name for name in players if name[0].isupper()]
print("New list of capitalized names only:", only_capitalized)

# Dict de scores
scores = {name: random.randint(0, 1000) for name in capitalized}
print("Score dict:", scores)

# Média
avg = sum(scores.values()) / len(scores)
print("Score average is", round(avg, 2))

# Acima da média
high_scores = {k: v for k, v in scores.items() if v > avg}
print("High scores:", high_scores)
