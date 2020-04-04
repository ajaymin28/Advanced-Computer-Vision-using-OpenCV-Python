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

# Draw Line
cv2.line(img,(0,0),(250,250),(255,0,0),2)

# Draw Circle
cv2.circle(img,(250,250),50,(0,255,0),2)

# Draw Rectangle
cv2.rectangle(img,(10,10),(100,100),(0,0,255),2)


# Put text
cv2.putText(img,"CV For Everyone",(10,150),cv2.FONT_HERSHEY_SIMPLEX,1,(23,14,255))

# Show image
cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
