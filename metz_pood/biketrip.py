class Mechanic:
    def prepare_bicycles(self, bicycles):
        for bicycle in bicycles:
            self.prepare_bicycle(bicycle)
    
    def prepare_bicycle(self, bicycle):
        pass

    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self.prepare_bicycle(bicycle)

class TripCoordinator:
    def buy_food(self, customers):
        pass

    def prepare_trip(self, trip):
        self.buy_food(trip.customers)
    
class Driver:
    def gas_up(self, vehicle):
        pass

    def fill_water_tank(self, vehicle):
        pass

    def prepare_trip(self, trip):
        self.gas_up(trip.vehicle)
        self.fill_water_tank(trip.vehicle)

class Trip:
    def __init__(self, bicycles, customers, vehicle):
        self.bicycles = bicycles
        self.customers = customers
        self.vehicle = vehicle

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)            
