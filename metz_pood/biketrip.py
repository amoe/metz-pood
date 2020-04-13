class Mechanic:
    def prepare_bicycles(self, bicycles):
        for bicycle in bicycles:
            self.prepare_bicycle(bicycle)
    
    def prepare_bicycle(self, bicycle):
        pass

class TripCoordinator:
    def buy_food(self, customers):
        pass
    
class Driver:
    def gas_up(self, vehicle):
        pass

    def fill_water_tank(self, vehicle):
        pass

class Trip:
    def __init__(self, bicycles, customers, vehicle):
        self.bicycles = bicycles
        self.customers = customers
        self.vehicle = vehicle

    def prepare(self, preparers):
        for preparer in preparers:
            if isinstance(preparer, Mechanic):
                preparer.prepare_bicycle(self.bicycles)
            elif isinstance(preparer, TripCoordinator):
                preparer.buy_food(self.customers)
            elif isinstance(preparer, Driver):
                preparer.gas_up(self.vehicle)
                preparer.fill_water_tank(self.vehicle)
            
