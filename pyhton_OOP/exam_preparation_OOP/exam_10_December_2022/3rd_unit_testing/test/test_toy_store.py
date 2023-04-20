from project.toy_store import ToyStore
from unittest import TestCase, main
# from project1.toy_store import ToyStore

class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toystore = ToyStore()

    def test_initialization_correct(self):
        self.toystore.toy_shelf = {"A": None, "B": None, "C": None, "D": None,
            "E": None,
            "F": None,
            "G": None,
                          }
        # for key in range(ord("A") + ord("G") + 1):
        #     self.assertIsNone(self.toystore.toy_shelf[chr(key)])
        # self.assertEqual(7, len(self.toystore.toy_shelf))
        self.assertEqual(self.toystore.toy_shelf["A"], None)
        self.assertEqual(self.toystore.toy_shelf["B"], None)
        self.assertEqual(self.toystore.toy_shelf["C"], None)
        self.assertEqual(self.toystore.toy_shelf["D"], None)
        self.assertEqual(self.toystore.toy_shelf["E"], None)
        self.assertEqual(self.toystore.toy_shelf["F"], None)
        self.assertEqual(self.toystore.toy_shelf["G"], None)

    def test_add_toy_raises_an_error_if_not_in(self):
        self.toystore.toy_shelf = {"A": None, "B": None, "C": None, "D": None,
                          "E": None,
                          "F": None,
                          "G": None,
                          }
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("K", "Pepi")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_raises_an_error_if_toy_in_shelf(self):
        self.toystore.add_toy("D", "Pepi")
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("D", "Pepi")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual("Pepi", self.toystore.toy_shelf["D"])

    def test_add_toy_raises_exception_if_shelf_is_not_None(self):
        self.toystore.add_toy("D", "Pepi")
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("D", "Kiki")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_correct(self):
        actual = self.toystore.add_toy("D", "Pepi")
        self.assertEqual("Toy:Pepi placed successfully!", actual)
        self.assertEqual("Pepi", self.toystore.toy_shelf["D"])

    def test_remove_toy_raises_an_error(self):
        self.toystore.add_toy("D", "Pepi")
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("K", "Jimi")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_raises_an_error_if_not_in_shelf(self):
        self.toystore.add_toy("D", "Pepi")
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("D", "Jimi")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_correct(self):
        self.toystore.add_toy("D", "Pepi")
        self.assertEqual("Remove toy:Pepi successfully!", self.toystore.remove_toy("D", "Pepi"))
        self.assertEqual(None, self.toystore.toy_shelf["D"])

if __name__ == "__main__":
    main()