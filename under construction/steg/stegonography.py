from PIL import Image
import math
import sys


# image = Image.open("rei.png")
# x = image.size[0]
# y = image.size[1]
# imageSpace = x*y

# pixels = image.load()

def decimal_to_binary(n, length):
    return bin(n)[2:].rjust(length, "0")[0:length]

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

def check_metadata(filename):

    image = Image.open(filename)
    x, y = image.size
    pixels = image.load()

    l1 = get_from_pixel(pixels[x-3, y-1], 6)
    l2 = get_from_pixel(pixels[x-2, y-1], 6)
    sdf = get_from_pixel(pixels[x-1, y-1], 3)
    
    image.close()

    bits = l1 + l2 + sdf[3:]
    sanity = 0

    for bit in bits:
        if bit == "1":
            sanity += 1

    if decimal_to_binary(sanity, 3) == sdf[0:3]:
        return (binary_to_decimal(l1+l2), binary_to_decimal(sdf[3:6]), binary_to_decimal(sdf[6:]))
    
    print("No metadata found")
    return False

def read_pixel(filename, n):
    image = Image.open(filename)
    x, y = image.size
    print(f"Dimensions: {x}x-{y}y")
    pixels = image.load()
    image.close()

    if n < 0:
        # print(f"Last pixel available: {x*y-1}")
        n += x * y
        # print(f"Looking for pixel number: {n} at {n%x}, {n//x}")
        
    return pixels[n%x, n//x]

def get_hidden_dimensions(filename):
    metadata = check_metadata(filename)
    if metadata:
        filetype = metadata[2]
        if filetype == 1 or filetype == 2:
            hx = get_from_pixel(read_pixel(filename, -4), 4)
            hy = get_from_pixel(read_pixel(filename, -5), 4)
            return (hx, hy)

        print("No image is hidden")
    return False

# STRING ENCODE AND DECODE
def text_to_binary(text):
    bitstring = ""

    for char in text:
        dec = ord(char)
        bin = decimal_to_binary(dec, 9)
        bitstring += bin
    
    return bitstring

def binary_to_string(bitstring):
    text = ""

    for i in range(0, len(bitstring), 9):
        binary_character = bitstring[i:i+9]

        text += chr(binary_to_decimal(binary_character))
    
    return text


# BITSTRING IN AND OUT OF PNG
def insert_bitstring_into_png(bitstring, image, depth, filetype):
    x, y = image.size
    pixels = image.load()
    
    # Calculate space available and check
    num_of_pixels_available = (x+1)*(y+1) - 3
    pixels_required = math.ceil(len(bitstring) / (3 * depth))
    if num_of_pixels_available < pixels_required:
        raise ValueError(f"Length of data is too long! Max limit is {num_of_pixels_available * 3 * depth}, and your data is {len(bitstring)}!")

    bs_length = len(bitstring)

    # Pad bitstring
    desired_length = pixels_required * 3 * depth
    bitstring.ljust(desired_length, "0")

    # Cut bitstring into correctly sized pieces
    characters = []
    for i in range(0, len(bitstring), 3*depth):
        characters.append(bitstring[i:i+3*depth])

    # Insert each piece into pixel
    for i in range(len(characters)):
        p = pixels[i//y, i%x]
        pixels[i//y, i%x] = add_to_pixel(characters[i], pixels[i//y, i%x])

    # Add metadata to the end
    metadata_length = decimal_to_binary(bs_length, 36)
    metadata_filetype = decimal_to_binary(filetype, 3)
    metadata_depth = decimal_to_binary(depth, 3)
    
    sanity_check = 0
    for md in [metadata_length, metadata_depth, metadata_filetype]:
        for char in md:
            if char == "1":
                sanity_check += 1
    
    metadata_sanity = decimal_to_binary(sanity_check, 3)

    pixels[x-3, y-1] = add_to_pixel(metadata_length[0:18], pixels[x-3, y-1])
    pixels[x-2, y-1] = add_to_pixel(metadata_length[18:], pixels[x-2, y-1])
    pixels[x-1, y-1] = add_to_pixel(f"{metadata_sanity}{metadata_depth}{metadata_filetype}", pixels[x-1, y-1])

    return True

def extract_bitstring_from_png(filename):
    # Image loading prep work
    image = Image.open(filename)
    x, y = image.size
    pixels = image.load()

    # Get metadata
    try:
        bs_length, depth, filetype = check_metadata(filename)
    except:
        print("No data could be found")
        return False

    # Start extracting bitstream
    bitstring = ""
    for i in range(math.ceil(bs_length / (3 * depth))):
        bitstring += get_from_pixel(pixels[i//y, i%x], depth)

    bitstring = bitstring[:bs_length]

    # Convert bitstream based on filetype
    if filetype == 0:
        # print("Text file")
        output = binary_to_string(bitstring)
    

    return (filetype, output)


def text_into_image(text_filename, image_filename, depth, output_filename):
    textfile = open(text_filename, "r")
    text_to_hide = textfile.read()
    textfile.close()
    bitstring = text_to_binary(text_to_hide)

    image = Image.open(image_filename)
    insert_bitstring_into_png(bitstring, image, depth, 0)

    extension = ".png"
    if output_filename.lower().endswith(".png"):
        extension = ""
    image.save(f"{output_filename}{extension}")
    return True


def main():

    # EXTRACTION
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        
        # Check if PNG
        if filename.lower().endswith(".png"):

            check = check_metadata(filename)
            if check:
                filetype, output = extract_bitstring_from_png(filename)

                if filetype == 0:
                    output_file = open("extracted_data.txt", "w", encoding="utf-8")
                    output_file.write(output)
                    output_file.close()

                    print("Done")
                
                else:
                    print("Could not parse filetype")
            
            else:
                print("Could not find any data hidden in this image")

        else:
            print("Can only extract data from PNG images")


    # INJECTION
    elif len(sys.argv) == 5:
        
        hidden_file = sys.argv[1]
        injection_file = sys.argv[2]
        depth = int(sys.argv[3])
        output_file = sys.argv[4]

        # Hide txt file
        if hidden_file.lower().endswith(".txt"):
            print("txt file ok")
            if injection_file.lower().endswith(".jpg") or injection_file.lower().endswith(".png"):
                print("yes")
                text_into_image(hidden_file, injection_file, depth, output_file)



if __name__=="__main__":main()

# img = Image.open("gunnar.jpg")
# bs = text_to_binary("you little shits better show up to the fucking cunt ass 17:30 class today. else im gonna shit on your grades :)")
# insert_bitstring_into_png(bs, img, 2, 0)
# img.save("gunnar_hidden.png")
# img.close()

# print(extract_bitstring_from_png("borgir.png"))





# goddamn
