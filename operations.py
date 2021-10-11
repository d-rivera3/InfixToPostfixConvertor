# file containing actual calculation functionality for operators and functions
# remember program should reflect 16-bit singed integers and use of 16-bit arithmetic

import numpy as np

""" The Operators """


# ~ bitwise inverse
def bit_inverse(num):
    return np.int16(np.invert(np.int16(num)))


# ! logical inverse
def logical_not(num):
    boolean = False

    # check if num if true
    if np.int16(num) != 0:
        boolean = True

    # return !boolean (0 False, -1 True)
    if boolean is False:
        return -1  # !False is True
    else:
        return 0  # !True is False


# * multiplication
def multi(a, b):
    y = np.int16(a)
    x = np.int16(b)
    return np.int16(np.multiply(y, x))


# / division
def divide(a, b):
    y = np.int16(a)
    x = np.int16(b)
    return np.int16(np.divide(y, x))


# % mod
def mod(a, b):
    y = np.int16(a)
    x = np.int16(b)

    if x == 0:
        raise ZeroDivisionError

    return np.int16(np.mod(y, x))


# + addition (level 5)
def add(a, b):
    y = np.int16(a)
    x = np.int16(b)
    return np.int16(np.add(y, x))


# - subtraction (level 5)
def sub(a, b):
    y = np.int16(a)
    x = np.int16(b)
    return np.int16(np.subtract(y, x))


# - negative (unary level 2)
def unary_minus(num):
    return np.int16(np.negative(np.int16(num)))


# + positive (unary level 2)
def unary_plus(num):
    return np.int16(num)


# << left shift
def left_shift(a, b):
    return np.int16(np.left_shift(np.int16(a), np.int16(b)))


# >> right shift
def right_shift(a, b):
    return np.int16(np.right_shift(np.int16(a), np.int16(b)))


# <<< left rotate
def left_rotate(num, r):
    s = np.binary_repr(np.int16(num), 16)
    # print(s)

    # array of bits
    bits = []
    for b in s:
        bits.append(b)
    # print(bits)

    # left rotate bits
    r_bits = np.roll(bits, np.negative(np.int16(r)))
    # print(r_bits)

    # convert as a bit string
    bit_str = ''.join(str(b) for b in r_bits)
    # print(bit_str)

    # convert to int base 16
    value = int(bit_str, 2)
    # print(value)

    return np.int16(value)


# >>> right rotate
def right_rotate(num, r):
    s = np.binary_repr(np.int16(num), 16)
    # print(s)

    # array of bits
    bits = []
    for b in s:
        bits.append(b)
    # print(bits)

    # right rotate bits
    r_bits = np.roll(bits, np.int16(r))
    # print(r_bits)

    # convert as a bit string
    bit_str = ''.join(str(b) for b in r_bits)
    # (bit_str)

    # convert to int base 16
    value = int(bit_str, 2)
    # print(value)

    return np.int16(value)


# < less than
def lt(a, b):
    if np.int16(a) < np.int16(b):
        return -1
    else:
        return 0


# > greater than

def gt(a, b):
    if np.int16(a) > np.int16(b):
        return -1
    else:
        return 0


# <= less than or equal to
def lte(a, b):
    if np.int16(a) < np.int16(b) or np.int16(a) == np.int16(b):
        return -1
    else:
        return 0


# >= greater than or equal to
def gte(a, b):
    if np.int16(a) > np.int16(b) or np.int16(a) == np.int16(b):
        return -1
    else:
        return 0


# == equal
def equal(a, b):
    if np.int16(a) == np.int16(b):
        return -1
    else:
        return 0


# != not equal
def not_equal(a, b):
    if not (np.int16(a) == np.int16(b)):
        return -1
    else:
        return 0


# & bitwise and
def bitwise_and(a, b):
    return np.int16(np.int16(a) & np.int16(b))


# ^ bitwise XOR
def bitwise_xor(a, b):
    return np.int16(np.int16(a) ^ np.int16(b))


# | bitwise or
def bitwise_or(a, b):
    return np.int16(np.int16(a) | np.int16(b))


# && logical and
def logical_and(a, b):
    # boolean representation of a,b
    c1 = False
    c2 = False

    # check if a,b are true
    if np.int16(a) != 0:
        c1 = True
    if np.int16(b) != 0:
        c2 = True

    # logical and
    ans = (c1 and c2)

    # return 0 False, -1 True
    if ans is True:
        return -1
    else:
        return 0


# ^^ logical XOR
def logical_xor(a, b):
    # boolean representation of a,b
    c1 = False
    c2 = False

    # check if a,b are true
    if np.int16(a) != 0:
        c1 = True
    if np.int16(b) != 0:
        c2 = True

    # logical and
    ans = (c1 != c2)

    # return 0 False, -1 True
    if ans is True:
        return -1
    else:
        return 0


# || logical or
def logical_or(a, b):
    # boolean representation of a,b
    c1 = False
    c2 = False

    # check if a,b are true
    if np.int16(a) != 0:
        c1 = True
    if np.int16(b) != 0:
        c2 = True

    # logical or
    ans = c1 or c2
    # print(ans)

    # return 0 False, -1 True
    if ans is False:
        return 0
    else:
        return -1


""" The Functions   """


# square
def sq(num):
    return np.int16(np.square(np.int16(num)))


# min
def min(x, y):
    if np.int16(x) < np.int16(y):
        return np.int16(x)
    else:
        return np.int16(y)


# max
def max(x, y):
    if np.int16(x) > np.int16(y):
        return np.int16(x)
    else:
        return np.int16(y)


# absolute
def abs(num):
    return np.int16(np.absolute(np.int16(num)))
