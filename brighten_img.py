import cv2 as cv

# function for reduce each value of intensity
def plus(value, modify_value):
  value = value + modify_value
  value = 255 if value > 255 else value
  return value


# reduce rgb value of intensiry
def brighter_intensity(red, green, blue, modify_value):
  red = plus(red, modify_value)
  green = plus(green, modify_value)
  blue = plus(blue, modify_value)
  return red, green, blue
  
  
# for darken the img by modify value
def brighter_img(image, modify_value) :
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      pixel = image[y, x]
      blue, green, red = pixel
      red, green, blue = brighter_intensity(red, green, blue, modify_value)
      image[y, x] = [blue, green, red]
  return image
      
      
# read an image
img = cv.imread("./pics/apples.png")
new_img = img.copy()

new_img = brighter_img(new_img, 100)

# show image
cv.imshow('Original img', img)
cv.imshow('New img', new_img)
cv.waitKey(0)

