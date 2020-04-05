# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""

# Import opencv.
import cv2

# Import numpy with alias
import numpy as np

# Read image
img = cv2.imread("glasses.jpg")

# Get/Print Pixel value
px1 = img[0,0,0]

img[0,0,0] = 123

# Set Pixel Value
px1_new = img[0,0,0]

# Show updated image
img[:,:,0] = 0
img[:,:,1] = 0

img[0:100,0:100,:] = 0

cv2.imshow("R",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
