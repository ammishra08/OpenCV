# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:39:59 2023

@author: AMIT
"""

import cv2

img = cv2.imread("E:/OpenCV/girl.jpg")

cv2.imshow('Original', img)
# convert BGR format to Grayscale
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny(image, threshold1, threshold2)
# Computing Edge Gradient with canny thresholds
# The edge gradients that are greater tha threshold value will be detected as Edges
# thresholds lower than threshold1 will not be considered as edges.
edges_low = cv2.Canny(img_g, 50, 120)
cv2.imshow('Edge Detection', edges_low)

edges_high = cv2.Canny(img_g, 60, 200)
cv2.imshow('High Edge Detection', edges_high)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()