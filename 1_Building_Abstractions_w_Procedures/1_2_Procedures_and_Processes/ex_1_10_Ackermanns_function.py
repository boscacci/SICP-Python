"""Exercise 1.10.  The following procedure computes a mathematical 
function called Ackermann's function.

(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1)
                 (A x (- y 1))))))

"""

def acker(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return acker(x-1, acker(x, y-1))

"""
What are the values of the following expressions?
"""
# 1. (A 1 10)
1024

# 2. (A 2 4)
65536

# 3. (A 3 3)
65536

"""
Consider the following procedures, where A is the procedure defined above:
Give concise mathematical definitions for the functions computed by 
the procedures f, g, and h for positive integer values of n. 

(define (k n) (* 5 n n))

For example, (k n) computes 5n2.
"""

# (define (f n) (A 0 n))
def f(n):
    """2n"""
    return acker(0,n)


# (define (g n) (A 1 n))
def g(n):
    """2**n"""
    return acker(1,n)

# (define (h n) (A 2 n))

def h(n):
    """2^2^…(n-1 times) — I had to look at this answer"""
    return acker(2,n)