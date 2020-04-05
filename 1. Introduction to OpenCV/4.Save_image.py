# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:02:29 2019

@author: Jaimin
"""


# import opencv
import cv2

# Read image
img = cv2.imread("glasses.jpg")

# RGB to Gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Save image
cv2.imwrite("glasses_gray.jpg",gray)

# Show images
cv2.imshow("RGB",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()