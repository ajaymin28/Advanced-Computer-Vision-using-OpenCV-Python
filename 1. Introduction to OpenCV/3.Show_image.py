# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:00:46 2019

@author: Jaimin
"""

# import opencv
import cv2

# Read image
img  = cv2.imread("glasses.jpg")

# Show image
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()