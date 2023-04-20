class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        output = []
        output.append(f"Player: {self.__name}")
        output.append(f"Sprint: {self.__sprint}")
        output.append(f"Dribble: {self.__dribble}")
        output.append(f"Passing: {self.__passing}")
        output.append(f"Shooting: {self.__shooting}")
        # output = [f"Player: {self.name}", f"Sprint: {self.__sprint}", f"Dribble: {self.__dribble}",
        #           f"Passing: {self.__passing}", f"Shooting: {self.__shooting}"]
        return "\n".join(output)
        # return f"Player: {self.__name}\n" \
        #                  f"Sprint: {self.__sprint}\n" \
        # #                f"Dribble: {self.__dribble}\n" \
        # #                f"Passing: {self.__passing}\n" \
        # #                f"Shooting: {self.__shooting}\n"