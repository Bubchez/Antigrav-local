import pytest
from add import add

def test_add_positive_numbers():
    """Test addition of two positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test addition of two negative numbers."""
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    """Test addition of a positive and a negative number."""
    assert add(2, -3) == -1

def test_add_zero():
    """Test addition of zero."""
    assert add(0, 0) == 0