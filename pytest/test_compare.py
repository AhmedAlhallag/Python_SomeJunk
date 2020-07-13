import math
import pytest

@pytest.mark.great
def test_greater():
    num  = 100
    assert num > 100

def test_gequal():
    num = 90
    assert num >= 100

@pytest.mark.other
def test_less():
    num = 100
    assert num < 99
