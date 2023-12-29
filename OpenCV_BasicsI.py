# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:22:33 2023

@author: AMIT
"""

import cv2

img = cv2.imread("E:/OpenCV/parrot.jpg")
# opencv reads image in BGR Format 
print(img)

# convert BGR format to Grayscale
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('frame1', img)
cv2.imshow('frame2', img_g)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()