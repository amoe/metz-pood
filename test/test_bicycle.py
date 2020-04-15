from metz_pood.bicycle import Bicycle, RoadBike
from metz_pood.test_utility import responds_to
from metz_pood.role_predicates import assert_is_bicycle
import pytest


# Because this fn is defined within an actual pytest file, its functions
# will have their assertions rewritten properly.
def assert_is_bicycle(obj):
    assert responds_to(obj, 'default_tire_size')
    assert responds_to(obj, 'default_chain')
    assert responds_to(obj, 'spares')
    assert hasattr(obj, 'chain')
    assert hasattr(obj, 'size')
    assert hasattr(obj, 'tire_size')

def test_bicycle():
    assert_is_bicycle(Bicycle(tire_size=0))

def test_roadbike():
    assert_is_bicycle(RoadBike())

