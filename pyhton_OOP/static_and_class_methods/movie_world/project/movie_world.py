# from pyhton_OOP.static_and_class_methods.movie_world.project.customer import Customer
from project.customer import Customer
# from pyhton_OOP.static_and_class_methods.movie_world.project.dvd import DVD
from project.dvd import DVD

class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []   # customers objects
        self.dvds = []    # dvd objects

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in self.dvds if x.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False  # if any errors check this out
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        output = []
        for customer in self.customers:
            output.append(f"{customer}")
        for dvd in self.dvds:
            output.append(f"{dvd}")
        return "\n".join(output)
