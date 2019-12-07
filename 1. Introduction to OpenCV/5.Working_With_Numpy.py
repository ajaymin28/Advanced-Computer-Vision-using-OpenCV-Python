# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:09:04 2019

@author: Jaimin
"""

"""
If you dont understand what to do, please look at this video content I have made for you:  https://youtu.be/QxI-GRIfBvM

You can find full course playlist here: https://www.youtube.com/playlist?list=PLwRoxHWReaEhVFjTeKlifKUimbw6ZyV7K

"""

# Import opencv


# Import numpy with alias

# Create blank image using numpy

# Show blank image

# do something with blank image


# show updated image




















# Import opencv
import cv2
# Import numpy with alias
import numpy as np
import timeit
import time
import imutils

# Create blank image using numpy
img = np.zeros((500,500,3),dtype="uint8")
h,w = img.shape[:2]
img = cv2.line(img,(0,0),(h,w),(255,0,0),3)

# Show blank image
cv2.imshow("blank",img)


def rotate_imutils(img,angle):
    return imutils.rotate(img,angle)

def rotate_function(img,angle):
    rotation_mat = cv2.getRotationMatrix2D((img.shape[0]/2,img.shape[1]/2),angle,1.0)
    return cv2.warpAffine(img,rotation_mat,(img.shape[0],img.shape[1]))


for i in range(1,15):
    print("index: {} feature:{} supported: {}".format(i,cv2.getHardwareFeatureName(i),cv2.checkHardwareSupport(i)))

start = time.time()
ri = rotate_imutils(img,90)
end = time.time()
print("Total time taken by imutils {}".format(end-start))

start = time.time()
rf= rotate_function(img,90)
end = time.time()
print("Total time taken by rotate function {}".format(end-start))

# do something with blank image
cnt = 0
while True:
    img = img + cnt
    # Show image
    cv2.imshow("after operation",img)
    
    if cnt>254:
        cnt = 0
    else:
        cnt +=1
    
    # waitkey and destroy window
    keyboard = cv2.waitKey(30)
    if keyboard == 27:
        break

cv2.destroyAllWindows()