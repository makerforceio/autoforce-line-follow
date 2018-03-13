#!/usr/bin/env python

import numpy as np
import cv2 as cv

c_width = 1/20

def line_follow(frame): #Returns (angle, lean)
    mask = cv.inRange(frame, np.array([0, 0, 0]), np.array([100, 100, 100]))
    mask = cv.blur(mask, (10,10))
    mask = cv.threshold(mask, 100, 255, cv.THRESH_BINARY)[1]
    
    contours = cv.findContours(mask, 1, cv.CHAIN_APPROX_NONE)[1]

    if len(contours) > 0:
        cnt = max(contours, key=cv.contourArea)
        
        rect = cv.minAreaRect(cnt)
        angle = rect[2]
        if rect[1][0] > rect[1][1]:
            angle = 90 + angle
        
        if (cv.contourArea(cnt) < 0.01 * (frame.shape[0] * frame.shape[1])):
            return None
        cv.drawContours(frame, [cnt], 0, (0,255,0), 1)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        cv.drawContours(frame,[box],0,(0,0,255),2)
        if angle < -30 or angle > 30:
            return frame, (angle, None)

        cx = int(rect[0][0])
        cv.line(frame,(cx,0),(cx,frame.shape[0]),(255,0,0),3)
        return frame, (angle, rect[0][0] - frame.shape[1]/2)
    else:
        return None
