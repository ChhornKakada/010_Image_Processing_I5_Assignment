import cv2 as cv
import numpy as np
  
def convert_to_greyScale(image) :
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      pixel = image[y, x]
      blue, green, red = pixel
      gray_value = int((0.299 * blue) + (0.587 * green) + (0.114 * red))
      image[y, x] = [gray_value, gray_value, gray_value]
  return image
      
# read an image
img = cv.imread("./pics/apples.png")
img_copied = img.copy()

# convert image to gray image
img_copied = convert_to_greyScale(img_copied)

# show image
cv.imshow('Original', img)
cv.imshow('Gray Scale Img', img_copied)
cv.waitKey(0)

