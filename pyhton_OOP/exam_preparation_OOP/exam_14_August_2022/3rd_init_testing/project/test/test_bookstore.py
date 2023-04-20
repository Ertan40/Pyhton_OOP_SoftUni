# from project.bookstore import Bookstore
from unittest import TestCase, main
from project1.project.bookstore import Bookstore
# --------------------------- score = 93 ---------------------------

class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(20)

    def test_initialization_correct(self):
        self.assertEqual(20, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)  # Dict[str, int] = {}
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_total_sold_books_correct(self):
        self.bookstore._Bookstore__total_sold_books = 2
        self.assertEqual(2, self.bookstore._Bookstore__total_sold_books)

    def test_setter_books_limit_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_len_correct(self):
        self.bookstore.count_books = 0
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 2, "King": 1}
        self.assertEqual(3, self.bookstore.__len__())

    def test_receive_book_raises_an_error(self):
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 20, "King": 10}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Dune", 32)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_and_book_title_not_in(self):
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 10, "King": 5}
        self.bookstore.receive_book("Rocky", 2)
        self.bookstore.receive_book("King", 1)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles["Rocky"])
        self.assertEqual(6, self.bookstore.availability_in_store_by_book_titles["King"])
        expected = "7 copies of King are available in the bookstore."
        self.assertEqual(expected, self.bookstore.receive_book("King", 1))

    def test_sell_book_raises_an_error_if_not_available(self):
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 10, "King": 5}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Rocky", 1)
        self.assertEqual("Book Rocky doesn't exist!", str(ex.exception))

    def test_sell_book_raises_an_error_if_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 10, "King": 5}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("King", 8)
        self.bookstore.books_left = self.bookstore.availability_in_store_by_book_titles["King"]
        expected = f"King has not enough copies to sell. Left: {self.bookstore.books_left}"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["King"])

    def test_sell_book_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 10, "King": 5}
        expected = "Sold 4 copies of Dune"
        self.assertEqual(expected, self.bookstore.sell_book("Dune", 4))
        self.assertEqual(6, self.bookstore.availability_in_store_by_book_titles["Dune"])
        self.assertEqual(4, self.bookstore.total_sold_books)

    def test_str_correct(self):
        self.bookstore.availability_in_store_by_book_titles = {"Dune": 10, "King": 5}
        self.bookstore.sell_book("Dune", 4)
        expected = f"Total sold books: 4\n" \
                   f'Current availability: 11\n' \
                   f" - Dune: 6 copies\n" \
                   f" - King: 5 copies"
        self.assertEqual(expected, self.bookstore.__str__())

if __name__ == "__main__":
    main()


