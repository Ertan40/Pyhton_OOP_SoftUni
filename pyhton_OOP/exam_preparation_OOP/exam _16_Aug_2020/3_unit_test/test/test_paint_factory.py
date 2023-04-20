from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Jumbo", 100)

    def test_initialization_correct(self):
        self.assertEqual("Jumbo", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.products)

    def test_add_ingredient_not_enough_space(self):
        self.factory.capacity = 0
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("white", 10)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_different_type_raises_an_error(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("black", 1)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(te.exception))
        # expected = f"Ingredient of type bomba not allowed in {self.factory.__class__.__name__}"

    def test_add_ingredient_adds_if_enough_quantity(self):
        expected = {"white": 2}
        self.factory.add_ingredient("white", 2)
        self.assertEqual(expected, self.factory.ingredients)

    def test_remove_ingredient_raises_error_quantity_below_zero(self):
        self.factory.add_ingredient("white", 1)
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("white", 2)
        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_ingredient_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("banana", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_decreases_quantity(self):
        self.factory.add_ingredient("white", 10)
        self.factory.remove_ingredient("white", 5)
        self.assertEqual(5, self.factory.products["white"])

    # def test_successful_remove_quantity_from_ingredient(self):
    #     self.factory.add_ingredient("red", 1)
    #     self.factory.remove_ingredient("red", 1)
    #     self.assertEqual({"red": 0}, self.factory.ingredients)

if __name__ == "__main__":
    main()