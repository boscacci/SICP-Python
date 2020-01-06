"""
Exercise 1.5.  Ben Bitdiddle has invented a test to determine whether 
the interpreter he is faced with is using applicative-order evaluation 
or normal-order evaluation. He defines the following two procedures:

(define (p) (p))

(define (test x y)
  (if (= x 0)
      0
      y))

Then he evaluates the expression

(test 0 (p))

What behavior will Ben observe with an interpreter that uses 
applicative-order evaluation?
"""

# "fully expand and then reduce" evaluation method is normal-order.
# "evaluate the arguments then apply" is applicative-order evaluation.
# The LISP interpreter uses applicative-order.


def p():
    return p()


def test(x, y):
    if x == 0:
        return 0
    else:
        return y

# What does this do in applicative order?
>>> test(0, p())

# First it tries to evaluate p, before passing to test function.
# This will result in an infinite recursive loop where the python
# interpreter tries to evaluate p which just keeps calling itself...

"""
What behavior will Ben observe with an 
interpreter that uses normal-order evaluation? Explain your answer.
"""
>>> test(0, p())

# The "test" function will receive the args before they're evaluated.
# Then it will test to see if x == 0 (True) and return 0. Finished.

"""
(Assume that the evaluation rule for the special form if is the same 
whether the interpreter is using normal or applicative order: The 
predicate expression is evaluated first, and the result determines 
whether to evaluate the consequent or the alternative expression.)
"""

