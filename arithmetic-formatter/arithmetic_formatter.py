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
    for problem in problems:
        element_problem = problem.split()
        max_length_problem = len(max(element_problem[::2],key=len))
        line_1 = element_problem[0].rjust(max_length_problem+2)
        line_2 = element_problem[1] + element_problem[2].rjust(max_length_problem+1)
        line_3 = '-' * (max_length_problem+2)
        line_1_problems.append(line_1)
        line_2_problems.append(line_2)
        line_3_problems.append(line_3)
    
    line_1_result = '    '.join(line_1_problems)
    line_2_result = '    '.join(line_2_problems)
    line_3_result = '    '.join(line_3_problems)
    operation = f'{line_1_result}\n{line_2_result}\n{line_3_result}'

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
        operands = [int(i) for i in elements_problem[::2]]
        if elements_problem[1] == '+':
            result = operands[0]+operands[1]
            
        else:
            result = operands[0]-operands[1]
        results_list.append(result)

    return results_list

def show_answers(problems,list_results):
    list_max_length_problem = []
    for problem in problems:
        element_problem = problem.split()
        max_length_problem = len(max(element_problem[::2],key=len))
        list_max_length_problem.append(max_length_problem)
    
    list_results_str = [str(elements) for elements in list_results]
    list_results_str_spaced = []
    for i in range(len(list_results)):
        results_spaced = list_results_str[i].rjust(list_max_length_problem[i]+2)
        list_results_str_spaced.append(results_spaced)
    result_line_spaced = '    '.join(list_results_str_spaced)
    final_result_line = f'\n{result_line_spaced}'

    return final_result_line


def arithmetic_formatter(problems, display_answers=False):
    
    #Validation
    status, message = validation(problems)
    if not status:
        return message

    #Format problems
    result = format_problems(problems)

    #return if display is False
    if not display_answers:
        return result
    #calculation of results
    list_results = calculate(problems)

    #format answer line
    answer_line = show_answers(problems,list_results)
    final_result = f'{result}{answer_line}'

    return final_result

problems = ["1 + 3801", "32 + 8"]
print(arithmetic_formatter(problems, display_answers=True))