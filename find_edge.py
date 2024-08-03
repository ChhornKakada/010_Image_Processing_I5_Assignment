import cv2
import numpy as np

# Read the image
image = cv2.imread('./pics/kakada.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel kernels
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Compute gradients for each channel
G_x_red = cv2.filter2D(image[:, :, 2], -1, sobel_x)
G_y_red = cv2.filter2D(image[:, :, 2], -1, sobel_y)

G_x_green = cv2.filter2D(image[:, :, 1], -1, sobel_x)
G_y_green = cv2.filter2D(image[:, :, 1], -1, sobel_y)

G_x_blue = cv2.filter2D(image[:, :, 0], -1, sobel_x)
G_y_blue = cv2.filter2D(image[:, :, 0], -1, sobel_y)

# Compute gradient magnitudes for each channel
G_red = np.sqrt(G_x_red**2 + G_y_red**2)
G_green = np.sqrt(G_x_green**2 + G_y_green**2)
G_blue = np.sqrt(G_x_blue**2 + G_y_blue**2)

# Combine channels to get the final edge-detected image
final_edge_image = np.sqrt(G_red**2 + G_green**2 + G_blue**2)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edges', final_edge_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
