from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity=15):
        super().__init__(name, capacity)

    def details(self):
        output = [f"{self.name} Secondary Service:"]  # [f"{self.name} {self.__class__.__name__}:"]
        names = []
        if self.robots:
            for robot in self.robots:
                names.append(robot.name)
            output.append(f"Robots: {' '.join(names)}")
        else:
            output.append("Robots: none")

        return "\n".join(output)