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
    print(lisp_string)
    brackets_1 = re.sub(r"\)", "))", lisp_string)
    brackets_2 = "" + brackets_1
    mults = re.sub(r"multiply\s+", "multiply(", brackets_2)
    adds = re.sub(r"add\s+", "add(", mults)
    subtracts = re.sub(r"subtract\s+", "subtract(", adds)
    divides = re.sub(r"divide\s+", "divide(", subtracts)
    commas = re.sub(r" ", ",", divides)

    print(commas)
    return eval(commas)


assert baby_lisp("(add 1 2)") == 3

assert baby_lisp("(multiply 4 (add 2 3))") == 20

assert baby_lisp("(multiply (add (subtract 2 1) (multiply 5 1)) (add 2 3))") == 30
