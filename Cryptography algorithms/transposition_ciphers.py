def ceasar_cipher(text, alphabet, k, code):
    """
    Will encode or decode given text based on the provided alphabet by transposition
    PARAMS:
        text (string): The text you would like to encode or decode
        alphabet (array[char] / string): List of all the available characters in order. May be one long string, or array of single characters
        k (int): The encryption key
        code (int): Whether you want to encode(0) or decode(1)
    RETURNS:
        string: Encoded ciphertext or decoded plaintext
    """

    if code == 0:

        encodingDictionairy = {}
        
        for i in range(0, len(alphabet)):
            encodingDictionairy[alphabet[i]] = alphabet[(i+k)%len(alphabet)]

        plaintext = text
        ciphertext = ""

        for plainChar in plaintext:
            ciphertext += encodingDictionairy[plainChar]

        return ciphertext

    elif code == 1:

        decodingDictionairy = {}

        for i in range(0, len(alphabet)):
            decodingDictionairy[alphabet[i]] = alphabet[(i-k)%len(alphabet)]

        ciphertext = text
        plaintext = ""

        for cipherChar in ciphertext:
            plaintext += decodingDictionairy[cipherChar]

        return plaintext




def vigenere(text, alphabet, k, code):
    """
    Will encode or decode given text based on the provided alphabet by transposition
    PARAMS:
        text (string): The text you would like to encode or decode
        alphabet (array[char] / string): List of all the available characters in order. May be one long string, or array of single characters
        k (array[int]): Array of integers to be used as keys. Period is determined by the length of the array. No padding is applied here
        code (int): Whether you want to encode(0) or decode(1)
    RETURNS:
        string: Encoded ciphertext or decoded plaintext
    """

    if code == 0:

        plaintext = text
        ciphertext = ""
        counter = 0

        for plainChar in plaintext:
            charIndex = alphabet.index(plainChar)
            ciphertext += alphabet[(charIndex + k[counter % len(k)]) % len(alphabet)]
        
            counter += 1

        return ciphertext

    elif code == 1:

        ciphertext = text
        plaintext = ""
        counter = 0

        for cipherChar in ciphertext:
            charIndex = alphabet.index(cipherChar)
            plaintext += alphabet[(charIndex - k[counter % len(k)]) % len(alphabet)]
        
            counter += 1

        return plaintext

# Coded by Lucas Emmes some time during quarantine
