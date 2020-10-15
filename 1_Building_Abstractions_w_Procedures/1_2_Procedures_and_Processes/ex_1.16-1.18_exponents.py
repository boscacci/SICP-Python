def expt_broke(b, n):
    return 1 if n == 0 else (b * expt(b, n - 1))


def expt_better(b, n, p=1):
    if n == 0:
        return p
    else:
        return expt_better(b, n - 1, b * p)


def expt_woke(b, n, p=1):
    if n == 0:
        return p
    elif n % 2 == 0:
        return expt_woke(b ** 2, n / 2, p)
    else:
        return expt_woke(b, n - 1, b * p)


def mul(a, b):
    """Exercise 1.18"""
    if b == 1:
        return a
    elif b % 2 == 0:
        return mul(a + a, b / 2)
    else:
        return a + mul(a, b - 1)
