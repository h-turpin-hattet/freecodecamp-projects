from arithmetic_formatter import arithmetic_arranger
import pytest


def test_input_none():
    """Input cannot be None: a ValueError is raised."""
    with pytest.raises(ValueError, match='Input cannot be None'):
        arithmetic_arranger(None)


def test_too_much_problems():
    """More than 5 problems returns 'Error: Too many problems.'."""
    assert arithmetic_arranger(
        ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "47 + 59", "12 - 48"]
    ) == 'Error: Too many problems.'


def test_wrong_operator():
    """An operator other than '+' or '-' returns an operator error."""
    assert arithmetic_arranger(
        ["1 * 3801", "523 / 49"]
    ) == "Error: Operator must be '+' or '-'."


def test_only_digits():
    """An operand containing a non-digit returns a digits error."""
    assert arithmetic_arranger(
        ["52b + 49"]
    ) == 'Error: Numbers must only contain digits.'


def test_maximum_digits():
    """An operand of more than four digits returns a length error."""
    assert arithmetic_arranger(
        ["1 + 38091"]
    ) == 'Error: Numbers cannot be more than four digits.'


def test_result_shown():
    """With display_answers=True, the results line is shown below."""
    assert arithmetic_arranger(
        ["1 + 3801"], True
    ) == '     1\n+ 3801\n------\n  3802'


def test_aligned_operand():
    """A single problem is right-aligned with the operator on line 2."""
    assert arithmetic_arranger(["32 + 698"]) == '   32\n+ 698\n-----'


def test_multiple_problems():
    """Several problems are separated by 4 spaces, with dashes under each."""
    assert arithmetic_arranger(
        ["32 + 698", "3801 - 2"]
    ) == '   32      3801\n+ 698    -    2\n-----    ------'
