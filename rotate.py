import numpy as np
import cv2 as cv


# rotate the img to left side
def rotate_left(img):
  h, w, _ = img.shape
  # image = np.zeros((height, width, 3), np.uint8)
  new_img = np.zeros((w, h, 3), np.uint8)
  new_h, new_w, _ = new_img.shape
  # j for y and i for x
  i = new_w - 1
  for y in range(h):
    j = 0
    for x in range(w):
      new_img[j, i] = img[y, x]
      j += 1
    i -= 1
  return new_img


# rotate the img to right side
def rotate_right(img):
  h, w, _ = img.shape
  # image = np.zeros((height, width, 3), np.uint8)
  new_img = np.zeros((w, h, 3), np.uint8)
  new_h, new_w, _ = new_img.shape
  # j for y and i for x
  i = 0
  for y in range(h):
    j = new_h - 1
    for x in range(w):
      new_img[j, i] = img[y, x]
      j -= 1
    i += 1
  return new_img
      
    
# read an image
img = cv.imread("./pics/tall.png")
# convert image to gray image
new_img = rotate_right(img)


# show image
cv.imshow('Original img', img)
cv.imshow('New img', new_img)
cv.waitKey(0)
