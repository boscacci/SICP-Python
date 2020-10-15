"""Exercise 1.11.  
A function f is defined by the rule that 
if n < 3:
    f(n) = n  
and if n >= 3:
    f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) 
"""

# Write a procedure that computes f by means of a recursive process.


def func_rec(n):
    if n < 3:
        return n
    else:
        a = 1 * func_rec(n - 1)
        b = 2 * func_rec(n - 2)
        c = 3 * func_rec(n - 3)
        return a + b + c


# Now, write a procedure that computes f by means of an iterative process.
"""
HINT:
Consider the iterative method of getting the fibonacci sequence:
"""


def fib(n, a=0, b=1):
    """Gets the fibonacci sequence:"""
    if n == 0:
        return a
    else:
        prev = b
        nex = a + b
        return fib(n - 1, a=prev, b=nex)


# Now again, write a procedure that computes f by means of an iterative process.
"""
if n < 3:
    f(n) = n  
and if n >= 3:
    f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) 
"""

# I could not solve this within an hour and looked up an answer:


def func_iter(n, a=0, b=1, c=2):
    print(n, a, b, c)
    if n == 0:
        return a
    else:
        n -= 1
        alpha = b
        beta = c
        chi = c + (2 * b) + (3 * a)
        return func_iter(n, a=alpha, b=beta, c=chi)


# I've just translated from LISP but am still struggling to get it.
# I guess you need to store a countdown (n) and two temp vars (a and b)
# in order to compute the next (c) digit, but formulating this...idk
