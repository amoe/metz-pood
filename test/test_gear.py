from pytest import approx
import pytest
from metz_pood.gear import Gear
from metz_pood.wheel import Wheel

from unittest.mock import Mock

class DiameterDouble:
    def diameter(self):
        return 10

# Use the real Wheel class to provide the hidden diameter calculation.
def test_calculates_gear_inches_with_real_dependency():
    chainring = 52
    cog = 11
    rim = 26
    tire = 1.5

    wheel = Wheel(rim, tire)
    gear = Gear(chainring, cog, wheel, None)
    
    assert gear.gear_inches() == approx(137.1, rel=1e-4)


# Use a test double.  This is not a mock!
def test_calculates_gear_inches_with_test_double():
    chainring = 52
    cog = 11
    gear = Gear(chainring, cog, DiameterDouble(), None)
    
    assert gear.gear_inches() == approx(47.27, rel=1e-4)

def test_notifies_observers_when_cogs_change():
    mock_observer = Mock()
    chainring = 52
    cog = 11
    gear = Gear(chainring, cog, DiameterDouble(), mock_observer)
    gear.set_cog(27)
    mock_observer.changed.assert_called_with(52, 27)

    
def test_notifies_observers_when_chainrings_change():
    mock_observer = Mock()
    chainring = 52
    cog = 11
    gear = Gear(chainring, cog, DiameterDouble(), mock_observer)
    gear.set_chainring(42)
    mock_observer.changed.assert_called_with(42, 11)

    
