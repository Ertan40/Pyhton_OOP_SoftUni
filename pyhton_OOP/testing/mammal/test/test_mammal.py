from unittest import TestCase, main
# from pyhton_OOP.testing.mammal.project.mammal import Mammal
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Joe", "delphin", "mimi")

    def test_initialization(self):
        self.assertEqual("Joe", self.mammal.name)
        self.assertEqual("delphin", self.mammal.type)
        self.assertEqual("mimi", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_correct(self):
        self.assertEqual("Joe makes mimi", self.mammal.make_sound())

    def test_get_kingdom_correct(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_correct(self):
        self.assertEqual("Joe is of type delphin", self.mammal.info())


if __name__ == "__main__":
    main()