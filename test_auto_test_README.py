
# test_hypothetical_module.py
import pytest
from hypothetical_module import add

# Fixture for providing test data
@pytest.fixture(params=[
    (2, 3, 5),
    (-2, -3, -5),
    (0, 0, 0),
    (2.5, 3.5, 6.0),
    (1000000, 2000000, 3000000)
], ids=["positive", "negative", "zero", "float", "large"])
def add_data(request):
    return request.param

# Test function using the fixture
def test_add(add_data):
    a, b, expected = add_data
    assert add(a, b) == expected
