import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 160)
video_capture.set(4, 120)

while(True):

    # Capture the frames
    ret, frame = video_capture.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ret,thresh = cv2.threshold(gray,70,255, cv2.THRESH_BINARY_INV)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)    
    if len(contours) >= 1:
        cnt = contours[0]
    
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(frame, approx, -1, (0, 0, 255), 3)
    
    cv2.imshow('frame',frame)
    cv2.imshow('thrash',thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
    
    #hull = cv2.convexHull(cnt)
