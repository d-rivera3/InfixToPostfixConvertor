# contains functionality to split an expression into a list of parts (number values, function names, operators)

from precedence import operators    # operator dictionary


# check if string is a number
def is_number(n):
    try:
        # Type-casting the string to `float`
        float(n)
    except ValueError:
        # If string is not a valid `float`, it'll raise `ValueError` exception so false
        return False
    return True


# check if string an operator
def is_operator(line):
    # check downwards from largest operator size 3 to correctly identify operator (e.g. >>> is not > three times)
    if line[:3] in operators:
        return True
    elif line[:2] in operators:
        return True
    elif line[0] in operators:
        return True
    else:
        return False


# get length of operator
def len_operator(line):
    if line[:3] in operators:
        return 3
    elif line[:2] in operators:
        return 2
    elif line[0] in operators:
        return 1
    else:
        return False


# spilt line into parts
def spilt(line):
    str_len = len(line)     # expression string
    parts = []  # resulting list of parts

    # if empty string
    if str_len == 0:
        return parts

    # index of string
    i = 0

    # expression part
    part = ''

    # find parts
    while i < str_len:
        # if spot space, continue on line
        if line[i].isspace():
            i = i + 1

        # need to handle ',' b/c an inner expr inside a function possible (e.g. min(x,y))
        elif line[i] == ',':  # added comma to handle
            parts.append(line[i])
            part = ''
            i = i + 1

        # if spot a number, get the rest of possible digits
        elif is_number(line[i]):
            # build the number value part
            while i < str_len and is_number(line[i]):
                part += line[i]
                i += 1

            # add number value to list and clear part
            parts.append(part)
            part = ''

        # check if spot is a letter using built-in function isalpha()
        elif line[i].isalpha():
            # build the function name part
            while line[i].isalpha() and i < str_len:
                part += line[i]
                i += 1
            # add function name to list and clear part
            parts.append(part)
            part = ''

        # check if spot an operator
        elif is_operator(line[i:]):
            # get length of operator
            o = len_operator(line[i:])
            # get operator
            part = line[i:i + o]

            # add operator and clear part
            parts.append(part)
            part = ''

            # append index i
            i = i + o

    # return list of parts
    return parts
