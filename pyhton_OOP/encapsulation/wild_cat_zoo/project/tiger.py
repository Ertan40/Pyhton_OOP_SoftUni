# from pyhton_OOP.inheritance.zoo.project.animal import Animal
from project.animal import Animal


class Tiger(Animal):
    MONEY_FOR_CARE = 45
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.MONEY_FOR_CARE)