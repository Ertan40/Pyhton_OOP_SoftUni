from unittest import TestCase, main
# from pyhton_OOP.testing.vehicle.project.vehicle import Vehicle
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(6.5, 19.3)

    def test_initialization_correct(self):
        self.assertEqual(6.5, self.vehicle.fuel)
        self.assertEqual(19.3, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correct(self):
        self.vehicle.fuel = 20
        self.vehicle.drive(10)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_refuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(12)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_fuel(self):
        self.vehicle.fuel = 3
        self.vehicle.refuel(3)
        self.assertEqual(6, self.vehicle.fuel)

    def test_str_correct(self):
        self.assertEqual("The vehicle has 19.3 horse power with 6.5 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()