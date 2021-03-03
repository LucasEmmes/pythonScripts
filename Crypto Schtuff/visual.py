from PIL import Image
import random

def visual_encode(filename):

    original = Image.open(filename)
    plaintext = original.convert("1")
    
    plaintextSize = plaintext.size
    pixels = plaintext.load()
    totalPixelCount = plaintextSize[0] * plaintextSize[1]

    oneTimePad = [random.randint(0,1) for i in range(2*totalPixelCount)]
    
    share1 = Image.new(mode="1", size=plaintextSize)
    share2 = Image.new(mode="1", size=plaintextSize)

    for y in range(0, plaintextSize[1]):
        for x in range(0, plaintextSize[0]):
            share1.putpixel((x,y), (oneTimePad[y*plaintextSize[1]+x]))

    for y in range(0, plaintextSize[1]):
        for x in range(0, plaintextSize[0]):
            if plaintext.getpixel((x,y)) == 255:
                share2.putpixel((x,y), (oneTimePad[y*plaintextSize[1]+x]))
            elif plaintext.getpixel((x,y)) == 0:
                share2.putpixel((x,y), ((oneTimePad[y*plaintextSize[1]+x]+1)%2))
    
    plaintext.close()
    
    share1.save("ct_s1.png")
    share2.save("ct_s2.png")
    share1.close()
    share2.close()
    print(f"Succesfully encoded {filename}!\n")
            

def visual_decode(share1, share2):

    s1 = Image.open(share1)
    s2 = Image.open(share2)

    dimensions = s1.size

    if s1.size != s2.size:
        print("DEFINETLY NOT SHARES OF SAME IMAGE. DIMENSIONS DONT MATCH")
        raise ValueError

    plaintext = Image.new(mode="1", size=dimensions)

    for y in range(0, dimensions[1]):
        for x in range(0, dimensions[0]):
            p1 = s1.getpixel((x, y))
            p2 = s2.getpixel((x, y))

            if p1 == p2:
                plaintext.putpixel((x,y), (1))
            else:
                plaintext.putpixel((x,y), (0))

    s1.close()
    s2.close()

    plaintext.save("decoded_plaintext.png")
    plaintext.close()
    print(f"Succesfully decoded shares!\n")


def main():
    while True:
        command = int(input("Encode [0] / Decode [1]: "))
        if command:
            print("Please enter the name of the ciphertext shares (with extensions):")
            s1 = input("Share 1: ")
            s2 = input("Share 2: ")
            visual_decode(s1, s2)
        else:
            print("Please enter the name of the plaintext image (with extension):")
            pt = input("Plaintext: ")
            visual_encode(pt)

main()
    
# Coded by Lucas Emmes some time during quarantine
