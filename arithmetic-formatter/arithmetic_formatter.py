def arithmetic_formatter(problems, display_answers=False):
    
    #Validation
    status, message = validation(problems)
    if not status:
        return message

    #
    

#problems = ["32 + 8", "3701 - 3801", "9999 + 9999", "523 - 49", "47 + 59", "12 - 48"]
problem = "32 + 980"
ex = '   32\n+ 980\n-----'
x = problem.split()
z = len(max(x[::2],key=len))

a = x[0].rjust(z+2)
b = x[1] + x[2].rjust(z+1)
c = '-' * (z+2)
result = f'{a}\n{b}\n{c}'
print(result)



           


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
    
    if any (problem.split()[1] not in ['+', '-'] for problem in problems):
        return False, "Error: Operator must be '+' or '-'."
    
    if not all(operand.isdigit() for problem in problems for operand in problem.split()[::2]):
        return False, 'Error: Numbers must only contain digits.'

    if any(len(operand)>4 for problem in problems for operand in problem.split()[::2]):
        return False, 'Error: Numbers cannot be more than four digits.'

    return True, ''
