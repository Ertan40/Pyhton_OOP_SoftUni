from project.pet_shop import PetShop
from unittest import TestCase, main
# from area_test.project.pet_shop import PetShop
# ______________________ score = 94 __________________

class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop("Mimi")

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Mimi", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_adds_correct(self):
        self.pet_shop.add_food("Kiki", 1.6)
        self.assertEqual({"Kiki": 1.6}, self.pet_shop.food)
        expected = "Successfully added 1.60 grams of Kiki."
        self.assertEqual(expected, self.pet_shop.add_food("Kiki", 1.6))

    def test_add_pet_raises_an_error(self):
        self.pet_shop.pets = ["Mimi", "Kiki"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Kiki")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_adds_if_not_in(self):
        self.pet_shop.pets = ["Mimi", "Kiki"]
        self.pet_shop.add_pet("Fifi")
        self.assertEqual(["Mimi", "Kiki", "Fifi"], self.pet_shop.pets)
        expected = "Successfully added Pepi."
        self.assertEqual(expected, self.pet_shop.add_pet("Pepi"))

    def test_feed_pet_raises_an_error(self):
        self.pet_shop.pets = ["Mimi", "Kiki"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("m", "Bobi")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_name_not_in_correct(self):
        self.pet_shop.food = {"A": 1.6, "B": 2}
        self.pet_shop.pets = ["Mimi", "Kiki"]
        expected = 'You do not have C'
        self.assertEqual(expected, self.pet_shop.feed_pet("C", "Mimi"))

    def test_feed_pet_if_below_quantity_correct(self):
        self.pet_shop.food = {"A": 1.6, "B": 2}
        self.pet_shop.pets = ["Mimi", "Kiki"]
        self.pet_shop.add_food("Kiki", 10)
        self.assertEqual("Adding food...", self.pet_shop.feed_pet("A", "Mimi"))

    def test_feed_pet_reduces(self):
        self.pet_shop.food = {"A": 1.6, "B": 2}
        self.pet_shop.pets = ["Mimi", "Kiki"]
        self.pet_shop.add_food("Kiki", 10)
        self.pet_shop.feed_pet("A", "Kiki")
        self.assertEqual(1001.6, self.pet_shop.food["A"])
        self.assertEqual("Kiki was successfully fed", self.pet_shop.feed_pet("A", "Kiki"))

    def test_repr_correct(self):
        expected = f'Shop Mimi:\n' \
                   f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected, self.pet_shop.__repr__())
    # def test_repr(self):
    #     self.pet_shop.add_pet("Tom")
    #     self.pet_shop.add_pet("Bom")
    #     expected = "Shop Mimi:\n" \
    #                "Pets: Tom, Bom"
    #     self.assertEqual(expected, str(self.pet_shop))

if __name__ == "__main__":
    main()
