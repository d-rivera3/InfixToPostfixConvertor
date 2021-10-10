# we still need a way to classify what each part actually is (operator/number/function), operator levels. and correctly
# differentiate between unary + and - operations from subtraction and addition

from precedence import operators, functions     # get operator and function dictionaries
from expressionSplitter import is_number        # get made function to check for numbers


# process identification of parts
def is_which(arr):
    which = []          # list of what parts are in list
    precedence = []     # list of what operator level parts are in list (if applicable)
    part = 0  # index for parts list

    # parse through parts list to identify type and precedence
    while part < len(arr):
        # check is part is a number value
        if is_number(arr[part]):
            which.append(int)       # add int as identifier in which list
            precedence.append(int)  # add int as identifier in precedence list (ignorable)

        # check is part is an operator
        elif arr[part] in operators:
            which.append('op')  # add 'op' as identifier in which list

            '''conditions to determine if '-','+' is level 2 or 5'''
            # expression begins with unary -
            if part == 0 and arr[part] == '-':
                if is_number(arr[part + 1]):  # op, int
                    precedence.append(2)
                elif arr[part + 1] in operators:  # op, op
                    precedence.append(2)
            # if unary - situation case is comma, op
            elif arr[part] == '-' and which[part - 1] == 'comma':
                precedence.append(2)
            # if unary - situation case is op,op,int
            elif arr[part] == '-' and which[part - 1] == 'op' and is_number(arr[part + 1]):
                if arr[part - 1] == ')':    # op before is parentheses, likely to be level 5 subtraction
                    precedence.append(5)
                else:
                    precedence.append(2)    # else level 2
            # if subtraction - situation case is int,op,int
            elif arr[part] == '-' and is_number(arr[part - 1]) and is_number(arr[part + 1]):
                precedence.append(5)

            # expression begins with unary +
            elif part == 0 and arr[part] == '+':
                if is_number(arr[part + 1]):  # op, int
                    precedence.append(2)
                elif arr[part + 1] in operators:  # op, op
                    precedence.append(2)
            # if unary + situation case is comma, op
            elif arr[part] == '+' and which[part - 1] == 'comma':
                precedence.append(2)
            # if unary + situation case is op,op,int
            elif arr[part] == '+' and which[part - 1] == 'op' and is_number(arr[part + 1]):
                if arr[part - 1] == ')':    # op before is parentheses, likely to be level 5 addition
                    precedence.append(5)
                else:
                    precedence.append(2)    # else level 2
            # if addition + situation case is int,op,int
            elif arr[part] == '+' and is_number(arr[part - 1]) and is_number(arr[part + 1]):
                precedence.append(5)

            # find level for non-confusing other operators
            else:
                precedence.append(operators[arr[part]])

        # if part is a function
        elif arr[part] in functions:
            which.append('func')        # add 'func' as identifier in which list
            precedence.append('func')   # add 'func' as identifier in precedence list (ignorable)
        # if part is a comma
        elif arr[part] == ',':
            which.append('comma')       # add 'comma' as identifier in which list
            precedence.append('comma')  # add 'comma' as identifier in precedence list (ignorable)
        # unsupported
        else:
            which.append(ValueError)        # error, no clue what it is
            precedence.append(ValueError)   # error, no clue what it is

        # move onto next part
        part += 1

    # returns 2 lists: which that tells what each part is, precedence that tells what the operator level is
    return which, precedence
