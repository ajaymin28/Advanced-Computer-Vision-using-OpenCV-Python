# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""

# import opencv
import cv2
import numpy as np

# Read image
img = cv2.imread("src/cow.jpg")

# Flip Image Vertically
imgvf = cv2.flip(img,flipCode=0)

# Flip Image Horizontally
imghf = cv2.flip(img,flipCode=1)

# Flip Image Vertically and Horizontally
imgvhf = cv2.flip(img,flipCode=-1)


#stack image
hstack1 = np.hstack((img,imghf))
hstack2 = np.hstack((imgvf,imgvhf))

final_img = np.vstack((hstack1,hstack2))

# Show all Images
cv2.imshow("final img",final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
