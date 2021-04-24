import cv2
import numpy as np

width = 1200
height = 800
j = 1j

image = np.full((height,width), 255, np.uint8)
scale = 350
it = 50

def test_complex(c):
    z = c**2 + c
    for i in range(it):
        try:
            z = z**2 + c
            if z != z:
                return False
        except OverflowError:
            return False
    return True

for y in range(height):
    for x in range(width):
        x1 = x-width/1.5
        y1 = y-height/2
        c = (x1 + y1*j)/scale
        if test_complex(c):
            image[y][x] = 0

    if y%5 == 0:
        cv2.imshow("Mandelbrot", image)
        cv2.waitKey(1)

print("Finished")
cv2.waitKey(0)

# Coded by Lucas Emmes on 02/03/21
# I did this instead of studying for a test :^)
