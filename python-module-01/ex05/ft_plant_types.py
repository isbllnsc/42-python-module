class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def to_string(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

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
        print(self.to_string())
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
        self.shade = shade

    def show_tree(self)
        print(self.to_string())
        print(f"{self.shade} shade")

class Seed(Flower):
    def __init__(self, name, height, color)
        super().__init__(name, height, color)
        self.seeds = seeds


def ft_plant_types():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")
    print("\n")

    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show_flower()

    print("=== Anonymous")

    anon = Plant.create_anonymous()
    print(f"{anon.name}: {anon.height}cm, {anon.age} days old")


ft_plant_types()
