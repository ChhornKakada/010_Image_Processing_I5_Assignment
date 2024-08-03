import cv2 as cv
# import numpy as np
  
# reverse image from top to bottom
def changeBg(image) :
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      pixel = image[y, x]
      blue, green, red = pixel
      # red, green, blue = darken_intensity(red, green, blue, modify_value)
      if (red == 1 and green == 0 and blue == 5):
        image[y, x] = [54, 23, 54]
      elif (red == 255 and green == 253 and blue == 254):
        image[y, x] = [23, 54, 63]
  return image

# rgb(255, 253, 254)
# rgb(1, 0, 5)

img = cv.imread("./pics/nokorcode.webp")
new_img = img.copy()
new_img = changeBg(new_img)
cv.imshow('New img', new_img)
cv.waitKey(0)