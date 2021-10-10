# main to run program

from expressionSplitter import expr_splitter    # to split expr strings into list of parts
from classify import is_which                   # to identify parts and operator levels
from postfixConverter import postfix_converter  # to convert split expr list into postfix form


def main():

    # relative path to infix file (from current directory to file)
    infix_file = r'infix\infix.txt'
    convert = open(infix_file)

    # postfix expr list
    postfix_form = []

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

    # close files
    convert.close()


main()  # run main
