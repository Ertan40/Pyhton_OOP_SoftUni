class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int ):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget - price < 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        # for i, worker in enumerate(self.workers): # second option
        #     if worker.name == worker_name:
        #         self.workers.pop(i)
        #         f"{worker_name} fired successfully"
        #  return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = [worker.salary for worker in self.workers]
        if self.__budget - sum(salaries) >= 0:
            left_budget = self.__budget - sum(salaries)
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_expenses = [animal.money_for_care for animal in self.animals]
        if self.__budget - sum(animal_expenses) >= 0:
            self.__budget -= sum(animal_expenses)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = []
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        output.append(f"You have {len(self.animals)} animals")
        output.append(f"----- {len(lions)} Lions:")
        output.extend(lions)
        # output.append((f'\n'.join(str(lion) for lion in lions)))
        output.append(f"----- {len(tigers)} Tigers:")
        output.extend(tigers)
        # output.append((f'\n'.join(str(tiger) for tiger in tigers)))
        output.append(f"----- {len(cheetahs)} Cheetahs:")
        output.extend(cheetahs)
        # output.append((f'\n'.join(str(cheetah) for cheetah in cheetahs)))
        return "\n".join(str(o) for o in output)

    def workers_status(self):
        output = []
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        output.append(f"You have {len(self.workers)} workers")
        output.append(f"----- {len(keepers)} Keepers:")
        output.extend(keepers)

        output.append(f"----- {len(caretakers)} Caretakers:")
        output.extend(caretakers)

        output.append(f"----- {len(vets)} Vets:")
        output.extend(vets)

        return "\n".join(str(o) for o in output)


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
