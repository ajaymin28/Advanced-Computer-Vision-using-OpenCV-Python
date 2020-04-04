# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# Import opencv
import cv2


# Read image
img = cv2.imread("src/cow.jpg")

# Show image
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Crop image by array slicing
cropped = img[0:115,0:115,:]

cv2.imshow("cropped",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
