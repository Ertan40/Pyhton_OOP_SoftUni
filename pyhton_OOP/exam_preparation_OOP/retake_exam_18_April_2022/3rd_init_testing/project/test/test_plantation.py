from project.plantation import Plantation
from unittest import TestCase, main
# from project1.project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plant = Plantation(2)

    def test_initialization_correct(self):
        self.assertEqual(2, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_size_setter_correct(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.size = -10
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_correct(self):
        self.assertEqual("Mimi successfully hired.", self.plant.hire_worker("Mimi"))
        self.assertEqual(["Mimi"], self.plant.workers)


    def test_hire_worker_raises_an_error_if_already_exists(self):
        self.plant.workers = ["Mimi"]
        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker("Mimi")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_len_correct(self):
        self.plant.count_of_plants = 0
        self.plant.plants = {"Rose": ["Rose"], "Papa": ["Orkide"]}
        self.assertEqual(2, self.plant.__len__())

    def test_planting_error_raises_if_worker_not_in(self):
        self.plant.workers = ["Mimi"]
        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Pepi", "Rose")
        self.assertEqual("Worker with name Pepi is not hired!", str(ve.exception))

    def test_planting_with_no_capacity(self):
        self.plant.size = 2
        self.plant.hire_worker("Pepi")
        self.plant.planting("Pepi", "tree")
        self.plant.planting("Pepi", "tree")
        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Pepi", "tree")
        expected = f'The plantation is full!'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'Pepi': ['tree', 'tree']}, self.plant.plants)

    def test_planting_if_worker_in_correct(self):
        self.plant.workers = ["Mimi", "Pepi"]
        self.plant.plants = {"Mimi": []}
        self.assertEqual("Mimi planted Rose.", self.plant.planting("Mimi", "Rose"))
        self.assertEqual(["Rose"], self.plant.plants["Mimi"])

    def test_planting_if_worker_plants_for_first_time_correct(self):
        self.plant.workers = ["Pepi", "Kiki"]
        self.plant.hire_worker("Mimi")
        self.assertEqual(['Pepi', 'Kiki', 'Mimi'], self.plant.workers)
        self.assertEqual("Mimi planted it's first Rose.", self.plant.planting("Mimi", "Rose"))

    def test_str_correct(self):
        self.plant.workers = ["Pepi", "Kiki"]
        self.plant.plants = {"Pepi": ["Rose", "Papatya"], "Kiki": ["Orkide"]}
        expected = "Plantation size: 2\n" \
                   f'{", ".join(self.plant.workers)}\n' \
                   f"Pepi planted: Rose, Papatya\n" \
                    "Kiki planted: Orkide"
        self.assertEqual(expected, self.plant.__str__())

    def test_repr_correct(self):
        self.plant.workers = ["Pepi", "Kiki"]
        expected = 'Size: 2\n' \
                   'Workers: Pepi, Kiki'
        self.assertEqual(expected, self.plant.__repr__())


if __name__ == "__main__":
    main()
