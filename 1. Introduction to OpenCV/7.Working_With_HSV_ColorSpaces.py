# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:19:13 2019

@author: Jaimin
"""


# Import opencv
import cv2

# Import numpy with alias
import numpy as np

# Read image(RGB)
img = cv2.imread("glasses.jpg")

# Convert RGB to HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Seperate channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Display Hue Channel
# Display Saturation Channel
# Display Value Channel
cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)
cv2.waitKey(0)
cv2.destroyAllWindows()
