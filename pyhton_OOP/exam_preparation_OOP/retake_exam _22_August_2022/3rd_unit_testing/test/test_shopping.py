from project.shopping_cart import ShoppingCart
from unittest import TestCase, main
# from project1.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Mimi", 200)


    def test_initialization(self):
        self.assertEqual("Mimi", self.shopping_cart.shop_name)
        self.assertEqual(200, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_setter_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "kiki9"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Choco", 100)
        self.assertEqual("Product Choco cost too much!", str(ve.exception))

    def test_add_to_cart_correct(self):
        self.shopping_cart.add_to_cart("Choco", 20.0)
        self.assertEqual({"Choco": 20.0}, self.shopping_cart.products)
        expected = "Cola product was successfully added to the cart!"
        self.assertEqual(expected, self.shopping_cart.add_to_cart("Cola", 2.8))

    def test_remove_from_cart_raises_an_error(self):
        self.shopping_cart.products = {"Cola": 2.8}
        self.shopping_cart.add_to_cart("Choco", 20.0)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Honey")
        self.assertEqual("No product with name Honey in the cart!", str(ve.exception))
        actual = self.shopping_cart.remove_from_cart("Cola")
        self.assertEqual({'Choco': 20.0}, self.shopping_cart.products)
        self.assertEqual("Product Cola was successfully removed from the cart!", actual)

    def test_add_correct(self):
        self.other = ShoppingCart("Kiki", 300)
        self.other.products = {"Choco": 1.8}
        self.shopping_cart.products = {"Cola": 2.8}
        new_shop = self.shopping_cart.__add__(self.other)
        self.assertEqual("MimiKiki", new_shop.shop_name)
        self.assertEqual(500, new_shop.budget)
        self.assertEqual({"Choco": 1.8, "Cola": 2.8}, new_shop.products)

    def test_buy_products_raises_an_error(self):
        self.shopping_cart.products = {"Choco": 10.8, "Cola": 20.8}
        self.shopping_cart.budget = 20
        self.shopping_cart.total_sum = sum(self.shopping_cart.products.values())
        self.assertEqual(31.6, sum(self.shopping_cart.products.values()))
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        expected = f"Not enough money to buy the products! Over budget with {self.shopping_cart.total_sum - self.shopping_cart.budget:.2f}lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_returns_correct(self):
        self.shopping_cart.products = {"Choco": 10.8, "Cola": 20.8}
        self.shopping_cart.budget = 100
        self.shopping_cart.total_sum = sum(self.shopping_cart.products.values())
        self.assertEqual(31.6, sum(self.shopping_cart.products.values()))
        expected = f'Products were successfully bought! Total cost: {self.shopping_cart.total_sum:.2f}lv.'
        self.assertEqual(expected, self.shopping_cart.buy_products())


if __name__ == "__main__":
    main()