#!/usr/bin/env python

import cv2 as cv

cap = cv.VideoCapture(0)

from line_follow import *

while (True):
    frame = cap.read()[1]

    out = line_follow(frame)
    if out is None:
        continue
    frame, (angle, lean) = out
    print(angle)
    print(lean)
    
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
                break

    
