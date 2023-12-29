# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:29:31 2023

@author: AMIT
"""

import cv2

cap = cv2.VideoCapture("E:/OpenCV/Video.avi")

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (840,680), fx = 200, fy = 300, 
                       interpolation = cv2.INTER_NEAREST)
    cv2.imshow('Original', frame)
    
    # convert BGR format to Grayscale
    img_g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    edges_low = cv2.Canny(img_g, 50, 150)
    edges_high = cv2.Canny(img_g, 150, 220)
 
    cv2.imshow('original',frame)
    cv2.imshow('Edges',edges_low)
    cv2.imshow('Edges High',edges_high)
    
    k = cv2.waitKey(60) & 0xFF
    if k == ord('q') or k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()