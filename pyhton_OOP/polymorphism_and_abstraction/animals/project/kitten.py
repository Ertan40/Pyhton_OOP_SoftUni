from pyhton_OOP.polymorphism_and_abstraction.animals.project.cat import Cat
# from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)


    def make_sound(self):
        return "Meow"