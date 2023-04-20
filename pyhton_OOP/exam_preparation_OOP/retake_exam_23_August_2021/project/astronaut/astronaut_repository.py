from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []


    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)
        # if astronaut not in self.astronauts:
        #     self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)
        # if astronaut in self.astronauts:
        #     self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = next(filter(lambda x: x.name == name, self.astronauts), None)
        return astronaut
        # return astronaut
        # for astronaut in self.astronauts:
        #     if astronaut.name == name:
        #         return astronaut


