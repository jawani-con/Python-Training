import pytest
from two import add, subtract, multiply, divide

def test_add():
    """Test the addition function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtraction function"""
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(-5, -3) == -2

def test_multiply():
    """Test the multiplication function"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-2, -3) == 6
    assert multiply(0, 100) == 0

def test_divide():
    """Test the division function"""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
    assert divide(5, 0) == "Error! Division by zero."

def test_invalid_division():
    """Test invalid division case with zero."""
    assert divide(5, 0) == "Error! Division by zero."
