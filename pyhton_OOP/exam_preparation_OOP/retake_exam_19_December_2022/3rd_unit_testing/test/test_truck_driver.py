from project.truck_driver import TruckDriver
from unittest import TestCase, main
# from project1.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Joni", 100)

    def test_initialization_correct(self):
        self.assertEqual("Joni", self.truck_driver.name)
        self.assertEqual(100, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)  # Dict[str, int] = {}
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -10
        self.assertEqual("Joni went bankrupt.", str(ve.exception))

    def test_add_cargo_raises_an_error(self):
        self.truck_driver.add_cargo_offer("Italy", 100)
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Italy", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.truck_driver.add_cargo_offer("BG", 200)
        self.assertEqual(200, self.truck_driver.available_cargos["BG"])
        expected = "Cargo for 300 to TR was added as an offer."
        self.assertEqual(expected, self.truck_driver.add_cargo_offer("TR", 300))

    def test_drive_best_cargo_offer_returns_correct(self):
        self.truck_driver.available_cargos = {}
        self.assertEqual("There are no offers available.", self.truck_driver.drive_best_cargo_offer())

    def test_drive_best_cargo_correct(self):
        self.truck_driver.money_per_mile = 1
        self.truck_driver.earned_money = 0
        self.truck_driver.miles = 0
        self.truck_driver.available_cargos = {"Italy": 100, "BG": 200, "TR": 300}
        self.truck_driver.cargo_location = max(self.truck_driver.available_cargos, key=self.truck_driver.available_cargos.get)
        self.assertEqual("TR", self.truck_driver.cargo_location)
        self.assertEqual(300, self.truck_driver.available_cargos["TR"])
        self.assertEqual("Joni is driving 300 to TR.", self.truck_driver.drive_best_cargo_offer())
        self.assertEqual(300, self.truck_driver.miles)
        self.assertEqual(280, self.truck_driver.earned_money)

    def test_check_for_activities_with_eat(self):
        self.truck_driver.add_cargo_offer("London", 250)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(24980, self.truck_driver.earned_money)

    def test_check_for_activities_with_sleep(self):
        self.truck_driver.add_cargo_offer("Milano", 1000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(99875, self.truck_driver.earned_money)

    def test_check_for_activities_with_pump_gas(self):
        self.truck_driver.add_cargo_offer("Milano", 1500)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(149335, self.truck_driver.earned_money)

    def test_check_for_activities_with_repair_truck(self):
        self.truck_driver.add_cargo_offer("Milano", 10000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(988250, self.truck_driver.earned_money)

    def test_repr_correct(self):
        self.truck_driver.add_cargo_offer("Milano", 10000)
        expected = f"{self.truck_driver.name} has {self.truck_driver.miles} miles behind his back."
        self.assertEqual(expected, self.truck_driver.__repr__())

if __name__ == "__main__":
    main()
