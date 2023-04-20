from project.robot import Robot
# from project1.robot import Robot
from unittest import TestCase, main

class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot('128', 'Military', 100, 10.5)
        self.hardware_upgrades = []
        self.software_updates = []
        self.PRICE_INCREMENT = 1.5

    def test_initialization_correct(self):
        self.assertEqual('128', self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(10.5, self.robot.price)
        self.assertEqual([], self.hardware_upgrades)
        self.assertEqual([], self.software_updates)
        self.assertEqual(1.5, self.PRICE_INCREMENT)

    def test_categories_correct(self):
        self.robot = Robot('128', 'Entertainment', 100, 10.5)
        self.assertEqual("Entertainment", self.robot.category)

    def test_categories_correct2(self):
        self.robot = Robot('128', 'Humanoids', 100, 10.5)
        self.assertEqual("Humanoids", self.robot.category)

    def test_categories_correct3(self):
        self.robot = Robot('128', 'Education', 100, 10.5)
        self.assertEqual("Education", self.robot.category)

    def test_category_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('128', 'Sport', 100, 10.5)
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_returns_an_error_if_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -10
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_correct(self):
        self.hardware_upgrades = []
        self.assertEqual("Robot 128 was upgraded with Memory.", self.robot.upgrade("Memory", 10.5))
        self.assertEqual(26.25, self.robot.price)
        self.assertEqual(["Memory"], self.robot.hardware_upgrades)
        self.assertEqual("Robot 128 was not upgraded.", self.robot.upgrade("Memory", 10.5))

    def test_update_correct(self):
        self.software_updates = []
        self.assertEqual('Robot 128 was updated to version 1.2.', self.robot.update(1.2, 20))
        self.assertEqual([1.2], self.robot.software_updates)
        self.assertEqual(80, self.robot.available_capacity)
        self.assertEqual('Robot 128 was not updated.', self.robot.update(2.4, 90))
        self.robot.update(2.4, 20)
        self.assertEqual('Robot 128 was not updated.', self.robot.update(1.1, 10))

    def test_gt_correct(self):
        self.robot = Robot('128', 'Humanoids', 100, 12)
        self.other = Robot('T100', 'Military', 80, 10)
        expected = 'Robot with ID 128 is more expensive than Robot with ID T100.'
        self.assertEqual(expected, self.robot.__gt__(self.other))

    def test_gt_equal_correct(self):
        self.robot = Robot('128', 'Humanoids', 100, 12)
        self.other = Robot('T100', 'Military', 80, 12)
        expected = 'Robot with ID 128 costs equal to Robot with ID T100.'
        self.assertEqual(expected, self.robot.__gt__(self.other))

    def test_gt_lower_correct(self):
        self.robot = Robot('128', 'Humanoids', 100, 10)
        self.other = Robot('T100', 'Military', 80, 12)
        expected = 'Robot with ID 128 is cheaper than Robot with ID T100.'
        self.assertEqual(expected, self.robot.__gt__(self.other))

if __name__ == "__main__":
    main()

