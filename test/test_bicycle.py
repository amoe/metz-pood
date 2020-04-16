from metz_pood.bicycle import Bicycle, RoadBike
from metz_pood.test_utility import responds_to
from metz_pood.role_predicates import assert_is_bicycle
import pytest


# Because this fn is defined within an actual pytest file, its functions
# will have their assertions rewritten properly.
def assert_fulfils_bicycle_role(obj):
    assert responds_to(obj, 'default_tire_size')
    assert responds_to(obj, 'default_chain')
    assert responds_to(obj, 'spares')
    assert hasattr(obj, 'chain')
    assert hasattr(obj, 'size')
    assert hasattr(obj, 'tire_size')

# Subclasses are required to respond to certain methods, check that
# they don't do anything so crazy that they break their inherited
# behaviour.  We don't care that the 'default_tire_size' method of the
# base class raises an exception just as long as the subclass does
# indeed respond to the message.
def assert_fulfils_bicycle_subclass_requirements(obj):
    assert responds_to(obj, 'post_initialize')
    assert responds_to(obj, 'local_spares')
    assert responds_to(obj, 'default_tire_size')


def test_bicycle():
    assert_fulfils_bicycle_role(Bicycle(tire_size=0))

def test_roadbike():
    rb = RoadBike()
    assert_fulfils_bicycle_role(rb)
    assert_fulfils_bicycle_subclass_requirements(rb)

