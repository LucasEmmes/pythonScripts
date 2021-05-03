import numpy as np
import math

roman_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def hill_cipher(message, key, alphabet=roman_uppercase):
    # Key setup
    key_matrix = np.array(key)
    d1, d2 = key_matrix.shape
    if d1 != d2:
        print("Key is not square!")
        return None
    length = d1*d2
    print(f"key length {length}")
    print(f"message length {len(message)}")
    
    # Padding the message
    diff = (length - (len(message) % length)) % length
    print(f"diff {diff}")
    for i in range(diff):
        message += alphabet[-1]

    print(f"padded message: {message}")
    
    # Cutting up message and doing math
    num_of_blocks = len(message) // d1
    pt = []
    try:
        for i in range(num_of_blocks):
            block = []
            for j in range(d1):
                block.append([alphabet.index(message[i*d1+j])])
            pt.append(block)
    except:
        print("Encountered a character not present in alphabet")
        return None
    pt = np.array(pt)

    print(f"PLAINTEXT: {pt}")

    # print(pt)

    # Encrypting
    ct = []
    for block in pt:
        ct_block = np.matmul(key_matrix, block)
        ct.append(ct_block)
    
    print(f"CIPHERTEXT: {ct}")
    # print(ct)

    ct_string = ""
    for block in ct:
        for character in block:
            ct_string += alphabet[character[0] % (len(alphabet)-1)]

    return ct_string

ct = hill_cipher("ONCE UPON A TIME", [[4, 5], [1, 7]])
print(ct)
pt = hill_cipher(ct, [[15, 19], [9, 16]])
print(pt)