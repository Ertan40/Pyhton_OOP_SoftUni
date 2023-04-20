# from project1.library import Library
from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Mimi")

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_valid(self):
        self.library.name = "Mimi"
        self.assertEqual("Mimi", self.library.name)

    def test_name_setter_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_if_author_not_in(self):
        self.library.books_by_authors = {"Mimi": "A", "Kiki": "B"}
        self.library.add_book("Pepi", "C")
        self.assertEqual(["C"], self.library.books_by_authors["Pepi"])

    def test_add_book_if_title_not_in(self):
        self.library.add_book("Mimi", "D")
        self.library.books_by_authors["Mimi"].append("K")
        self.assertEqual(["D", "K"], self.library.books_by_authors["Mimi"])

    def test_add_reader_if_name_not_in(self):
        self.library.readers = {"Mimi": "A", "Pepi": "B"}
        self.library.add_reader("Kiki")
        self.assertEqual([], self.library.readers["Kiki"])

    def test_add_reader_returns_correct(self):
        self.library.readers = {"Mimi": "A", "Pepi": "B"}
        expected = "Mimi is already registered in the Mimi library."
        self.assertEqual(expected, self.library.add_reader("Mimi"))

    def test_rent_book_reader_name_not_in(self):
        self.library.readers = {"Mimi": "A", "Kiki": "B"}
        self.library.books_by_authors = {"Joni": "C", "Moni": "D"}
        expected = "Pepi is not registered in the Mimi Library."
        self.assertEqual(expected, self.library.rent_book("Pepi", "Joni", "C"))

    def test_rent_book_author_name_not_in(self):
        self.library.readers = {"Mimi": "A", "Kiki": "B"}
        self.library.books_by_authors = {"Joni": "C", "Moni": "D"}
        expected = "Mimi Library does not have any Gabi's books."
        self.assertEqual(expected, self.library.rent_book("Mimi", "Gabi", "C"))

    def test_rent_book_book_title_not_in(self):
        self.library.readers = {"Mimi": "A", "Kiki": "B"}
        self.library.books_by_authors = {"Joni": "C", "Moni": "D"}
        expected = f"""Mimi Library does not have Joni's "Key"."""
        self.assertEqual(expected, self.library.rent_book("Mimi", "Joni", "Key"))

    def test_rent_book_correct(self):
        self.library.add_book("Mimi", "A")
        self.assertEqual({"Mimi": ["A"]}, self.library.books_by_authors)
        self.library.add_reader("Pepi")
        self.assertEqual([], self.library.readers["Pepi"])
        self.library.rent_book("Pepi", "Mimi", "A")
        self.assertEqual({'Pepi': [{'Mimi': 'A'}]}, self.library.readers)
        self.assertEqual({'Mimi': []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
