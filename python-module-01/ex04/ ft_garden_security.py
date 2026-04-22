class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.age = new_age
            print(f"Age updated: {new_age} days")

    def to_string(self):
        return f"{self.name}: {round(self.height), 1}cm, {self.age} days old"


def ft_garden_security():
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)
    print(f"Plant created: {plant.to_string()}")

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)

    print(f"Current state: {plant.to_string()}")


ft_garden_security()
