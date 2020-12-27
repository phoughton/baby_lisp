import re

# $ babyLisp(‘(add 1 2)’)
# $ 3
# $ babyLisp(‘(multiply 4 (add 2 3))’) 
# $ 20

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b


def baby_lisp(lisp_string):
    brackets = re.sub(r"\)", "))", lisp_string)
    commands = re.sub(r"([a-z]+) ", r"\1(", brackets)
    final = re.sub(r" ", ",", commands)

    return eval(final)


assert baby_lisp("(add 1 2)") == 3
assert baby_lisp("(multiply 4 (add 2 3))") == 20
assert baby_lisp("(multiply (add (subtract 2 1) (multiply 5 1)) (add 2 3))") == 30
