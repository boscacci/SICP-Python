"""Exercise 1.8.  

Newton's method for cube roots is based on the fact that if y is an 
approximation to the cube root of x, then a better approximation is 
given by the value:

(x / y**2 + 2y) / 3


Use this formula to implement a cube-root procedure analogous to the 
square-root procedure.
"""

def good_enough(guess, x, conf_interval):
    cond1 = (guess ** 3) < (x + conf_interval)
    cond2 = (guess ** 3) > (x - conf_interval)
    return True if (cond1 and cond2) else False

def make_better_guess(x, guess):
    return ((x / guess**2 + 2*guess) / 3)


def cub_rt(x, guess=1):
    if good_enough(guess, x, 0.001):
        return guess
    else:
        return cub_rt(x, make_better_guess(x, guess))