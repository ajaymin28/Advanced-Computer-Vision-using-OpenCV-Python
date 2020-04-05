# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:21:01 2019

@author: Jaimin
"""

# import opencv
import cv2

# open webcam stream

vs = cv2.VideoCapture("sample.mp4")

# Show frames
while vs.isOpened():
    flag, frame = vs.read()
    if flag:
        cv2.imshow("Frame",frame)
        
    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
vs.release()
