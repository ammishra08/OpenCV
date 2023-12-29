# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:29:12 2023

@author: AMIT
"""

import cv2

img = cv2.imread("E:/OpenCV/noisy_image.jpg")
 
# Median Blur
m_blur = cv2.medianBlur(img, 3)

# Gaussian Blur, sigmaX(stdDev)= 1
g_blur = cv2.GaussianBlur(img, (7,7), 1)

cv2.imshow('Original', img)
cv2.imshow('median', m_blur)
cv2.imshow('gaussian', g_blur)


# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()

