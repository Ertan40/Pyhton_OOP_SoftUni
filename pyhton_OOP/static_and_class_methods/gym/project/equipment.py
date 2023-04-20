class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.id  # __class__.id
        Equipment.id += 1       # __class__.id

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"