import cv2 as cv
# import numpy as np
  
# reverse image from top to bottom
def mirror_y_axis(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  j = 0
  for y in reversed(range(h)) : 
    i = 0 
    for x in (range(w)) :
      copy_img[j, i] = image[y, x]
      i += 1
    j += 1
  return copy_img


# reverse image from from left to right
def mirror_x_axis(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  
  j = 0
  for y in (range(h)) : 
    i = 0 
    for x in reversed(range(w)) :
      copy_img[j, i] = image[y, x]
      i += 1
    j += 1
  return copy_img


# reverse image from from left to right and top to bottom
def mirror_xy_axis(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  
  j = 0
  for y in reversed(range(h)) : 
    i = 0 
    for x in reversed(range(w)) :
      copy_img[j, i] = image[y, x]
      i += 1
    j += 1
  return copy_img


      
# read an image
img = cv.imread("./pics/tall.png")
new_img = img.copy()


# convert image to gray image
new_img = mirror_xy_axis(new_img)

# show image
cv.imshow('Original img', img)
cv.imshow('New img', new_img)
cv.waitKey(0)

