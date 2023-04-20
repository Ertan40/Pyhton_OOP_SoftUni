from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []  # contain all the decorations (objects)
        self.fish = []   # contain all the fish (objects)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        fish_type = type(fish).__name__   # fish_type = fish.__class__.__name__
        if fish_type in ["FreshwaterFish", "SaltwaterFish"]:
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = [f"{self.name}:"]
        if self.fish:
            output.append(f"Fish: {' '.join(f.name for f in self.fish)}")
        else:
            output.append(f"Fish: none")
        output.append(f"Decorations: {len(self.decorations)}")
        output.append(f"Comfort: {self.calculate_comfort()}")
        return "\n".join(output)


