# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:43:43 2023

@author: AMIT
"""

import cv2
import imutils

face_cascade = cv2.CascadeClassifier("E:/OpenCV/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("E:/OpenCV/haarcascade_eye.xml")

# Read Image
img = cv2.imread("E:/OpenCV/child.jpg")

# Resize the image
img_r = imutils.resize(img, width = 1000)

# Convert Image to GrayScale
gray = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)
# 1.3 = threshold value for scale factor, 5 = Num of nearest neighbouring features
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    # Draw the rectangle
    cv2.rectangle(img_r, (x,y),(x+w, y+h), (255,255,255), 2)
    # ROI is region of face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img_r[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 3)
    for (ex,ey,ew,eh) in eyes:
        # Draw the rectangle
        cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,0,0), 2)
        
cv2.imshow('frame', img_r)
cv2.waitKey(0)
cv2.destroyAllWindows()
