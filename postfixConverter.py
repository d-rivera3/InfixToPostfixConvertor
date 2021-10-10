# take in information of an expression and convert it into postfix format

from precedence import functions


def postfix_converter(expr_parts, is_which, is_pres):
    operations_stack = []   # stack to track of operators and precedence
    stack = []  # resulting postfix

    # index of expr_parts list and operations_stack size
    index = 0
    op_stack_size = 0

    '''use is_pres and is_which to make op_stack'''
    # print(expr_parts)
    while index < len(expr_parts):

        # print(index, end='\t')
        # print(expr_parts, end='\n')
        # print(stack, end='\n')
        # print(operations_stack, end='\n')

        # numbers get a clear pass into stack, and functions passed into operations_stack
        if is_which[index] == int:
            stack.append(expr_parts[index])
        elif is_which[index] == 'func':
            operations_stack.append([expr_parts[index], 'func'])    # pass [function name, 'func'] to tell what it is
            op_stack_size += 1

        # operators the complicated part

        # initial operator
        elif is_which[index] == 'op' and len(operations_stack) == 0:

            # add op and precedence
            operations_stack.append([expr_parts[index], is_pres[index]])    # [operator, operator's level]
            op_stack_size += 1

        # handle open parentheses '('
        elif is_which[index] == 'op' and expr_parts[index] == '(':

            # add op and precedence
            operations_stack.append([expr_parts[index], is_pres[index]])  # [operator, operator's level]
            op_stack_size += 1

        # handle close parentheses ')'
        elif is_which[index] == 'op' and expr_parts[index] == ')':
            # pop off operations into stack until '(' found
            while op_stack_size != 0 and operations_stack[op_stack_size-1][0] != '(':
                stack.append(operations_stack.pop(op_stack_size - 1))
                op_stack_size -= 1

            # pop off '(' but do not add to stack
            operations_stack.pop(op_stack_size - 1)
            op_stack_size -= 1

            # check if function is next, usually before the beginning of a '(' so add as well
            if op_stack_size != 0 and operations_stack[op_stack_size - 1][1] == 'func':
                stack.append(operations_stack.pop(op_stack_size - 1))
                op_stack_size -= 1

        # other operators besides '()'
        elif is_which[index] == 'op':
            # handle (
            if operations_stack[op_stack_size - 1][0] == '(':
                # add op and precedence
                operations_stack.append([expr_parts[index], is_pres[index]])
                op_stack_size += 1

            # if a 'func'
            elif operations_stack[op_stack_size - 1][1] == 'func':
                # add op and precedence
                operations_stack.append([expr_parts[index], is_pres[index]])
                op_stack_size += 1

            # if current op precedence == to top operations_stack op (lower pres)
            elif is_pres[index] == operations_stack[op_stack_size - 1][1]:
                # dealing with unary
                if is_pres[index] == 2 and operations_stack[op_stack_size - 1][1] == 2:
                    operations_stack.append([expr_parts[index], is_pres[index]])
                    op_stack_size += 1
                # else regular op
                else:
                    stack.append(operations_stack.pop(op_stack_size - 1))
                    op_stack_size -= 1

                    operations_stack.append([expr_parts[index], is_pres[index]])
                    op_stack_size += 1

            # if new op higher precedence than top of stack
            elif is_pres[index] < operations_stack[op_stack_size - 1][1]:
                # add op and precedence
                operations_stack.append([expr_parts[index], is_pres[index]])
                op_stack_size += 1

            # if new op lower precedence than top of stack
            elif is_pres[index] > operations_stack[op_stack_size - 1][1]:
                # pop off op in stack that are of higher precedence
                while op_stack_size != 0 and is_pres[index] > operations_stack[op_stack_size - 1][1]:
                    stack.append(operations_stack.pop(op_stack_size - 1))
                    op_stack_size -= 1

                    # check if function ahead, usually the beginning of a '(' so add and break
                    if op_stack_size != 0 and operations_stack[op_stack_size - 1][0] in functions:
                        stack.append(operations_stack.pop(op_stack_size - 1))
                        op_stack_size -= 1
                        break

                # add in new op into stack last
                operations_stack.append([expr_parts[index], is_pres[index]])
                op_stack_size += 1

        # handle commas
        elif is_which[index] == 'comma':
            # pop out any inner expr ops
            while op_stack_size != 0 and operations_stack[op_stack_size - 1][0] != '(':
                stack.append(operations_stack.pop(op_stack_size - 1))
                op_stack_size -= 1

        # increment index
        index += 1

    # pop remaining operators
    if operations_stack:
        while op_stack_size != 0:
            stack.append(operations_stack.pop(op_stack_size - 1))
            op_stack_size -= 1

    # return postfix stack
    return stack
