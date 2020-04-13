from metz_pood.biketrip import Mechanic, TripCoordinator, Driver, Trip
from metz_pood.test_utility import responds_to
from unittest.mock import Mock

def test_mechanic_implements_the_preparer_interface():
    assert responds_to(Mechanic(), 'prepare_trip')

def test_tripcoordinator_implements_the_preparer_interface():
    assert responds_to(TripCoordinator(), 'prepare_trip')

def test_tripcoordinator_implements_the_preparer_interface():
    assert responds_to(Driver(), 'prepare_trip')

    
def test_requests_trip_preparation():
    mock_preparer = Mock()
    trip = Trip([], [], [])
    trip.prepare([mock_preparer])
    mock_preparer.prepare_trip.assert_called_with(trip)
