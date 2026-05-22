import sys

print("=== Player Score Analytics ===")

scores = []

i = 1
while i < len(sys.argv):
    try:
        value = int(sys.argv[i])
        scores.append(value)
    except ValueError:
        print(f"Invalid parameter: '{sys.argv[i]}'")
    i += 1

# Se não tem nenhum válido
if len(scores) == 0:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py "
        "<score1> <score2> ..."
    )
else:
    total_players = len(scores)
    total_score = sum(scores)
    average = total_score / total_players
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print("Scores processed:", scores)
    print("Total players:", total_players)
    print("Total score:", total_score)
    print("Average score:", average)
    print("High score:", high)
    print("Low score:", low)
    print("Score range:", score_range)
