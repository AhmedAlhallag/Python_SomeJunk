import math
import pytest

@pytest.mark.sqr
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.sqr
def test_sqr():
    num = 7 
    assert num * num == 40

@pytest.mark.other
def test_vals():
    num1 = 10
    num2 = 11
    assert num1 == num2


