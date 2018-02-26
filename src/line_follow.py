#!/usr/bin/env python

import cv2 as cv

c_width = 1/20

def line_follow(frame): #Returns (angle, lean)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    mask = cv.threshold(gray, 30, 255, cv.THRESH_BINARY_INV)[1]
    mask = cv.GaussianBlur(mask, (5,5), 0)
    
    contours = cv.findContours(mask, 1, cv.CHAIN_APPROX_NONE)[1]
    
    if len(contours) > 0:
        cnt = max(contours, key=cv.contourArea)
        
        rect = cv.minAreaRect(cnt)
        angle = rect[2]

        M = cv.moments(cnt)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv.line(frame,(cx,0),(cx,frame.shape[0]),(255,0,0),3)
        
        cv.drawContours(frame, [cnt], 0, (0,255,0), 1)

        lean = 0
        if not (10 > angle > 10):
            lean = cx - frame.shape[0]/2

        return frame, (angle, lean)
        
    else:
        return None
