# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:06:43 2023

@author: AMIT
"""

import cv2
import random

def noise_black_white(image):
    # Get the dimensions of Image
    row, col = image.shape
    num_of_pixels = random.randint(1500, 20000)
    for i in range(num_of_pixels):
        # pick random y-coordinate
        y_coordinate = random.randint(0, row - 1)
        # pick random x-coordinate
        x_coordinate = random.randint(0, col - 1)
        image[y_coordinate][x_coordinate] = 255
    for i in range(num_of_pixels):
        # pick random y-coordinate
        y_coordinate = random.randint(0, row - 1)
        # pick random x-coordinate
        x_coordinate = random.randint(0, col - 1)
        image[y_coordinate][x_coordinate] = 0
    return image

image = cv2.imread("E:/OpenCV/parrot.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image',noise_black_white(image))

cv2.imwrite("E:/OpenCV/noisy_image.jpg",noise_black_white(image))

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()
