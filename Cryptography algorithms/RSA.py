import math
import random

def RSA_generate_keys(*args):
    """
    Generates a pair of public and private RSA keys
    
    PARAMS:
        *args: ((int), (int)) tuple with two prime numbers that you wish to be used. Can be ommited, in which case it will generate a random set for you (not implemented yet)
    RETURNS:
        If *args were provided (int, int, int): (e, d, N) tuple used for encrypting / decrypting your messages
        Otherwise (int, int, int, int, int): (e, d, N, p, q) tuple used for encrypting / decrypting your messages
    """

    # p, q = prime1, prime2
    if len(args) == 2:
        p, q = args
    else:
        pass
        # TODO: get numbers from prime genmerator
    
    # N = pq
    N = p*q
    # phi(N) = (p-1)(q-1)
    phi_N = (p-1)*(q-1)

    # e = 1 < e < phi(N), coprime to N, phi(N)
    e_candidates = []
    for i in range(2, phi_N):
        if (math.gcd(i, phi_N) == 1):
            e_candidates.append(i)
    # Pick a random e (optional)
    e = e_candidates[random.randint(0, len(e_candidates)-1)]

    # d = d*e % phi(N) = 1
    d = 0
    for i in range(phi_N):
        if i*e % phi_N == 1:
            d = i
            break

    if len(args) == 2:
        return e, d, N
    
    return p, q, e, d, N

def RSA_encrypt(e, N, m):
    """
    Encrypts your message using the provided keys p, q
    """
    if m > N:
        print(f"Message is too large!\nPlease make sure it is less than {N}")
        raise ValueError

    return m**e % N

# m = c**d % n
def RSA_decrypt(d, N, c):
    """
    Decrypts your message using the provided key d
    """
    return c**d % N

# TESTING FROM HERE. REMOVE IF YOU DONT NEED IT
def RSA_demo():
    m = 42069
    p, q = 523, 541

    print(f"Provided primes were p={p}, q={q}")

    e, d, N = RSA_generate_keys(p, q)
    print(f"e={e}, d={d}, N={N}")

    ct = RSA_encrypt(e, N, m)
    print(f"Message {m} was encrypted as {ct}")

    pt = RSA_decrypt(d, N, ct)
    print(f"Ciphertext {ct} was decrypted as {pt}")

    pause = input("Press enter to exit")

RSA_demo()
