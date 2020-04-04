# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:12:37 2019

@author: Jaimin
"""


# Import opencv
import cv2

# Import numpy with alias
import numpy as np

# Read image
img = cv2.imread("src/cow.jpg")


# Create a kernal
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")

sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")

# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")


sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")


from skimage.exposure import rescale_intensity

# Perform convolution operation on image
def convolution3d(kernel,img):
    if len(img.shape)>2:
        h,w,c = img.shape
        zeros = np.zeros((h,w,c), dtype="float32")
        for channel in np.arange(c):
            zeros[:,:,channel] = cv2.filter2D(img[:,:,channel],-1,kernel)
        zeros = rescale_intensity(zeros,in_range=(0,255))
        return zeros
    else:
        return cv2.filter2D(img,-1,kernel)
            

mykernel = np.array((
	[2, 1, -1],
	[3, -1, -1],
	[-1, -1, -1]), dtype="int")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
conv = convolution3d(mykernel,img)

cv2.imshow("img",img)
cv2.imshow("conv",conv)
cv2.waitKey(0)
cv2.destroyAllWindows()












"""
capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    if _:
        cnv3d = convolution3d(mykernel,frame)
        cnv3d = cv2.flip(cnv3d,1)
        stackedImg = np.hstack((frame,cnv3d))
        cv2.imshow("con",stackedImg)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
"""
# Show updated image
