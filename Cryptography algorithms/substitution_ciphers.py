import random

def simple_substitute(text, alphabet, code):
    """
    Used to encode or decode the given text based on the provided alphabet.
    PARAMS:
        plaintext (string): The message you want to encode
        alphabet (dictionairy[char] = char): Key is plaintext char, value is the substitute. Enter the same alphabet for both encode and decode
        code (int): Whether to encode (0) or decode (1)
    RETURNS:
        string: The decoded plaintext or encoded ciphertext
    """

    if code == 0:
        
        plaintext = text
        ciphertext = ""

        for plainChar in plaintext:
            ciphertext += alphabet[plainChar]

        return ciphertext

    elif code == 1:

        ciphertext = text
        plaintext = ""

        #   Reverting alphabet
        decodeAlphabet = {}
        for key in alphabet.keys():
            decodeAlphabet[alphabet[key]] = key

        for cipherChar in ciphertext:
            plaintext += decodeAlphabet[cipherChar]

        return plaintext


def poly_substitute(text, alphabet, code):
    """
    Used to encode or decode the given text based on the provided poly-alphabet.
    PARAMS:
        plaintext (string): The message you want to encode.
        alphabet (dictionairy[char] = array[chars]): Key is plaintext char, value is array of one or more substitute(s). Enter the same alphabet for both encode and decode
        code int: Whether to encode (0) or decode (1)
    RETURNS:
        string: The decoded plaintext or encoded ciphertext
    """
    
    if code == 0:   # Encode

        plaintext = text
        ciphertext = ""

        for plainChar in plaintext:
            #   Randomly picks a substitute
            randomIndex = random.randint(0,len(alphabet[plainChar])-1)
            ciphertext += alphabet[plainChar][randomIndex]

        return ciphertext

    elif code == 1: # Decode

        ciphertext = text
        plaintext = ""

        #   Reverting alphabet
        decodeAlphabet = {}
        for key in alphabet.keys():
            for sub in alphabet[key]:
                decodeAlphabet[sub] = key

        for cipherChar in ciphertext:
            plaintext += decodeAlphabet[cipherChar]

        return plaintext

# Coded by Lucas Emmes some time during quarantine