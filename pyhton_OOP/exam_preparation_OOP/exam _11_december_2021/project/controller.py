from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_driver(self, name):
        return next(filter(lambda x: x.name == name, self.drivers), None)

    def __find_race(self, name):
        return next(filter(lambda x: x.name == name, self.races), None)

    def __find_car(self, car_type):
        found_car = None
        for i in range(len(self.cars) -1, -1, -1):
            car = self.cars[i]
            if type(car).__name__ == car_type and not car.is_taken:
                found_car = car
                break
        return found_car

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ["MuscleCar", "SportsCar"]:
            return

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new = MuscleCar(model, speed_limit)
            self.cars.append(new)
            return f"{car_type} {model} is created."
        elif car_type == "SportsCar":
            new = SportsCar(model, speed_limit)
            self.cars.append(new)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.__find_driver(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        new = Driver(driver_name)
        self.drivers.append(new)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.__find_race(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")
        new = Race(race_name)
        self.races.append(new)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type in ["MuscleCar", "SportsCar"]:
            car = self.__find_car(car_type)
            if not car:
                raise Exception(f"Car {car_type} could not be found!")
            if driver.car is not None:
                old_car = driver.car
                old_car.is_taken = False
                car.is_taken = True
                driver.car = car
                return f"Driver {driver.name} changed his car from {old_car.model} to {driver.car.model}."
            else:
                driver.car = car
                car.is_taken = True
                return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        driver = self.__find_driver(driver_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        for race1 in self.races:
            if driver in race.drivers:
                return f"Driver {driver_name} is already added in {race1.name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        sorted_drivers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        output = []
        for i, driver in enumerate(sorted_drivers, 1):
            if i <= 3:
                output.append(f"Driver {driver.name} wins the {race_name} "
                              f"race with a speed of {driver.car.speed_limit}.")
                driver.number_of_wins += 1
        return "\n".join(output)
