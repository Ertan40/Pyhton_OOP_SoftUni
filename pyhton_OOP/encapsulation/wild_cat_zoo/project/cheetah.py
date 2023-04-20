# from pyhton_OOP.inheritance.zoo.project.animal import Animal
from project.animal import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE = 60
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Cheetah.MONEY_FOR_CARE)