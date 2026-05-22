import sys

print("=== Inventory System Analysis ===")

inventory: dict[str, int] = {}

i = 1
while i < len(sys.argv):
    arg = sys.argv[i]

    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        i += 1
        continue

    name, qty = arg.split(":", 1)

    if name in inventory:
        print(f"Redundant item '{name}' - discarding")
        i += 1
        continue

    try:
        quantity = int(qty)
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")
        i += 1
        continue

    inventory[name] = quantity
    i += 1


print("Got inventory:", inventory)

items = list(inventory.keys())
print("Item list:", items)

total = sum(inventory.values())
print(f"Total quantity of the {len(items)} items:", total)

if total > 0:
    for name in inventory:
        percent = (inventory[name] / total) * 100
        print(f"Item {name} represents {round(percent, 1)}%")

# Mais e menos abundante
if len(inventory) > 0:
    iterator = iter(inventory)
    most_name = next(iterator)
    least_name = most_name

    for name in inventory:
        if inventory[name] > inventory[most_name]:
            most_name = name
        if inventory[name] < inventory[least_name]:
            least_name = name

    print(
        f"Item most abundant: {most_name} "
        f"with quantity {inventory[most_name]}"
    )
    print(
        f"Item least abundant: {least_name} "
        f"with quantity {inventory[least_name]}"
    )

inventory.update({"magic_item": 1})

print("Updated inventory:", inventory)
