from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_supply(self, type_of_supply):
        found_supply = None
        index = None
        for i, supply in enumerate(self.supplies[::-1]):
            if supply.__class__.__name__ == type_of_supply:
                found_supply = supply
                index = -(i + 1)
                break
        if found_supply:
            self.supplies.pop(index)
        return found_supply

    def __find_player(self, player_name):
        return next(filter(lambda x: x.name == player_name, self.players), None)

    def add_player(self, *players: Player):
        player_names = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                player_names.append(player.name)
        return f"Successfully added: {', '.join(x for x in player_names)}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ["Food", "Drink"]:
            return

        player = self.__find_player(player_name)
        if player.stamina == 100:
            return f"{player_name} have enough stamina."
        if sustenance_type in ["Food", "Drink"]:
            supply = self.__find_supply(sustenance_type)
            if not supply:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f'{player_name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)
        if not first_player.stamina and not second_player.stamina:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."
        if not first_player.stamina:
            return f"Player {first_player.name} does not have enough stamina."
        if not second_player.stamina:
            return f"Player {second_player.name} does not have enough stamina."

        sort_players_by_stamina = [x for x in sorted([first_player, second_player], key=lambda x: x.stamina)]
        first_player_attack, second_player_attack = sort_players_by_stamina[0], sort_players_by_stamina[1]

        if second_player_attack.stamina - (first_player_attack.stamina / 2) <= 0:
            second_player_attack.stamina = 0
            return f"Winner: {first_player_attack.name}"
        else:
            second_player_attack.stamina -= first_player_attack.stamina / 2

        if first_player_attack.stamina - (second_player_attack.stamina / 2) <= 0:
            first_player_attack.stamina = 0
            return f"Winner: {second_player_attack.name}"
        else:
            first_player_attack.stamina -= second_player_attack.stamina / 2

        player_with_more_stamina = [x for x in sorted(sort_players_by_stamina, key=lambda x: -x.stamina)][0]
        return f"Winner: {player_with_more_stamina.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
                # self.sustain(player.name, "Food")
                # self.sustain(player.name, "Drink")
        for player in self.players:
            for food in ["Food", "Drink"]:
                self.sustain(player.name, food)

    def __str__(self):
        output = []
        for player in self.players:
            output.append(str(player))
        for supply in self.supplies:
            output.append(supply.details())

        return "\n".join(output)