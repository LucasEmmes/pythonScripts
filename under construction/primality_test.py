import math
import random

def bruteforce(p):
    if p % 2 == 0:
        return False
    
    sqrt = math.sqrt(p)
    if sqrt % 1 == 0:
        return False
    
    for i in range(3, math.ceil(sqrt)):
        if p % i == 0:
            return False

    return True

def fermat(p, a=0):
    if a != 0:
        if math.gcd(a, i) == 1:
            if a**(p-1)%p != 1:
                return False
            else:
                return True
        else:
            raise ValueError("p and a are not relatively prime!")

    else:
        for i in range(5):
            while True:
                a = random.randrange(2, p-1)
                if math.gcd(a, p) == 1:
                    break
                
            if math.gcd(a, p) == 1:
                if a**(p-1)%p != 1:
                    return False
        return True

# BUGGY DOESN'T WORK
def miller_rabin(n):
    if n%2 == 0:
        return False

    t = (n-1)
    v = 0
    
    while t % 2 == 0:
        v += 1
        t = t/2

    u = int(t)

    a = random.randrange(2, n-1)

    b = a**u % n

    if b == 1:
        print(n)
        return True
    else:
        for j in range(0, v):
            if b == -1:
                print(n)
                return True
            else:
                print(f"{b}**2 % {n} = {b**2 % n}")
                b = b**2 % n
        return False




    
