import pytest
import math
from operations import add, subtract

def test_add():
    assert add(10, 5) == 15
    assert add(-10, 5) == -5
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-10, 5) == -15
    assert subtract(0, 0) == 0

def test_sqrt_negative():
    with pytest.raises(ValueError):
        math.sqrt(-1)

def test_log_negative():
    with pytest.raises(ValueError):
        math.log(-1)

def test_log_zero():
    with pytest.raises(ValueError):
        math.log(0)