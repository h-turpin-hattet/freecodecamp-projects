from arithmetic_formatter import arithmetic_formatter
import pytest

# Test that input cannot be None
def test_input_none():
    with pytest.raises(ValueError, match='Input cannot be None'):
        arithmetic_formatter(None)

# Test that input cannot have more than 5 problems
def test_too_much_problems():
    assert arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "47 + 59", "12 - 48"]) == 'Error: Too many problems.'

# Test that operator must be + or -  
def test_wrong_operator():
    assert arithmetic_formatter(["1 * 3801", "523 / 49"]) == "Error: Operator must be '+' or '-'."

# Test that all operand are only digits  
def test_only_digits():
    assert arithmetic_formatter(["52b + 49"]) == 'Error: Numbers must only contain digits.'

# Test that operand are maximum 4 digits  
def test_maximum_digits():
    assert arithmetic_formatter(["1 + 38091"]) == 'Error: Numbers cannot be more than four digits.'

# Test that result of operation is shown if parameter is set to True  
def test__result_shown():
    assert arithmetic_formatter(["1 + 3801"],True) == '     1\n+ 3801\n------\n  3802'


