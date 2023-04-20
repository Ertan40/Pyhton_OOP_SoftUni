class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = []
        result.append(f"Name: {self.name}")   # return f"Name: {self.name}\n" \
        result.append(f"Guild: {self.guild}")        # f"Guild: {self.guild}\n" \
        result.append(f"HP: {self.hp}")              # f"HP: {self.hp}\n" \
        result.append(f"MP: {self.mp}")              # f"MP: {self.mp}\n" + \
        for skill, mana_cost in self.skills.items():  # '\n'.join([f'==={s} - {m}' for s, m in self.skills.items()])
            result.append(f"==={skill} - {mana_cost}")

        return '\n'.join(result)



player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
