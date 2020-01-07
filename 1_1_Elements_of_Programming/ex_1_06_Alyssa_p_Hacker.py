"""
Exercise 1.6. Alyssa P. Hacker doesn't see why if needs to be 
provided as a special form. ``Why can't I just define it as an 
ordinary procedure in terms of cond?'' she asks. Alyssa's friend 
Eva Lu Ator claims this can indeed be done, and she defines a new 
version of if:

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))
"""

# Python translation:
def new_if(predicate, then_clause, else_clause):
    if predicate:
        return then_clause
    else:
        return else_clause


"""
Eva demonstrates the program for Alyssa:

(new-if (= 2 3) 0 5)
5

(new-if (= 1 1) 0 5)
0

"""

# Python:
>>> new_if(2 == 3, 0, 5)
5

>>> new_if(1 == 1, 0, 5)
0

"""
Delighted, Alyssa uses new-if to rewrite the square-root program:

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x)
                     x)))
"""

# Fast and loose Python translation:
def sqrt_iter(guess, x):
    return new_if(good_enough(guess, x), 
                  guess, 
                  (sqrt_iter(improve(guess, x), x))
           )
    
"""
What happens when Alyssa attempts to use this to compute square roots? 
Explain.
"""

# improve function defined separately

# Try it
>>> sqrt_iter(guess=5, x=10)
# Continue:
>>>>> return new_if(False, 5, sqrt_iter(((5 + 10/5) / 2), 10))
# Simplify:
>>>>> return new_if(False, 5, sqrt_iter((3.5, 10)))
>>>>> return sqrt_iter(3.5, 10)
>>>>> return new_if(False, 3.5, sqrt_iter(3.178, 10))
>>>>> return sqrt_iter(3.178, 10)
# I don't see why this shouldn't work. Prove me wrong with a PR