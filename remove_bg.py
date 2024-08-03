import cv2 as cv
import numpy as np

class bgr:
    def __init__(self, b, g, r):
        self.b = b
        self.g = g
        self.r = r

def inverse_img(image, pic, bg):
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      blue = image[y, x, 0]
      green = image[y, x, 1]
      red = image[y, x, 2]

      if (blue > 100 and green > 100 and red > 100):
        image[y, x] = [bg.b, bg.g, bg.r]
      else:
        image[y, x] = [pic.b, pic.g, pic.r]

  return image

# Read an image
img = cv.imread("brain.jpg")

# Create ColorObject instances
bg = bgr(141, 232, 195)
pic = bgr(0, 0, 255) 

# Apply inverse_img function
result_img = inverse_img(img, pic, bg)

# Show image
cv.imshow('Test Image', result_img)
cv.waitKey(0)
cv.destroyAllWindows()
