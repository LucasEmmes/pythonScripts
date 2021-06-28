import random

def miller_rabin_factor(n):
    """
    Will factorise n to be the form of 2^v * u + 1

    RETURNS:
        tuple: (v, u)
    """


    if n % 2 == 0:
        print("Please only enter odd numbers")
        return False

    v = 0
    u = n - 1

    while u % 2 == 0:
        u = u // 2
        v += 1
    
    return v, u

def miller_rabin_test(n):
    """
    Implementation of the Miller-Rabin primality test. Returns false if n is /definitely/ composite.

    Should be run multiple times for safety.
    """

    factors = miller_rabin_factor(n)
    if factors == False:
        return False
    else:
        v, u = factors

    a = random.randint(2, n-2)

    b = a**u % n

    if b == 1 or b == n-1:
        return True
    
    else:
        for j in range(0, v-1):
            
            b = b**2 % n

            if b == n-1:
                return True
    
    return False