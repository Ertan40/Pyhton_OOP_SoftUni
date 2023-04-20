from pyhton_OOP.inheritance.zoo.project.lizard import Lizard
from pyhton_OOP.inheritance.zoo.project.mammal import Mammal
from pyhton_OOP.inheritance.zoo.project.reptile import Reptile
# from project.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)