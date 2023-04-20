from unittest import TestCase, main

from pyhton_OOP.testing.car_manager.project.car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "5", 1, 4)

    def test_correct_initializing(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("5", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(4, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_returns(self):
        self.car.make = "BMW"
        self.assertEqual("BMW", self.car.make)

    def test_no_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_increases_the_fuel(self):
        self.car.refuel(self.car.fuel_capacity + 20)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_raises_exception(self):
        self.car.fuel_amount = 4
        with self.assertRaises(Exception) as ex:
            self.car.drive(2000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_decreases_from_fuel(self):
        self.car.fuel_amount = 20
        self.car.drive(100)
        self.assertEqual(19, self.car.fuel_amount)

if __name__ == "__main__":
    main()