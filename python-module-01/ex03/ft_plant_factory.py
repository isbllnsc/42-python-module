class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def to_string(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_factory():
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    for plant in plants:
        print(f"Created: {plant.to_string()}")


ft_plant_factory()
