# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# Import opencv
import cv2

# Import numpy with alias

# Read image
img = cv2.imread("src/glasses.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray,100,255)

# Eroding the image
erode = cv2.erode(canny,(3,3),iterations=1)

# Dialating the image
dilate = cv2.dilate(canny,(3,3),iterations=1)

# Show updated image

cv2.imshow("img",img)
cv2.imshow("canny",canny)
cv2.imshow("erode",erode)
cv2.imshow("dial",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
