class Plant:
		def __init__(self, name, height, age):
			self.name = name
			self.height = height
			self.age = age
		def show(self):
			print(f"{self.name}: {self.height}cm, {self.age} days old")
		def grow(self):
			if self.name == "Rose":
				self.height += 1
			elif self.name == "Sunflower":
				self.height += 3
			elif self.name == "Cactus":
				self.height += 0.5
		def age_plant(self):
			self.age += 1

def ft_plant_growth():
	print("=== Garden Plant Growth ===")
	plants = [
		Plant("Rose", 13, 20),
		Plant("Sunflower", 59, 45),
		Plant("Cactus", 14, 120)
	]
	for day in range(7):
		print(f"=== Day {day + 1} ===")
		for plant in plants:
			plant.grow()
			plant.age_plant()	
			plant.show()	
ft_plant_growth()