# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:59:07 2023

@author: AMIT
"""

# Apply smoothening of Image - Apply Blur
import cv2 
import numpy as np

img = cv2.imread("E:/OpenCV/child.jpg")

# Blur using Filter2D
kernel = np.ones((5,5), np.float32) / 25
print(kernel)

# Filter2D
smoothed = cv2.filter2D(img, -1, kernel)

# Average Blur
img_blur = cv2.blur(img, (5,5))

# Median Blur
m_blur = cv2.medianBlur(img, 7)

# Gaussian Blur, sigmaX(stdDev)= 1
g_blur = cv2.GaussianBlur(img, (7,7), 1)

cv2.imshow('Original', img)
cv2.imshow('Blur', smoothed)
cv2.imshow('average', img_blur)
cv2.imshow('median', m_blur)
cv2.imshow('gaussian', g_blur)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()
