from unittest import TestCase, main
# from area_test.project.train.train import Train
from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.train = Train("Mimi", 10)

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_class_values(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_raises_value_error_if_no_capacity(self):
        self.train.passengers = ["a", "b", "c", "4", "5", "6", "7", "8", "9", "10"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Fifi")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_raises_value_error_if_passenger_in(self):
        self.train.passengers = ["Mimi", "b", "c", "4", "5", "6"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Mimi")
        self.assertEqual("Passenger Mimi Exists", str(ve.exception))

    def test_add_correct(self):
        self.train.passengers = ["Mimi", "b", "c", "4"]
        self.train.add("Kiki")
        self.assertEqual(["Mimi", "b", "c", "4", "Kiki"], self.train.passengers)

    def test_add_returns_correct(self):
        self.train.passengers = ["Mimi", "b", "c", "4"]
        self.train.add("Kiki")
        self.assertEqual("Added passenger Kiki", self.train.PASSENGER_ADD.format("Kiki"))

    def test_remove_raises_error_if_not_in(self):
        self.train.passengers = ["Mimi", "b", "c", "4"]
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Kim")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_correct(self):
        self.train.passengers = ["Mimi", "b", "c", "4"]
        self.train.remove("Mimi")
        self.assertEqual(["b", "c", "4"], self.train.passengers)

    def test_remove_returns_correct(self):
        self.train.passengers = ["Mimi", "b", "c", "4"]
        self.train.remove("Mimi")
        self.assertEqual("Removed Mimi", self.train.PASSENGER_REMOVED.format("Mimi"))


if __name__ == "__main__":
    main()