import re


def lexer(raw_input):
    return re.findall(r'\d+|add|subtract|multiply|divide|\(|\)', raw_input)


def baby_lisp(input):
    return parse(lexer(input))


def parse(tokens):
    token = tokens.pop(0)

    if token in ['(', ')']:
        return parse(tokens)
    elif token == 'add':
        return parse(tokens) + parse(tokens)
    elif token == 'subtract':
        return parse(tokens) - parse(tokens)
    elif token == 'multiply':
        return parse(tokens) * parse(tokens)
    elif token == 'divide':
        return parse(tokens) / parse(tokens)
    else:
        return int(token)



assert baby_lisp("(add 1 2)") == 3
assert baby_lisp("(multiply 4 (add 2 3))") == 20
assert baby_lisp("(multiply (add (subtract 2 1) (multiply 5 1)) (add 2 3))") == 30
