# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:43:19 2023

@author: AMIT
"""

import cv2

cap = cv2.VideoCapture("E:/OpenCV/Video_Car.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    
    # convert BGR format to Grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('original',frame)
    cv2.imshow('Gray',gray_frame)
    
    k = cv2.waitKey(10) & 0xFF
    if k == ord('q') or k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()