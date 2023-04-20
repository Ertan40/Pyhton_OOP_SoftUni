class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Ertan", 1500, 100)

    def test_correct_initializing(self):
        self.assertEqual("Ertan", self.worker.name)
        self.assertEqual(1500, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method_for_energy(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_work_method_for_money(self):
        self.worker.work()
        self.assertEqual(1500, self.worker.money)

    def test_whether_rest_method_works(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_whether_error_raises_after_zero_is_given(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_whether_error_raises_after_negative_is_given(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_get_correct_info(self):
        self.worker.get_info()
        self.assertEqual("Ertan has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    unittest.main()