# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:22:19 2019

@author: Jaimin
"""


# import opencv
import cv2
import numpy as np


img = np.zeros((500,500,3),dtype="uint8")

colorV = 0
    
while True:
    img = cv2.line(img,(0,0),(500,500),(colorV,0,0),5)
    img = cv2.line(img,(500,0),(0,500),(0,colorV,0),5)
    cv2.imshow("img",img)
    if colorV>254:
        colorV = 0
    else:
        colorV +=1
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()

x = 1

def f():
    x = 2
    return x
    
class C(object):
    x = 2

if True:
    x = 4
    
f()
C()
print(x)

