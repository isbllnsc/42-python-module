def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seed_type_cap = seed_type.capitalize()
	if unit == "packets":
		print(f"{seed_type_cap} seeds: {quantity} {unit} available")
	elif unit == "grams":
		print(f"{seed_type_cap} seeds: {quantity} {unit} total")
	elif unit == "area":
		print(f"{seed_type_cap} seeds: covers {quantity} square meters")
"""
ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
"""