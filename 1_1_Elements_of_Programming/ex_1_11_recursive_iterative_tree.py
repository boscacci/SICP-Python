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
        a = 1*func_rec(n-1)
        b = 2*func_rec(n-2)
        c = 3*func_rec(n-3)
        return a + b + c

# Write a procedure that computes f by means of an iterative process.
"""
HINT:
Consider the iterative method of getting the fibonacci sequence:

(define (fib n)
  (fib-iter 1 0 n))

(define (fib-iter a b count)
  (if (= count 0)
      b
      (fib-iter (+ a b) a (- count 1))))
"""

def fib(n, a=1, b=0):
    if n == 0:
        return b
    else:
        prev = a
        nex = a + b
        return fib(n-1, nex, prev)

# Now again, write a procedure that computes f by means of an iterative process.
"""
if n < 3:
    f(n) = n  
and if n >= 3:
    f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) 
"""

""" I could not solve this in an hour and looked up the answer.
 (define (f n) 
   (define (iter a b c count) 
     (if (= count 0) 
       a 
       (iter b c (+ c (* 2 b) (* 3 a)) (- count 1)))) 
   (iter 0 1 2 n)) 
"""
def func_iter(n, a=0, b=1, c=2):
    print(n, a, b, c)
    if n == 0:
        return a
    else:
        return func_iter(n = n - 1,
                         a = b, 
                         b = c, 
                         c = c + (2*b) + (3*a)
                        )

# I've just typed this out but still don't get it and am processing