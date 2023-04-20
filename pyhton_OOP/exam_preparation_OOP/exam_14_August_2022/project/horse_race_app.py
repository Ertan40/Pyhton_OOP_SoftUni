from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_horse(self, horse_type):
        found_horse = None
        for i in range(len(self.horses) - 1, -1, -1):
            if self.horses[i].__class__.__name__ == horse_type and self.horses[i].is_taken == False:
                found_horse = self.horses[i]
                break
        return found_horse
        # return next(filter(lambda x: (type(x).__name__ == horse_type_ and not x.is_taken), \
        # reversed(self.horses)), None)
    def find_jockey(self, jockey_name):
        return next(filter(lambda x: x.name == jockey_name, self.jockeys), None)

    def find_race(self, race_type):
        return next(filter(lambda x: x.race_type == race_type, self.horse_races), None)

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.find_horse(horse_type)
        jockey = self.find_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            horse.is_taken = True
            jockey.horse = horse
            return f"Jockey {jockey_name} will ride the horse {horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.find_jockey(jockey_name)
        race = self.find_race(race_type)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        else:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        current_race = None
        for race in self.horse_races:
            if race.race_type == race_type:
                current_race = race
        if not current_race:
            raise Exception(f'Race {race_type} could not be found!')
        if len(current_race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')
        high_speed = 0
        winner = None
        for jockey in current_race.jockeys:
            if jockey.horse.speed > high_speed:
                high_speed = jockey.horse.speed
                winner = jockey
        return f"The winner of the {race_type} race, with a speed of {high_speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."
