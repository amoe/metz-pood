from metz_pood.biketrip import Mechanic, TripCoordinator, Driver
from metz_pood.test_utility import responds_to

def test_mechanic_implements_the_preparer_interface():
    assert responds_to(Mechanic(), 'prepare_trip')

def test_tripcoordinator_implements_the_preparer_interface():
    assert responds_to(TripCoordinator(), 'prepare_trip')

def test_tripcoordinator_implements_the_preparer_interface():
    assert responds_to(Driver(), 'prepare_trip')

    


