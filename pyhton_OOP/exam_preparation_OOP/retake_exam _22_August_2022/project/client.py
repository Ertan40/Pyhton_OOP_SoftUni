class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.ordered_quantities = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.startswith("0") or not value.isnumeric() or len(value) != 10:
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

        # if value[0] == "0" and len(value) == 10 and value.isdigit():
        #     self.__phone_number = value
        # raise ValueError("Invalid phone number!")


        # if value[0] != "0" or len(value) != 10 or not value.isnumeric():
        #     raise ValueError('Invalid phone number!')
        # self.__phone_number = value


