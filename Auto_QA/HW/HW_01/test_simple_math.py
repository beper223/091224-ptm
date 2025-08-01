from simple_math import SimpleMath
import pytest

@pytest.fixture
def simplemath():
    return SimpleMath()

def test_square_positive_numbers(simplemath):
    assert simplemath.square(2) == 4

def test_cube_negative_numbers(simplemath):
    assert simplemath.cube(-3) == -27

def test_square_with_zero(simplemath):
    assert simplemath.square(0) == 0