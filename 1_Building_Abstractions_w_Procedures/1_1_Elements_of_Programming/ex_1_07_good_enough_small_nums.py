"""
Exercise 1.7.
"""


def good_enough(guess, x, conf_interval):
    cond1 = (guess ** 2) < (x + conf_interval)
    cond2 = (guess ** 2) > (x - conf_interval)
    return True if (cond1 and cond2) else False


def make_better_guess(x, guess):
    return (guess + (x / guess)) / 2


def root(x, guess=1):
    if good_enough(guess, x, 0.001):
        return guess
    else:
        return root(x, make_better_guess(x, guess))


"""
Explain the following statements, with examples showing how the test 
fails for small and large numbers:

The good-enough? test used in computing square roots will not be very 
effective for finding the square roots of very small numbers.
"""
# Explanation
"""
When our good_enough test is only accurate to the thousandths place,
we will lose precision when calculating the sqrt of small-ass numbers

# >>> root(.00000000000008)**2
0.0009765625000532812 # This should be closer to zero

# >>> root(.00000000000000000008)**2
0.0009765625 # Okay now we're losing precision

# >>> root(.000000000000000000000000000000000008)**2
0.0009765625 # Same answer as before? Not good. Bad computer

"""
# Explain This Statement:
"""
Also, in real computers, arithmetic operations are almost always 
performed with limited precision. This makes our test inadequate for 
very large numbers.

"""
# Explanation:
"""
# >>> root(800000000000)**2
800000000000.0004 # Not ideal.

# >>> root(8000000000000)**2 # Bigger number
RecursionError: maximum recursion depth exceeded in comparison # Also a snag
"""
# Continued question:
"""
An alternative strategy for implementing good-enough? is to watch how 
guess changes from one iteration to the next and to stop when the 
change is a very small fraction of the guess. 

Design a square-root procedure that uses this kind of end test. Does 
this work better for small and large numbers?
"""
# Python:


def sqrt_alt(x, guess=1, delta=1):
    # breakpoint()
    if delta < (guess / 1000):
        return guess
    else:
        ret = sqrt_alt(
            x=x,
            guess=make_better_guess(x, guess),
            delta=abs(guess - make_better_guess(x, guess))
        )
        return ret
