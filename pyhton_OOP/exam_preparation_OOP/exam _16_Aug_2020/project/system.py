from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware

class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_instance = PowerHardware(name, capacity, memory)
        if new_instance not in System._hardware:
            System._hardware.append(new_instance)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_instance = HeavyHardware(name, capacity, memory)
        if new_instance not in System._hardware:
            System._hardware.append(new_instance)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        new_instance = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_instance)
        System._software.append(new_instance)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        new_instance = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_instance)
        System._software.append(new_instance)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if hardware and software:
            hardware, software = hardware[0], software[0]
            hardware.uninstall(software)
            System._software.remove(software)
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory_cons_software = sum([s.memory_consumption for s in System._software])
        total_capacity_cons_software = sum([s.capacity_consumption for s in System._software])
        total_memory_cons_hardware = sum([s.memory for s in System._hardware])
        total_capacity_cons_hardware = sum([s.capacity for s in System._hardware])
        output = ["System Analysis"]
        output.append(f"Hardware Components: {len(System._hardware)}")
        output.append(f"Software Components: {len(System._software)}")
        output.append(f"Total Operational Memory: {total_memory_cons_software} / {total_memory_cons_hardware}")
        output.append(f"Total Capacity Taken: {total_capacity_cons_software} / {total_capacity_cons_hardware}")
        return "\n".join(output)

    @staticmethod
    def system_split():
        output = []
        for item in System._hardware:
            number_of_express_comps = [1 for s in item.software_components if s.software_type == "Express"]
            number_of_light_comps = [1 for s in item.software_components if s.software_type == "Light"]
            memory_soft_comps = sum([x.memory_consumption for x in item.software_components])
            total_capacity_soft_comps = sum([x.capacity_consumption for x in item.software_components])
            check_comps = [c.name for c in item.software_components]
            output.append(f"Hardware Component - {item.name}")
            output.append(f"Express Software Components: {len(number_of_express_comps)}")
            output.append(f"Light Software Components: {len(number_of_light_comps)}")
            output.append(f"Memory Usage: {memory_soft_comps} / {item.memory}")
            output.append(f"Capacity Usage: {total_capacity_soft_comps} / {item.capacity}")
            output.append(f"Type: {item.hardware_type}")
            if check_comps:
                output.append(f"Software Components: {', '.join(check_comps)}")
            else:
                output.append(f"Software Components: None")
        return "\n".join(output)
