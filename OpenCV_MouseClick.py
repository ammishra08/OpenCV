# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:14:14 2023

@author: AMIT
"""

import cv2
import numpy as np

circles = np.zeros((4,2), int)
counter = 0

def mousePosition(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)
        
img = cv2.imread("E:/OpenCV/cards.jpg")

cv2.imshow("Original", img)
cv2.setMouseCallback('Original', mousePosition)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()