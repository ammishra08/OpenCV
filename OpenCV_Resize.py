# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:40:42 2023

@author: AMIT
"""
# Resize an Image

import cv2
import imutils

img = cv2.imread("E:/OpenCV/pug.jpg")

# It takes height and width of image and reshapes to 500x500
img_resize = cv2.resize(img, (700,700))

img_resize1 = imutils.resize(img, width = 900)

cv2.imshow('Original', img)
cv2.imshow('Reshape', img_resize)
cv2.imshow('Reshape1', img_resize1)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()
