from metz_pood.wheel import Wheel
from pytest import approx, fixture

@fixture
def wheel():
    return Wheel(26, 1.5)

def test_calculates_diameter(wheel):
    assert wheel.diameter() == approx(29)

def responds_to(obj, message):
    m = getattr(obj, message, None)
    if m is None:
        return False
    else:
        return callable(m)
    

def test_implements_the_diameterizable_interface(wheel):
    assert responds_to(wheel, 'diameter')
