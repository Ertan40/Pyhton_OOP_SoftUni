from pyhton_OOP.polymorphism_and_abstraction.wild_farm.project.animals.animal import Bird
# from project.animals.animal import Bird
from pyhton_OOP.polymorphism_and_abstraction.wild_farm.project.food import Meat, Vegetable, Seed, Fruit
# from project.food import Meat, Vegetable, Seed, Fruit

class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weights(self):
        return 0.25

class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Vegetable, Seed, Fruit, Meat]

    @property
    def gained_weights(self):
        return 0.35

