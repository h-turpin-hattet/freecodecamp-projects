# Arithmetic Formatter

[![Arithmetic Formatter tests](https://github.com/h-turpin-hattet/freecodecamp-projects/actions/workflows/arithmetic-formatter-tests.yml/badge.svg?branch=main&event=push)](https://github.com/h-turpin-hattet/freecodecamp-projects/actions/workflows/arithmetic-formatter-tests.yml)

freeCodeCamp - Scientific Computing with Python | Project 1

## Description

Arranges addition and subtraction problems vertically and side by side,
the way they are written in primary school. The answers can optionally be
displayed below each problem.

> The project is called "Arithmetic Formatter", but the function required by
> freeCodeCamp is named `arithmetic_arranger`.

## Usage

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

With the answers (second argument set to `True`):

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Errors

| Case | Result |
|---|---|
| More than 5 problems | `Error: Too many problems.` |
| Operator other than `+` or `-` | `Error: Operator must be '+' or '-'.` |
| Operand with non-digit characters | `Error: Numbers must only contain digits.` |
| Operand with more than 4 digits | `Error: Numbers cannot be more than four digits.` |
| Input is `None` | raises `ValueError` |

## Project structure

```
arithmetic-formatter/
├── arithmetic_formatter.py        # the code
├── test_arithmetic_formatter.py   # pytest test suite
└── README.md
```

| Function | Role |
|---|---|
| `validation` | Checks the input and returns a status and an error message |
| `maximum_length` | Returns the length of the longest operand of a problem |
| `format_problems` | Builds the three lines and places the problems side by side |
| `calculate` | Computes the result of each problem |
| `show_answers` | Builds the answers line, right-aligned under each problem |
| `arithmetic_arranger` | Entry point: validates, formats, optionally adds the answers |


## Running the tests

From the `arithmetic-formatter/` folder:

```bash
py -m pytest -v
py -m flake8 .
```

The suite has 8 tests: 5 for input validation and 3 for the layout
(answers line, alignment, several problems side by side).

## Method

- **TDD**: the tests were written before the code.
- **CI**: a GitHub Actions workflow runs flake8, then pytest, on every
  change in this folder.

### Design decisions

- `validation` returns a status and a message, so that judging the input
  stays separate from displaying the result.
- Each function splits the problems on its own, so every function can be read
  without knowing how the others work.
- The width computation lives in `maximum_length`, to avoid duplicating it in
  `format_problems` and `show_answers`.