from pytest import approx
from main import Gear

def test_calculates_gear_inches():
    chainring = 52
    cog = 11
    rim = 26
    tire = 1.5
    
    gear = Gear(chainring, cog, rim, tire)
    
    assert gear.gear_inches() == approx(137.1, rel=1e-4)
