from metz_pood.wheel import Wheel
from metz_pood.test_utility import responds_to
from pytest import approx, fixture

@fixture
def wheel():
    return Wheel(26, 1.5)

def test_calculates_diameter(wheel):
    assert wheel.diameter() == approx(29)

def test_implements_the_diameterizable_interface(wheel):
    assert responds_to(wheel, 'diameter')
