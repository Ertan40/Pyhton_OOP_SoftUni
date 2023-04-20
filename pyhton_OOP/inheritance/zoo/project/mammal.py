from pyhton_OOP.inheritance.zoo.project.animal import Animal
# from project.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)