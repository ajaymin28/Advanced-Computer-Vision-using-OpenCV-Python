# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:15:48 2019

@author: Jaimin
"""


# Import opencv
import cv2

# Read image(RGB)
img = cv2.imread("glasses.jpg")

# Seperate channels
B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

import numpy as np

def get_rgb(s_img,channel=0):
    w,h = s_img.shape
    RGB = np.zeros((w,h,3),dtype="uint8")
    RGB[:,:,channel] = s_img
    return RGB

blue = get_rgb(B,channel=0)

green = get_rgb(G,channel=1)

Red = get_rgb(R,channel=2)

# Display Red Channel
# Display Blue Channel
# Display Green Channel
cv2.imshow("B",blue)
cv2.imshow("G",green)
cv2.imshow("R",Red)
cv2.waitKey(0)
cv2.destroyAllWindows()

