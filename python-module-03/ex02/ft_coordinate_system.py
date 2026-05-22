import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            for p in parts:
                try:
                    float(p.strip())
                except ValueError:
                    print(f"Error on parameter '{p.strip()}': {e}")
                    break


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
p1 = get_player_pos()

print(f"Got a first tuple: {p1}")
print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

dist_center = math.sqrt(p1[0] ** 2 + p1[1] ** 2 + p1[2] ** 2)
print("Distance to center:", round(dist_center, 4))

print("Get a second set of coordinates")
p2 = get_player_pos()

dist_points = math.sqrt(
    (p2[0] - p1[0]) ** 2
    + (p2[1] - p1[1]) ** 2
    + (p2[2] - p1[2]) ** 2
)

print(
    "Distance between the 2 sets of coordinates:",
    round(dist_points, 4),
)
