# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# import opencv
import cv2

# Read image
img = cv2.imread("src/cow.jpg")

# Rotate Image by angle
imgr = cv2.rotate(img,rotateCode=2)

# img center/shape
h,w,c = img.shape
center = (h//2,w//2)

rotation_matrix = cv2.getRotationMatrix2D(center,-15,0.75)
final_rotated = cv2.warpAffine(img,rotation_matrix,(w,h))




# Show rotated image
cv2.imshow("original",img)
cv2.imshow("rotated",final_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()