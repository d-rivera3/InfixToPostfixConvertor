# main to run program

from expressionSplitter import expr_splitter    # to split expr strings into list of parts
from classify import is_which                   # to identify parts and operator levels
from postfixConverter import postfix_converter  # to convert split expr list into postfix form
from evaluator import evaluate                  # to solve the expression


def main():

    # relative path to infix file (from current directory to file)
    infix_file = r'infix\infix.txt'
    convert = open(infix_file)

    # relative path to postfix file to output postfix form
    postfix_location = r'postfix\postfix.txt'
    write_postfix = open(postfix_location, 'w')

    # relative path to output file to output expression answer
    output_location = r'postfix\output.txt'
    write_output = open(output_location, 'w')

    # postfix expr list
    postfix_form = []
    # output list of answers
    answer_output = []

    # read expression lines and convert
    for line in convert.readlines():
        # print(line)

        # split line into parts
        parts = expr_splitter(line)
        # print(parts)

        # get what type and precedence of each part
        is_type, is_pres = is_which(parts)

        # print(is_type)
        # print(is_pres)

        postfix_form = postfix_converter(parts, is_type, is_pres)
        # print(postfix_form, end='\n\n')

        # convert postfix_form list into a string instead
        postfix_string = ''
        for part in postfix_form:
            # remember postfix_converter has ops as [operator, pres_level] and functions as [name, 'func'] in its output
            if isinstance(part, list):
                postfix_string += str(part[0]) + ','
            # otherwise it is a numeric value
            else:
                postfix_string += str(part) + ','
        postfix_string = postfix_string[:-1]  # removes extra comma at the end
        postfix_string += '\n'  # put a newline at the end

        # write postfix_string into postfix file
        write_postfix.writelines(postfix_string)

        # Evaluate answer for expression
        answer = evaluate(postfix_form)
        # print(answer)
        answer_output.append(answer)    # add answer to output list

    # close files
    convert.close()
    write_postfix.flush()
    write_postfix.close()

    # write the output answers to file
    for x in answer_output:
        y = str(x) + '\n'
        write_output.writelines(y)
    # close file
    write_output.flush()
    write_output.close()


main()  # run main
