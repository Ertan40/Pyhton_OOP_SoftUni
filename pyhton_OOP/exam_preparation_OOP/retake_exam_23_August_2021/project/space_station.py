from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository

class SpaceStation:
    successful_missions = 0
    not_completed_missions = 0
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        # if astronaut_type == "Biologist" or astronaut_type == "Geodesist" or astronaut_type == "Meteorologist":
        #     for astronaut in self.astronaut_repository.astronauts:
        #         if astronaut.name == name:
        #             return f'{name} is already added.'

        if astronaut_type in ["Biologist", "Geodesist", "Meteorologist"]:
            astronaut = self.astronaut_repository.find_by_name(name)
            if astronaut:
                return f"{name} is already added."
            if astronaut_type == "Biologist":
                new_astronaut = Biologist(name)
                self.astronaut_repository.add(new_astronaut)
                return f'Successfully added {astronaut_type}: {name}.'
            elif astronaut_type == "Geodesist":
                new_astronaut = Geodesist(name)
                self.astronaut_repository.add(new_astronaut)
                return f'Successfully added {astronaut_type}: {name}.'
            elif astronaut_type == "Meteorologist":
                new_astronaut = Meteorologist(name)
                self.astronaut_repository.add(new_astronaut)
                return f'Successfully added {astronaut_type}: {name}.'
        else:
            raise Exception('Astronaut type is not valid!')

    def add_planet(self, name: str, items: str):
        current_planet = self.planet_repository.find_by_name(name)
        if current_planet:
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        current_astronaut = self.astronaut_repository.find_by_name(name)
        if not current_astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(current_astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        sorted_astronaut = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
        astronauts_on_mission = []
        for i, astronaut in enumerate(sorted_astronaut, 1):
            if i <= 5 and astronaut.oxygen > 30:
                astronauts_on_mission.append(astronaut)
        if not astronauts_on_mission:
            raise Exception(f'You need at least one astronaut to explore the planet!')
        for i, astronaut in enumerate(astronauts_on_mission, 1):
            while astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if not planet.items:
                    self.successful_missions += 1
                    return f'Planet: {planet_name} was explored. {i} ' \
                           f'astronauts participated in collecting items.'
        self.not_completed_missions += 1
        return f'Mission is not completed.'

    def report(self):
        display_result = [f"{self.successful_missions} successful missions!"]
        display_result.append(f"{self.not_completed_missions} missions were not completed!")
        display_result.append("Astronauts' info:")
        for info in self.astronaut_repository.astronauts:
            display_result.append(f"Name: {info.name}")
            display_result.append(f"Oxygen: {info.oxygen}")
            if info.backpack:
                display_result.append(f"Backpack items: {', '.join(info.backpack)}")
            else:
                display_result.append(f"Backpack items: none")
        return "\n".join(display_result)
