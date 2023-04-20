from unittest import TestCase, main
from pyhton_OOP.testing.test_list.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList("2", 3, 28, 3.4, False)

    def test_correct_initializing(self):
        self.assertEqual([3, 28], self.integer_list._IntegerList__data)

    def test_correct_get_data(self):
        self.assertEqual([3, 28], self.integer_list.get_data())

    def test_correct_add_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(3.4)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_correct_data_returns_properly(self):
        result = self.integer_list.add(2)
        self.assertEqual(result, [3, 28, 2])
        self.assertEqual(self.integer_list._IntegerList__data, [3, 28, 2])

    def test_remove_index_raises_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_correct_remove_index_removes(self):
        result = self.integer_list.remove_index(1)
        self.assertNotIn(28, self.integer_list._IntegerList__data)
        self.assertEqual(result, 28)

    def test_get_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(3)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_valid_index(self):
        self.assertEqual(28, self.integer_list.get(1))

    def test_insert_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(3, "4")
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, "4")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_works(self):
        self.integer_list.insert(1, 4)
        self.assertEqual([3, 4, 28], self.integer_list._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual(28, self.integer_list.get_biggest())

    def test_get_index_works(self):
        self.assertEqual(1, self.integer_list.get_index(28))

if __name__ == "__main__":
    main()