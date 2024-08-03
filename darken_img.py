import cv2 as cv

# function for reduce each value of intensity
def reduce(value, modify_value):
  value = value - modify_value
  value = 0 if value < 0 else value
  return value


# reduce rgb value of intensiry
def darken_intensity(red, green, blue, modify_value):
  red = reduce(red, modify_value)
  green = reduce(green, modify_value)
  blue = reduce(blue, modify_value)
  return red, green, blue
  
  
# for darken the img by modify value
def darken_img(image, modify_value) :
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      pixel = image[y, x]
      blue, green, red = pixel
      red, green, blue = darken_intensity(red, green, blue, modify_value)
      image[y, x] = [blue, green, red]
  return image
      
      
# read an image
img = cv.imread("./pics/apples.png")
new_img = img.copy()

new_img = darken_img(new_img, 100)

# show image
cv.imshow('Original img', img)
cv.imshow('New img', new_img)
cv.waitKey(0)

