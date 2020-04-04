# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# Import opencv
import cv2

# Import numpy with alias
import numpy as np

# Create Blank image using Numpy
img = np.zeros((500,500,3),dtype="uint8")


def nothing(val):
    print(val)

# Create Trackbars for RGB each which holds value from 0 to 255.
cv2.namedWindow("img")
cv2.createTrackbar("R","img",0,255,nothing)
cv2.createTrackbar("B","img",0,255,nothing)
cv2.createTrackbar("G","img",0,255,nothing)

while True:
    r = cv2.getTrackbarPos("R","img")
    b = cv2.getTrackbarPos("B","img")
    g = cv2.getTrackbarPos("G","img")
    img[:] = [b,g,r]
    cv2.imshow("img",img)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()