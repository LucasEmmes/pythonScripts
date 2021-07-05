from PIL import Image
import random


# image = Image.open("rei.png")
# x = image.size[0]
# y = image.size[1]
# imageSpace = x*y

# pixels = image.load()

def decimal_to_binary(n, length):
    return bin(n)[2:].rjust(length, "0")

def binary_to_decimal(b):
    return int(b, 2)

def get_binary_array(tup):
    binary_pixel = []
    for color in tup:
        binary_pixel.append(decimal_to_binary(color, 8))
    return binary_pixel

def add_to_pixel(bitstring, pixel):
    # bitstring must be multiple of 3
    # pixel is (r, g, b) 0-255

    # Checks
    if type(bitstring) != str:
        raise TypeError("Bitstring must be string")
    elif type(pixel) != tuple:
        raise TypeError("Pixel must be tuple")
    elif len(pixel) != 3:
        raise ValueError("Pixel must be a 3-tuple (R,G,B)")
    elif len(bitstring) % 3 != 0:
        raise ValueError("Bitstring must be a multiple of 3")
    elif len(bitstring) == 0 or len(bitstring) > 24:
        raise ValueError("Bitstring can must be between 3 and 24 characters (both inclusive)")
    
    # Split up bitstring
    deltas = []
    delta_length = len(bitstring)//3

    for i in range(3):
        deltas.append(bitstring[i*delta_length:(i+1)*delta_length])
    
    # Convert rgb values
    binary_pixel = get_binary_array(pixel)

    # Insert bitstring
    # Turn back into decimal
    for i in range(3):
        binary_pixel[i] =binary_to_decimal(binary_pixel[i][0:8-delta_length] + deltas[i])
    
    # Finito
    return (binary_pixel[0], binary_pixel[1], binary_pixel[2])

def get_from_pixel(pixel, depth):
    # Turn into binary
    binary_pixel = get_binary_array(pixel)

    # Retrieve slice from each pixel
    bitstring = ""
    for binary_color in binary_pixel:
        bitstring += binary_color[8-depth:]
    
    return bitstring