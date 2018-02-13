#!/usr/bin/env python

import rospy
import sys
import numpy as np
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageConverter:
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

def main(args):
	ic = ImageConverter()
	rospy.init_node('line_follower', anonymous=True)

	rate = rospy.Rate(10)
    
    c_width = 1/20
	
	while not rospy.is_shutdown():
		frame = ic.get_latestcv2Image()
        size = frame.size()
        gray = cv2.cvtColor(frame, cv1.COLOR_BGR2GRAY)
		mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)[1]
        mask = cv2.GaussianBlur(mask, (5,5), 0)
        
		contours = cv2.findContours(mask, 1, cv2.CHAIN_APPROX,NONE)[1]
        
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            
            rect = cv2.minAreaRect(cnt)
            angle = rect[2]
            
            print "Rotate {}".format(angle)
            
            M = cv2.moments(c)

            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            cv2.line(frame,(cx,0),(cx,size[1]),(255,0,0),3)
            
            cv2.drawContours(frame, contours, -1, (0,255,0), 1)

            if cx >= size[0] + c_width:
                print "Turn Left!"
            else if cx <= size[0] - c_width:
                print "Turn Right"
            else:
                print "On Track"

        else:
            print "I don't see the line"

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        rate.sleep()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
