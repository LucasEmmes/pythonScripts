from functools import cache

@cache
def lucas_number(n):
    """
    Gives the n-th Lucas-number. Kinda looks like Fibonacci.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return lucas_number(n - 1) + lucas_number(n - 2)


def lucas_lehmer_test(n):
    """
    Tests for primality of n and returns a boolean

    True - Propbably prime | False - Definitely composite
    """
    if (lucas_number(n)-1) % n == 0:
        return True
    else:
        return False