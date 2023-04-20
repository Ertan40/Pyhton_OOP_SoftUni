from pyhton_OOP.inheritance.zoo.project.reptile import Reptile
# from project.reptile import Reptile


class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)