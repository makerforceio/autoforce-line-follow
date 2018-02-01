#!/usr/bin/env python

import rospy
import sys
import numpy as np
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
	def __init__(self):
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("image_topic", Image, self.callback)
		self.cv_image = None

	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBrdigeError as e:
			print e

	def get_latestcv2Image():
		return self.cv_image

# video_capture = cv2.VideoCapture(0)
# video_capture.set(3, 160)
# video_capture.set(4, 120)

while(True):
    ret, frame = video_capture.read()
    crop_img = frame[60:120, 0:160]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
    _,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

        if cx >= 120:
            print "Turn Left!"

        if cx < 120 and cx > 50:
            print "On Track!"

        if cx <= 50:
            print "Turn Right"

    else:
        print "I don't see the line"

    cv2.imshow('frame',crop_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
