from calculator import Calculator
import pytest


def test_get_last_calculation_default():
    calc = Calculator()                                 # Arrange
    actual = calc.get_last_calculation()                # Act
    expected = 0
    assert actual == expected


def test_get_last_calculation_given():
    calc = Calculator(1)                                # Arrange
    actual = calc.get_last_calculation()                # Act
    expected = 1
    assert actual == expected


def test_add():
    calc = Calculator()                                 # Arrange
    calc.add(1, 1)                                      # Add two numbers
    actual = calc.add(calc.get_last_calculation(), 1)   # Add from last calculation
    expected = 3
    assert actual == expected


def test_add_mixed():
    calc = Calculator()
    calc.add(1, 1.0)
    actual = calc.add(calc.get_last_calculation(), 1)
    expected = 3.0
    assert type(actual) == type(expected) and actual == expected    # Check if 3.0 == 3.0 and not 3.0 == 3


def test_subtract():
    calc = Calculator()                                     # Arrange
    calc.subtract(5, 2)                                     # Subtract two numbers
    actual = calc.subtract(calc.get_last_calculation(), 1)  # Subtract from last calculation
    expected = 2
    assert actual == expected


def test_subtract_mixed():
    calc = Calculator()
    calc.subtract(5, 2.0)
    actual = calc.subtract(calc.get_last_calculation(), 1)
    expected = 2.0
    assert type(actual) == type(expected) and actual == expected    # Check if 2.0 == 2.0 and not 2.0 == 2


def test_invalid_object():
    with pytest.raises(ValueError):                         # Expect ValueError from constructor
        calc = Calculator("1")


def test_invalid_add():
    calc = Calculator()
    actual = calc.add(1, "1")                               # TypeError returns "INVALID INPUT"
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_add_strings():
    calc = Calculator()
    actual = calc.add("1", "1")                             # Setter returns "INVALID INPUT"
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_subtract():
    calc = Calculator()
    actual = calc.subtract(2, "1")                          # TypeError returns "INVALID INPUT"
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_subtract_strings():
    calc = Calculator()
    actual = calc.subtract("2", "1")                        # Setter returns "INVALID INPUT"
    expected = "INVALID INPUT"
    assert actual == expected
