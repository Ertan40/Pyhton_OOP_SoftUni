from pyhton_OOP.static_and_class_methods.hotel_rooms.project.room import Room
# from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result:
                    return result
                self.guests += people
                # if not isinstance(room.take_room(people), str):
                #     self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            guests = room.guests
            if room.number == room_number:
                result = room.free_room()
                if result:
                    return result
                self.guests -= guests
                # guests = room.free_room()
                # if not isinstance(guests, str):
                #     self.guests -= guests

    def status(self):
        free_rooms = [f.number for f in self.rooms if not f.is_taken]
        taken_rooms = [t.number for t in self.rooms if t.is_taken]
        output = [f"Hotel {self.name} has {self.guests} total guests"]
        output.append(f"Free rooms: {', '.join(str(r) for r in free_rooms)}")
        output.append(f"Taken rooms: {', '.join(str(r) for r in taken_rooms)}")

        return '\n'.join(output)


# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())