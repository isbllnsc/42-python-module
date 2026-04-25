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

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age updated rejected")
        else:
            self.age = new_age

    def show_plant(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show_flower(self):
        self.show_plant()
        print(f"Color: {self.color}")

        if self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show_tree(self):
        print(f"Trunk diameter: {self.trunk_diameter}")

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show_veg(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show_flower()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show_flower()

    print("\n")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show_tree()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show_veg()
    print("[make tomato grow and age for 20 days]")
    tomato.set_height(47)
    tomato.set_age(20)
    tomato.show_veg()


ft_plant_types()
