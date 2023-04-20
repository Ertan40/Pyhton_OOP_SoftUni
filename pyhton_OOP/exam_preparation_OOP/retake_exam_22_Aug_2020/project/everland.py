from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = [] #  an empty list that will contain all rooms (objects)

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for expense in self.rooms:
            total_consumption += expense.expenses
            total_consumption += expense.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        output, rooms_to_remove = [], []
        for room in self.rooms:
            if room.room_cost + room.expenses > room.budget:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(self.rooms.index(room))
                continue
            total_expenses = room.expenses+room.room_cost
            room.budget -= total_expenses
            output.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
        if rooms_to_remove:
            for _ in range(len(self.rooms) - 1, -1, -1):
                self.rooms.pop(rooms_to_remove.pop())
        return "\n".join(output)

    def status(self):
        output = []
        total_count = 0
        for room in self.rooms:
            total_count += room.members_count
        output.append(f"Total population: {total_count}")
        for room in self.rooms:
            output.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            for kid, info in enumerate(room.children, 1):
                output.append(f"--- Child {kid} monthly cost: {info.get_monthly_expense():.2f}$")
            output.append(f"--- Appliances monthly cost: {sum(r.get_monthly_expense() for r in room.appliances):.2f}$")

        return "\n".join(output)

# everland = Everland()
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
# if __name__ == "__main__":
#     test_one()