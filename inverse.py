import cv2 as cv
import numpy as np

def inverse_img(image):
    h, w, _ = image.shape
    for y in range(h):
        for x in range(w):
            blue = image[y, x, 0]
            green = image[y, x, 1]
            red = image[y, x, 2]
            image[y, x] = [255 - blue, 255 - green, 255 - red]
    return image

# read an image
img = cv.imread("./pics/nokorcode.webp")
img_copied = img.copy()

# convert image to inverted image
img_copied = inverse_img(img_copied)

# save the inverted image
cv.imwrite("inverted_image.jpg", img_copied)

# show original and inverted image
cv.imshow('Original Image', img)
cv.imshow('Inverted Image', img_copied)
cv.waitKey(0)
