# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# Import opencv
import cv2

# Read image
img = cv2.imread("src/cvforeveryone.png")


# gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Blur image
blurred = cv2.blur(gray,(3,3))

# Apply threshold
temp,th = cv2.threshold(blurred,100,255,cv2.THRESH_BINARY)

# Use trackbars

cv2.imshow("img",img)
cv2.imshow("th",th)
cv2.waitKey(0)
cv2.destroyAllWindows()