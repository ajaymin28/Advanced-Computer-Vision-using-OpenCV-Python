# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# Import opencv
import cv2
import numpy as np

# numpy addition
img = cv2.imread("src/blue.jpg")
img1 = cv2.imread("src/green.jpg")


# cv2 addition
final = cv2.add(img,img1)

npadd = img + img1
# Read images


# cv2 add weighted (image blending)
final = cv2.addWeighted(img,1,img1,1,1)

# cv2 subtract 

# Show image
cv2.imshow("result",final)
cv2.waitKey(0)
cv2.destroyAllWindows()




