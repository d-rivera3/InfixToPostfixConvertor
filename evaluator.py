# file does the actual calculation of the expression for an answer, evaluates the operators and functions

import operations   # for the actual functionality of operators and functions


def evaluate(postfix):
    # the expression after changed in postfix form
    expr = postfix

    # case 1: handle blank expression
    if len(expr) == 0:
        return 'NaN'

    # case 2: if just one element, return itself
    elif len(expr) == 1:
        return expr[0]

    # case 3: solve to reduce to 1 element (the answer)
    elif len(expr) > 1:
        while len(expr) != 1:
            expr_index = 0

            try:
                # skip to a op
                while not isinstance(expr[expr_index], list):
                    expr_index += 1

                # ---------- The Operators ---------- #

                # ~ bit inverse
                if expr[expr_index] == ['~', 2]:
                    # get the ~ of previous
                    result = operations.bit_inverse(expr[expr_index - 1])

                    # replace the value of previous location with result
                    expr[expr_index - 1] = result

                    # pop off op in expr
                    expr.pop(expr_index)

                # ! logical inverse
                elif expr[expr_index] == ['!', 2]:
                    # get the ! of previous
                    result = operations.logical_not(expr[expr_index - 1])

                    # replace the value of previous location with result
                    expr[expr_index - 1] = result

                    # pop off op in expr
                    expr.pop(expr_index)

                # * multiplication
                elif expr[expr_index] == ['*', 4]:
                    # get the * of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.multi(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # / division
                elif expr[expr_index] == ['/', 4]:
                    # get the / of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.divide(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # % mod
                elif expr[expr_index] == ['%', 4]:
                    # get the / of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.mod(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # + add (level 5)
                elif expr[expr_index] == ['+', 5]:
                    # get the + of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.add(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # - subtract (level 5)
                elif expr[expr_index] == ['-', 5]:
                    # get the - of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.sub(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # - unary (lv2)
                elif expr[expr_index] == ['-', 2]:
                    # get the neg of previous: (expr[i-1])
                    result = operations.unary_minus(expr[expr_index - 1])

                    # replace the value of location with result
                    expr[expr_index - 1] = result

                    # pop off op in expr
                    expr.pop(expr_index)

                # + unary (lv2)
                elif expr[expr_index] == ['+', 2]:
                    # get the unary + of previous: (expr[i-1])
                    result = operations.unary_plus(expr[expr_index - 1])

                    # replace the value of location with result
                    expr[expr_index - 1] = result

                    # pop off op in expr
                    expr.pop(expr_index)

                # << left shift
                elif expr[expr_index] == ['<<', 6]:
                    # get the << of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.left_shift(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # >> right shift
                elif expr[expr_index] == ['>>', 6]:
                    # get the >> of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.right_shift(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # <<< left rotate
                elif expr[expr_index] == ['<<<', 6]:
                    # get the <<< of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.left_rotate(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # >>> right rotate
                elif expr[expr_index] == ['>>>', 6]:
                    # get the + of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.right_rotate(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # < less than
                elif expr[expr_index] == ['<', 7]:
                    # get the < of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.lt(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                    # > greater than
                elif expr[expr_index] == ['>', 7]:
                    # get the > of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.gt(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # <= less than or equal to
                elif expr[expr_index] == ['<=', 7]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.lte(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # >= greater than or equal to
                elif expr[expr_index] == ['>=', 7]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.gte(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # == equal
                elif expr[expr_index] == ['==', 8]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.equal(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # != not equal
                elif expr[expr_index] == ['!=', 8]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.not_equal(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # & bitwise and
                elif expr[expr_index] == ['&', 9]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.bitwise_and(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # ^ bitwise XOR
                elif expr[expr_index] == ['^', 10]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.bitwise_xor(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # | bitwise or
                elif expr[expr_index] == ['|', 11]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.bitwise_or(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # && logical and
                elif expr[expr_index] == ['&&', 12]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.logical_and(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # ^^ logical XOR
                elif expr[expr_index] == ['^^', 13]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.logical_xor(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # || logical or
                elif expr[expr_index] == ['||', 14]:
                    # get the <= of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.logical_or(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # ---------- The Functions ---------- #

                # square
                elif expr[expr_index] == ['sq', 'func']:
                    # get the sq of previous: (expr[i-1])
                    result = operations.sq(expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 1] = result

                    # pop off op in expr
                    expr.pop(expr_index)

                # min
                elif expr[expr_index] == ['min', 'func']:
                    # get the min of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.min(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # max
                elif expr[expr_index] == ['max', 'func']:
                    # get the max of previous two: (a=expr[i-2], b=expr[i-1])
                    result = operations.max(expr[expr_index - 2], expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 2] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                    # pop off b in expr
                    expr.pop(expr_index - 1)

                # absolute
                elif expr[expr_index] == ['abs', 'func']:
                    # get the abs of previous : (expr[i-1])
                    result = operations.abs(expr[expr_index - 1])

                    # replace the value of farthest location with result
                    expr[expr_index - 1] = result

                    # pop off op in expr
                    expr.pop(expr_index)
                else:
                    raise ValueError

                # increment loop
                expr_index += 1

            # not supported expr
            except Exception:
                return 'NaN'

        # return solved expr
        return expr[0]

    # just in case
    else:
        return 'NaN'
