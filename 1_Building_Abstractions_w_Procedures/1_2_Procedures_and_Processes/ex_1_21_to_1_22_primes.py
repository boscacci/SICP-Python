from math import sqrt


def euclid_gcd(a, b):
    """
    Find the Greatest common divisor of p and q by euclid's
    f(n) = O(log(n))
    """
    if b == 0:
        return a
    return euclid_gcd(b, a % b)


def smallest_divisor(n, test_divisor=2):
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
        return smallest_divisor(n, test_divisor + 1)


def is_prime(n):
    return True if smallest_divisor(n) == n else False


def fermat_test(n):
    """
    Woke probabilistic test for primality
    """
    from random import randint

    # Select some number smaller than n:
    a = randint(1, n - 1)
    return True if are_congruent(a ** n, a, n) else False


def are_congruent(a, b, n):
    """
    Two numbers are said to be congruent modulo n if they both have the
    same remainder when divided by n.
    """
    left = a % n
    right = b % n
    return True if left == right else False


def power_fermat(n, iterations=30):
    """Runs fermat test a few times; even one failure means not prime"""
    for _ in range(iterations):
        if not fermat_test(n):
            return False
    return True


"""
Exercise 1.21.  
Use the smallest-divisor procedure to find the smallest divisor 
of each of the following numbers: 199, 1999, 19999.
"""

print(f"Smallest divisors:{[smallest_divisor(n) for n in (199, 1999, 19999)]}")

"""
Exercise 1.22.  
The following timed-prime-test procedure, when called with an integer n, 
prints n and checks to see if n is prime. If n is prime, the procedure 
prints three asterisks followed by the amount of time used in performing 
the test:
"""


def timed_prime_test(n):
    from time import time
    # print(f"n: {n};")
    start_time = time()
    if is_prime(n):
        dur = time() - start_time
        print(f"*** Dur: {dur:.7f}")
        return True
    return False


"""
Using this procedure, write a procedure search-for-primes that checks 
the primality of consecutive odd integers in a specified range. Use your 
procedure to find the three smallest primes larger than 1000; larger 
than 10,000; larger than 100,000; larger than 1,000,000. Note the time 
needed to test each prime. 
"""


def search_for_primes(p, q):
    primes = list()
    if p % 2 == 0:
        p += 1
    while p < q and (len(primes) < 3):
        if timed_prime_test(p):
            primes.append(p)
        p += 2
    return primes


search_for_primes(1000, 3000)
search_for_primes(10_000, 15_000)
# search_for_primes(1_000_000, 1_100_000)

