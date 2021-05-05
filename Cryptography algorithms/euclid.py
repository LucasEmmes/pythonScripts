def euclid(a, b):
    """
    Applies the Euclidean algorithm to find gcd(a, b)
    PARAMS:
        a (int)
        b (int)
    RETURNS:
        int: The greatest common demoninator
    """
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    q = a % b

    return euclid(b, q)

def euclid_extended(a, b):
    """
    Applies the Euclidean algorithm and returns an array that may be used to calculate the GCD in the form a*x + b*y = 1
    PARAMS:
        a (int)
        b (int)
    RETURNS:
        array: A formatted array
    """
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
    """
    Help function for extended_euclid
    """
    for i in range(len(arr)):

        element = arr[i]

        if type(element) == list:
            arr[i] = deep_replace(element, x, y)
        else:
            if element == x:
                arr[i] = y
    
    return arr

def deep_calculate(arr, a, b):
    """
    Help function for invert_mod
    """
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
    """
    Calculates the inverse modulus (if it exists)
    PARAMS:
        x (int): The integer to invert
        n (int): The modulus
    RETURNS:
        int: The inverse modulus x^-1 mod(n)
    """
    gcd = euclid(x, n)

    if gcd != 1:
        print(f"Cannot invert as the gcd is {gcd} and not 1")
        return None

    if x > n:
        x = x%n
    
    arr = euclid_extended(x, n)
    ax, by = deep_calculate(arr, n, x)

    if by < 0:
        return (by + n) % n
    return by
