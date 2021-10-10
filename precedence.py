# dictionary containing function names
functions = {
    'abs': None,
    'sq': None,
    'min': None,
    'max': None
}

# dictionary containing operators and their precedence level
operators = {
    # LEVEL 1
    '(': 1,
    ')': 1,
    '[': 1,
    ']': 1,

    # LEVEL 2
    '~': 2,
    '!': 2,

    # LEVEL 4
    '*': 4,
    '/': 4,
    '%': 4,

    # LEVEL 5
    '-': 5,
    '+': 5,

    # LEVEL 6
    '<<': 6,
    '>>': 6,
    '<<<': 6,
    '>>>': 6,

    # LEVEL 7
    '<': 7,
    '>': 7,
    '<=': 7,
    '>=': 7,

    # LEVEL 8
    '==': 8,
    '!=': 8,

    # LEVEL 9
    '&': 9,

    # LEVEL 10
    '^': 10,

    # LEVEL 11
    '|': 11,

    # LEVEL 12
    '&&': 12,

    # LEVEL 13
    '^^': 13,

    # LEVEL 14
    '||': 14
}
