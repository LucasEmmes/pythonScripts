import math
import random

def RSA_generate_keys(*args):

    # p, q = prime1, prime2
    if len(args) == 2:
        p, q = args
    
    # N = pq
    N = p*q
    # phi(N) = (p-1)(q-1)
    phi_N = (p-1)*(q-1)

    # e = 1 < e < phi(N), coprime to N, phi(N)
    e_candidates = []
    for i in range(2, phi_N):
        if (math.gcd(i, N) == 1) and (math.gcd(i, phi_N) == 1):
            e_candidates.append(i)
    # Pick a random e (optional)
    e = e_candidates[random.randint(0, len(e_candidates)-1)]

    # d = de % phi(N) = 1
    d = 0
    for i in range(phi_N):
        if i*e % phi_N == 1:
            d = i
            break

    if len(args) == 2:
        return e, d, N
    
    return e, d, N

def RSA_encrypt(e, N, m):
    if m > N:
        print(f"m is too large!\nPlease make sure it is less than {N}")
        raise ValueError

    return m**e % N

# m = c**d % n
def RSA_decrypt(d, N, c):
    return c**d % N

def RSA_test():
    m = 42069
    p, q = 523, 541

    e, d, N = RSA_generate_keys(p, q)
    print(f"e={e}, d={d}, N={N}")


    ct = RSA_encrypt(e, N, m)
    print(f"Message {m} was encrypted as {ct}")

    pt = RSA_decrypt(d, N, ct)
    print(f"Ciphertext {ct} was decrypted as {pt}")

RSA_test()