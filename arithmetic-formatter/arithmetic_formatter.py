def validation(problems):
    """
    Validate the list of problems.

    Raises ValueError if problems is None.
    Returns (False, 'Error: ...') for the 4 error cases, checked in order.
    Returns (True, '') if everything is valid.
    """

    if problems is None:
        raise ValueError('Input cannot be None')

    if len(problems) > 5:
        return False, 'Error: Too many problems.'

    if any(
        problem.split()[1] not in ['+', '-']
        for problem in problems
    ):
        return False, "Error: Operator must be '+' or '-'."

    if not all(
        operand.isdigit()
        for problem in problems
        for operand in problem.split()[::2]
    ):
        return False, 'Error: Numbers must only contain digits.'

    if any(
        len(operand) > 4
        for problem in problems
        for operand in problem.split()[::2]
    ):
        return False, 'Error: Numbers cannot be more than four digits.'

    return True, ''


def maximum_length(element_problem):
    """
    Return the length of the longest operand of a problem.

    Takes a problem already split into its three parts.
    Returns an integer. The operator is ignored.
    """

    return len(max(element_problem[::2], key=len))


def format_problems(problems):
    """
    Arrange the problems vertically, side by side.

    Takes the full list of problems (already validated).
    Returns a single string made of 3 lines separated by '\\n':
    top operands, operator and bottom operands, dashes.
    Problems are separated by 4 spaces and numbers are right-aligned.
    """

    line_1_problems = []
    line_2_problems = []
    line_3_problems = []

    # Build the 3 lines of each problem
    for problem in problems:
        elements_problem = problem.split()
        max_length_problem = maximum_length(elements_problem)
        # Problem width = longest operand + operator + one space
        line_1 = elements_problem[0].rjust(max_length_problem + 2)
        # Operator takes 1 character, so the operand gets width - 1
        line_2 = (
            elements_problem[1]
            + elements_problem[2].rjust(max_length_problem + 1)
        )
        # One dash per character of the problem width
        line_3 = '-' * (max_length_problem + 2)
        line_1_problems.append(line_1)
        line_2_problems.append(line_2)
        line_3_problems.append(line_3)

    # Place the problems side by side, separated by 4 spaces
    line_1_results = '    '.join(line_1_problems)
    line_2_results = '    '.join(line_2_problems)
    line_3_results = '    '.join(line_3_problems)

    operation = f'{line_1_results}\n{line_2_results}\n{line_3_results}'

    return operation


def calculate(problems):
    """
    Compute the result of each problem.

    Takes the full list of problems (already validated).
    Returns a list of integers, one per problem, in the same order.
    Supports addition and subtraction only; results can be negative.
    """

    results_list = []
    for problem in problems:
        elements_problem = problem.split()
        # Operands are at even indexes
        operands = [int(operand) for operand in elements_problem[::2]]
        if elements_problem[1] == '+':
            result = operands[0] + operands[1]
        else:
            result = operands[0] - operands[1]
        results_list.append(result)

    return results_list


def show_answers(problems, results_list):
    """
    Build the answers line shown below the arranged problems.

    Takes the full list of problems and the list of their results
    (from calculate), in the same order.
    Returns a string that starts with '\\n', followed by the results
    right-aligned on the width of their problem and separated by 4 spaces.
    """

    # Width reference of each problem (same order as the results)
    max_length_problems_list = []
    for problem in problems:
        elements_problem = problem.split()
        max_length_problem = maximum_length(elements_problem)
        max_length_problems_list.append(max_length_problem)

    results_str_list = [str(result) for result in results_list]

    # Result n°i is aligned on the width of problem n°i (longest operand + 2)
    aligned_results_list = []
    for i in range(len(results_list)):
        aligned_result = (
            results_str_list[i].rjust(max_length_problems_list[i] + 2)
        )
        aligned_results_list.append(aligned_result)
    aligned_results_line = '    '.join(aligned_results_list)

    # Leading '\n' lets arithmetic_formatter append this line directly
    final_results_line = f'\n{aligned_results_line}'

    return final_results_line


def arithmetic_arranger(problems, display_answers=False):
    """
    Arrange arithmetic problems vertically, side by side.

    Takes a list of problems and an optional flag.
    Returns the arranged problems, with their answers below if
    display_answers is True, or an error message if the input is invalid.
    Raises ValueError if problems is None.
    """

    # Stop early and return the error message if the input is invalid
    status, message = validation(problems)
    if not status:
        return message

    result = format_problems(problems)

    # Without answers, the 3 arranged lines are the final output
    if not display_answers:
        return result

    # Answers requested,claculate and add the results line below the problems
    results_list = calculate(problems)
    answer_line = show_answers(problems, results_list)

    # answer_line starts with '\n', so it goes on its own line
    # Commented for pipeline test
    # final_result = f'{result}{answer_line}'

    return final_result
