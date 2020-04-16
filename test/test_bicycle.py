from metz_pood.bicycle import Bicycle, RoadBike
from metz_pood.test_utility import responds_to
from metz_pood.role_predicates import assert_is_bicycle
import pytest
from pytest import raises


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


class BikeDouble(Bicycle):
    def default_tire_size(self):
        return 0

    def local_spares(self):
        return {'saddle': 'painful'}


# Bicycle is an abstract superclass.
def test_bicycle():
    b = Bicycle(tire_size=0)
    double = BikeDouble()

    # We can use the instantiated base class for most tests.
    assert_fulfils_bicycle_role(b)
    # Test that the superclass forces its subclasses to implement the
    # abstract method 'default_tire_size'.
    with pytest.raises(NotImplementedError):
        b.default_tire_size()

    # Use the double to blackbox-test the correct invocation of
    # the template method in the subclass.
    # i.e. test that the base class correctly calls and handles the
    # return value of local_spares in subclasses.
    #
    # This would not be possible without the test double, as local_spares
    # behaviour in Bicycle (empty dict) is indistinguishable from a bug.
    # At the same time, we couldn't use the double to prove that the
    # base class raises NotImplementedError.  So both strategies are needed.
    assert double.spares() == {'tire_size': 0,
                               'chain': '11-speed',
                               'saddle': 'painful'}

# Defend against the test double becoming obsolete.
def test_bikedouble():
    double = BikeDouble()
    assert_fulfils_bicycle_role(double)
    assert_fulfils_bicycle_subclass_requirements(double)

def test_roadbike():
    rb = RoadBike(tape_color='red')
    assert_fulfils_bicycle_role(rb)
    assert_fulfils_bicycle_subclass_requirements(rb)
    assert rb.local_spares()['tape_color'] == 'red'

