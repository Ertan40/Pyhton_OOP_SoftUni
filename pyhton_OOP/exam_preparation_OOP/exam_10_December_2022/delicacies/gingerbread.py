from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    # @property
    # def get_portion(self):
    #     return 200
    # PORTION = 200
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)


    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
