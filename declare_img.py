import numpy as np
import cv2
import random

height, width = 1080, 1920
b, g, r = 0x3E, 0x88, 0xE5  # orange

# create a black img
image = np.zeros((height, width, 3), np.uint8)

for x in range(width):
  for y in range(height):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    image[y, x] = (b, g, r)
# image[:, :, 0] = b
# image[:, :, 1] = g
# image[:, :, 2] = r

cv2.imshow("A New Image", image)
cv2.waitKey(0)