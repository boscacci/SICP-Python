# Exercise 1.4.
# Observe that our model of evaluation allows for combinations whose
# operators are compound expressions. Use this observation to describe
# the behavior of the following procedure:

""" SCHEME LISP:
(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))
"""

"""Unfortunately, in Python, we cannot return the addition operator.
"""

# Python translation:


def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b


# I.e., for concision:


def a_plus_abs_b_short(a, b):
    return a + b if b > 0 else a - b


# a_plus_abs_b(3,4) returns the same as a_plus_abs_b(3,-4).

# I.e., sort of more lispy:
# Here we can simulate returning an add/subtract operator:
def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def a_plus_abs_b_functional(x, y):
    plus_or_minus = plus if y > 0 else minus
    return plus_or_minus(x, y)


# That does the same thing.
