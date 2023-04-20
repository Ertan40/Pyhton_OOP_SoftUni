from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
# ---------------------- score = 144 ----------------------------

class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def __find_service(self, name):
        return next(filter(lambda x: x.name == name, self.services), None)

    def __find_robot(self, name):
        return next(filter(lambda x: x.name == name, self.robots), None)

    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")
        if service_type == "MainService":
            new = MainService(name)
            self.services.append(new)
            return f"{service_type} is successfully added."
        else:
            new = SecondaryService(name)
            self.services.append(new)
            return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")
        if robot_type == "MaleRobot":
            new = MaleRobot(name, kind, price)
            self.robots.append(new)
            return f"{robot_type} is successfully added."
        else:
            new = FemaleRobot(name, kind, price)
            self.robots.append(new)
            return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot(robot_name)
        service = self.__find_service(service_name)

        if service.capacity == len(service.robots):    # if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        if not type(robot).__name__ == "FemaleRobot" or not type(service).__name__ == "SecondaryService":
            self.robots.remove(robot)
            service.robots.append(robot)
            return f"Successfully added {robot_name} to {service_name}."

        elif not type(robot).__name__ == "MaleRobot" or not type(service).__name__ == "MainService":
            self.robots.remove(robot)
            service.robots.append(robot)
            return f"Successfully added {robot_name} to {service_name}."
        else:
            return "Unsuitable service."
        # return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        # robot = self.__find_robot(robot_name)
        # service = self.__find_service(service_name)
        # if robot not in service.robots:
        #     raise Exception("No such robot in this service!") #TODO
        # service.robots.remove(robot)
        # self.robots.append(robot)
        # return f"Successfully removed {robot_name} from {service_name}."
        service = self.__find_service(service_name)
        current_robot = None
        for robot in service.robots:
            if robot.name == robot_name:
                current_robot = robot
        if current_robot:
            service.robots.remove(current_robot)
            self.robots.append(current_robot)
            return f"Successfully removed {robot_name} from {service_name}."

        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service(service_name)
        robots = []
        for robot in service.robots:
            robots.append(robot.eating())
        return f"Robots fed: {len(robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service(service_name)
        total_price = 0
        if service.robots:
            for robot in service.robots:
                total_price += robot.price
            return f"The value of service {service_name} is {total_price:.2f}."
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        output = []
        for service in self.services:
            output.append(service.details())

        return "\n".join(output)