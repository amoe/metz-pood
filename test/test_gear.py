from pytest import approx
from main import Gear, Wheel

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
    gear = Gear(chainring, cog, wheel)
    
    assert gear.gear_inches() == approx(137.1, rel=1e-4)


# Use a test double.
def test_calculates_gear_inches_with_test_double():
    chainring = 52
    cog = 11

    gear = Gear(chainring, cog, DiameterDouble())
    
    assert gear.gear_inches() == approx(47.27, rel=1e-4)
