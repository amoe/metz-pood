from main import Wheel
from pytest import approx

def test_calculates_diameter():
    wheel = Wheel(26, 1.5)
    assert wheel.diameter() == approx(29)
