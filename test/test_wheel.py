from metz_pood.wheel import Wheel
from metz_pood.role_predicates import is_diameterizable
from pytest import approx, fixture

@fixture
def wheel():
    return Wheel(26, 1.5)

def test_calculates_diameter(wheel):
    assert wheel.diameter() == approx(29)

def test_implements_the_diameterizable_interface(wheel):
    assert is_diameterizable(wheel)


