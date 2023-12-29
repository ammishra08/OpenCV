# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:28:17 2023

@author: AMIT
"""

import cv2
import numpy as np

img = cv2.imread("E:/OpenCV/pug.jpg")

circles = np.zeros((2,2), int)
counter = 0

def mousePosition(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)
        
roi = img[67:390,447:815]

cv2.imshow("Original", img)
cv2.setMouseCallback('Original', mousePosition)
cv2.imshow("ROI", roi)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()