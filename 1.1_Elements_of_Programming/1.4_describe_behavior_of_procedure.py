# Exercise 1.4.
# Observe that our model of evaluation allows for combinations whose
# operators are compound expressions. Use this observation to describe
# the behavior of the following procedure:

""" SCHEME LISP:
(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))
"""

"""Unfortunately in Python, I cannot return a "plus" sign, as far as I know.
"""

# Python translation:


def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b


# I.e.


def a_plus_abs_b_short(a, b):
    return a + b if b > 0 else a - b


# a_plus_abs_b(3,4) returns the same as a_plus_abs_b(3,-4).
