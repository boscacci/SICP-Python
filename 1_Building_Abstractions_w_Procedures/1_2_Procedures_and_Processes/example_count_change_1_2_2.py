"""
How many different ways can we make change of $ 1.00, given 
half-dollars, quarters, dimes, nickels, and pennies? More generally, 
can we write a procedure to compute the number of ways to change any 
given amount of money?

The number of ways to change amount a using n kinds of coins equals:

* the number of ways to change amount a using all but the first kind of coin, plus
* the number of ways to change amount a - d using all n kinds of coins, where 
    d is the denomination of the first kind of coin.


Scheme LISP:
(define (count-change amount)
  (cc amount 5))
(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (= kinds-of-coins 0)) 0)
        (else (+ (cc amount
                     (- kinds-of-coins 1))
                 (cc (- amount
                        (first-denomination kinds-of-coins))
                     kinds-of-coins)))))
(define (first-denomination kinds-of-coins)
  (cond ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)))
"""


def count_change(amt, n_kinds=5):
    """This breaks my Python recursion depth, oh well"""
    if amt == 0:
        return 1
    elif amt < 0:
        return 0
    else:
        L = count_change(amt, n_kinds - 1)
        R = count_change(amt - first_denom[n_kinds], n_kinds)
        return L + R


first_denom = {1: 1, 2: 5, 3: 10, 4: 25, 5: 50}

