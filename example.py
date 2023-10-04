import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def subtract(a, b):
    return a - b   # fixed

@pytest.mark.parametrize("test_input1, test_input2, expected", [(5, 0, 5), (4.3, 0.9, 3.4)]) 
def test_subtract(test_input1, test_input2, expected):
    assert subtract(test_input1, test_input2) == expected
