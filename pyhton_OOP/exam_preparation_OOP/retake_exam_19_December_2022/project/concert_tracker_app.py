from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        if musician_type in ["Guitarist", "Drummer", "Singer"]:
            musician = next(filter(lambda n: n.name == name, self.musicians), None)
            if musician:
                raise Exception(f"{name} is already a musician!")
            if musician_type == "Guitarist":
                new = Guitarist(name, age)
                self.musicians.append(new)
                return f"{name} is now a {musician_type}."
            elif musician_type == "Drummer":
                new = Drummer(name, age)
                self.musicians.append(new)
                return f"{name} is now a {musician_type}."
            else:
                new = Singer(name, age)
                self.musicians.append(new)
                return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next(filter(lambda b: b.name == name, self.bands), None)
        if band:
            raise Exception(f"{name} band is already created!")
        new = Band(name)
        self.bands.append(new)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next(filter(lambda c: c.place == place, self.concerts), None)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next(filter(lambda m: m.name == musician_name, self.musicians), None)
        band = next(filter(lambda b: b.name == band_name, self.bands), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next(filter(lambda x: x.name == band_name, self.bands), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda x: x.name == musician_name, band.members), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next(filter(lambda c: c.place == concert_place, self.concerts), None)
        band = next(filter(lambda b: b.name == band_name, self.bands), None)

        singers = [s for s in band.members if isinstance(s, Singer)]
        guitarists = [g for g in band.members if isinstance(g, Guitarist)]
        drummers = [d for d in band.members if isinstance(d, Drummer)]

        if not (singers and guitarists and drummers):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        are_singers_qualified = True
        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    are_singers_qualified = False
            elif concert.genre == "Metal":
                if "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False
            else:
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False

        are_drummers_qualified = True
        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_qualified = False
            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_qualified = False
            else:
                if "play the drums with drum brushes" not in drummer.skills:
                    are_drummers_qualified = False

        are_guitarists_qualified = True
        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    are_guitarists_qualified = False
            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    are_guitarists_qualified = False
            else:
                if "play jazz" not in guitarist.skills:
                    are_guitarists_qualified = False

        if not are_singers_qualified or not are_guitarists_qualified or not are_drummers_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        else:
            profit = (concert.audience * concert.ticket_price) - concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."



