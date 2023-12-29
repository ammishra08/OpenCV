# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:17:15 2023

@author: AMIT
"""

import cv2

cap = cv2.VideoCapture("E:/OpenCV/Video.avi")

while (cap.isOpened()):
    ret, frame = cap.read()
    # increase the video resolution
    # fx = scale factor along horizontal axis
    # fy = scale factor along vertical axis
    frame = cv2.resize(frame, (840,680), fx = 200, fy = 300, 
                       interpolation = cv2.INTER_NEAREST)
    cv2.imshow('Original', frame)
    
    # Average Blur
    img_blur = cv2.blur(frame, (5,5))
    cv2.imshow('Blur', img_blur)

    # Median Blur
    m_blur = cv2.medianBlur(frame, 7)
    cv2.imshow('Median Blur', m_blur)

    # Gaussian Blur, sigmaX(stdDev)= 1
    g_blur = cv2.GaussianBlur(frame, (7,7), 1)
    cv2.imshow('Gaussian Blur', g_blur)
    
    k = cv2.waitKey(10) & 0xFF
    if k == ord('q') or k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()