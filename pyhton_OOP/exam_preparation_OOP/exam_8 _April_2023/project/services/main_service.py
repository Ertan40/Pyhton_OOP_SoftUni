from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str, capacity=30):
        super().__init__(name, capacity)

    def details(self):
        output = [f"{self.name} Main Service:"]    # [f"{self.name} Main Service:"]
        names = []
        if self.robots:
            for robot in self.robots:
                names.append(robot.name)
            output.append(f"Robots: {' '.join(names)}")
        else:
            output.append("Robots: none")

        return "\n".join(output)