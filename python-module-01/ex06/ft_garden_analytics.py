class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0

    def stats(self):
        print(f"[statistics for {self.name}]")
        print(
            f"Stats: {self.grow_count} grow, "
            f"{self.age_count} age, "
            f"{self.show_count} show"
        )

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self.grow_count += 1
            self.height = new_height

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age updated rejected")
        else:
            self.age = new_age

    def show_plant(self):
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    @staticmethod
    def older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show_flower(self):
        self.show_count += 1
        print(self.show_plant())
        print(f"Color: {self.color}")

        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown flower", 0.0, 0, "unknown")


class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk = trunk
        self.shade = False

    def produce_shade(self):
        self.shade = True
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk} wide."
        )

    def show_tree(self):
        self.show_count += 1
        print(self.show_plant())
        print(f"Trunk diameter: {self.trunk:.1f}cm")

    def show_shade(self):
        if self.shade:
            print("1 shade")
        else:
            print("0 shade")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show_seed(self):
        super().show_flower()  # reutiliza tudo de Flower
        print(f"Seeds: {self.seeds}")


def ft_plant_types():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")
    print("\n")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show_flower()
    print("[asking the rose to grow and bloom]")
    rose.set_height(23)
    rose.bloom()
    rose.show_flower()
    rose.stats()

    print("\n")
    print("== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show_tree()
    oak.stats()
    oak.show_shade()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.stats()
    oak.show_shade()

    print("\n")
    print("== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show_seed()
    print("[make sunflower grow, age and bloom]")
    sunflower.set_height(110)
    sunflower.set_age(65)
    sunflower.bloom()
    sunflower.show_seed()
    sunflower.stats()

    print("\n")
    print("=== Anonymous")
    anon = Plant.create_anonymous()
    print(f"{anon.name}: {anon.height}cm, {anon.age} days old")
    anon.stats()


ft_plant_types()
