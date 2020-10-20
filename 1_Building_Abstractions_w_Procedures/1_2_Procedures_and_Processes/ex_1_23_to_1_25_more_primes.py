from math import sqrt
from time import time


def better_smallest_divisor(n, test_divisor=2):
    """
    Find N's smallest divisor; useful for primality testing
    f(n) = O(sqrt(n))
    """
    if test_divisor > sqrt(n):
        # At this point we know it's a prime
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return smallest_divisor(n, increment_test_divisor(test_divisor))


def increment_test_divisor(td):
    return 3 if td == 2 else td + 2


def better_is_prime(n):
    return True if better_smallest_divisor(n) == n else False


def better_timed_prime_test(n):
    # print(f"n: {n};")
    start_time = time()
    if better_is_prime(n):
        dur = time() - start_time
        print(f"*** Dur: {dur:.7f}")
        return True
    return False


def better_search_for_primes(p, q):
    primes = list()
    if p % 2 == 0:
        p += 1
    while p < q and (len(primes) < 3):
        if better_timed_prime_test(p):
            primes.append(p)
        p += 2
    return primes


from ex_1_21_to_1_22_primes import *

first_tuple = (500_000, 700_000)

print("Old: \n")
search_for_primes(*first_tuple)

print("New: \n")
better_search_for_primes(*first_tuple)

"""
Why isn't this procedure twice as fast as the one in the previous module,
exercise 1.22?

From the forum:
The observed ratio of the speed of the two algorithms is not 2, but 
roughly 1.5 (or 3:2).

This is mainly due to the increment_test_divisor procedure's IF test. 
The input did halve indeed, but we need to do an extra IF test.
"""