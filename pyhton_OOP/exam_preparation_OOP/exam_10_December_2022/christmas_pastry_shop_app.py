from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def __find_booth(self, booth_number):
        return next(filter(lambda x: x.booth_number == booth_number, self.booths), None)

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy in ["Gingerbread", "Stolen"]:
            for current_name in self.delicacies:
                if current_name.name == name:
                    raise Exception(f"{name} already exists!")

            if type_delicacy == "Gingerbread":
                new = Gingerbread(name, price)
                self.delicacies.append(new)
                return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
            elif type_delicacy == "Stolen":
                new = Stolen(name, price)
                self.delicacies.append(new)
                return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        if self.__find_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if not self.__find_booth(booth_number):
            if type_booth == "Open Booth":
                new = OpenBooth(booth_number, capacity)
                self.booths.append(new)
                return f"Added booth number {booth_number} in the pastry shop."
            elif type_booth == "Private Booth":
                new = PrivateBooth(booth_number, capacity)
                self.booths.append(new)
                return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")
        # try:
        #     booth = next(filter(lambda x: x.capacity >= number_of_people and not x.is_reserved, self.booths))
        # except StopIteration:
        #     raise Exception(f"No available booth for {number_of_people} people!")
        # booth.reserve(number_of_people)
        # return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth = self.__find_booth(booth_number)
        delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies), None)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth(booth_number)
        bill = sum(b.price for b in booth.delicacy_orders) + booth.price_for_reservation
        booth.price_for_reservation = 0
        booth.is_reserved = False
        booth.delicacy_orders.clear()  # booth.delicacy_orders = []
        self.income += bill
        return f"Booth {booth.booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
