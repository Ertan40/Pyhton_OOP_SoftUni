from pyhton_OOP.polymorphism_and_abstraction.animals.project.cat import Cat
# from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)


    def make_sound(self):
        return "Hiss"


# dog = Dog("Rocky", 3, "Male")
# print(dog.make_sound())
# print(dog)
# tomcat = Tomcat("Tom", 6)
# print(tomcat.make_sound())
# print(tomcat)
#
# kitten = Kitten("Kiki", 1)
# print(kitten.make_sound())
# print(kitten)
# cat = Cat("Johnny", 7, "Male")
# print(cat.make_sound())
# print(cat)