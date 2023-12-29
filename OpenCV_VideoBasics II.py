# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:04:36 2023

@author: AMIT
"""

import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("E:/OpenCV/Squat_Video.mp4")

# Capture a Video Frame
ret, frame = cap.read()

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# imshow() - To display an Image
plt.imshow(frame)

print("Display Frame Count:",cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Display Frame Height:",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Display Frame Width:",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Display Frame FPS:",cap.get(cv2.CAP_PROP_FPS))

cap.release()
