class DecorationRepository:
    def __init__(self):
        self.decorations = [] # contain all decorations (objects)

    def add(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)


    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if type(decoration).__name__ == decoration_type:
                return decoration
        return "None"
        # decoration = [d for d in self.decorations if d.__class__.__name__ == decoration_type][0]
        # if decoration in self.decorations:
        #     return decoration
        # return "None"



