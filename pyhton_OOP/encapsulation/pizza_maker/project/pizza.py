from pyhton_OOP.encapsulation.pizza_maker.project.dough import Dough
# from project.topping import Topping
# from project.dough import Dough
from pyhton_OOP.encapsulation.pizza_maker.project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value
        
    def add_topping(self, topping: Topping):
        if self.max_number_of_toppings == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        elif topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())


tomato_topping = Topping("Tomato", 60)
print(tomato_topping.topping_type)
print(tomato_topping.weight)

mushrooms_topping = Topping("Mushroom", 75)
print(mushrooms_topping.topping_type)
print(mushrooms_topping.weight)

mozzarella_topping = Topping("Mozzarella", 80)
print(mozzarella_topping.topping_type)
print(mozzarella_topping.weight)

cheddar_topping = Topping("Cheddar", 150)

pepperoni_topping = Topping("Pepperoni", 120)

white_flour_dough = Dough("White Flour", "Mixing", 200)
print(white_flour_dough.flour_type)
print(white_flour_dough.weight)
print(white_flour_dough.baking_technique)

whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
print(whole_wheat_dough.weight)
print(whole_wheat_dough.flour_type)
print(whole_wheat_dough.baking_technique)

p = Pizza("Margherita", whole_wheat_dough, 2)

p.add_topping(tomato_topping)
print(p.calculate_total_weight())

p.add_topping(mozzarella_topping)
print(p.calculate_total_weight())

p.add_topping(mozzarella_topping)