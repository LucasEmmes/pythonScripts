import math

def is_prime(x):
    if x % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
    return True

def euclid(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    q = a % b

    return euclid(b, q)

def euclid_extended(a, b):
    if a < b:
        a, b = b, a
    
    if a % b == 0:
        return None

    q = a % b
    
    r = euclid_extended(b, q)
    
    if r == None:
        return [a, [b, a // b]]
    else:
        n = [a, [b, a // b]]
        new_r = deep_replace(r, q, n)
        return new_r

def deep_replace(arr, x, y):
    for i in range(len(arr)):

        element = arr[i]

        if type(element) == list:
            arr[i] = deep_replace(element, x, y)
        else:
            if element == x:
                arr[i] = y
    
    return arr

def deep_calculate(arr, a, b):
    # INNER WILL ALWAYS BE B * Y
    if type(arr[0]) == int and type(arr[1]) == int:
        return 0, arr[1]
    else:
        # [[], int]]
        if type(arr[0]) == list and type(arr[1]) == int:
            x, y = deep_calculate(arr[0], a, b)
            x *= arr[1]
            y *= arr[1]
        # [int, []]
        elif type(arr[0]) == int and type(arr[1]) == list:
            x, y = deep_calculate(arr[1], a, b)
            if arr[0] == a:
                x = 1 - x
                y = -y
            else:
                y = 1 -y
                x = -x
        # [[], []]
        else:
            x1, y1, = deep_calculate(arr[0], a, b)
            x2, y2, = deep_calculate(arr[1], a, b)
            x = x1 - x2
            y = y1 - y2

        return x, y

def invert_mod(x, n):
    gcd = euclid(x, n)

    if gcd != 1:
        print(f"Cannot invert as the gcd is {gcd} and not 1")
        return None
    
    arr = euclid_extended(x, n)
    ax, by = deep_calculate(arr, n, x)

    if by < 0:
        return (by + n) % n
    return by
