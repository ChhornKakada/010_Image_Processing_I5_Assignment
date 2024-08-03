import cv2 as cv
# import numpy as np

class bgr:
    def __init__(self, b, g, r):
        self.b = b
        self.g = g
        self.r = r

def to_binary_img(image):
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      blue = image[y, x, 0]
      green = image[y, x, 1]
      red = image[y, x, 2]
      threshold = ((blue + green + red)/3)/255
      print(threshold)
      if threshold > 0.5:
        image[y, x] = [255, 255, 255]
      else:
        image[y, x] = [0, 0, 0]

  return image

# Read an image
img = cv.imread("./pics/image.png")

# Apply inverse_img function
result_img = to_binary_img(img)

# Show image
cv.imshow('Test Image', result_img)
cv.waitKey(0)
cv.destroyAllWindows()
