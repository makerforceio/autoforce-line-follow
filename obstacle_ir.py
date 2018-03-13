#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16MultiArray
import RPi.GPIO as GPIO

def talker():
    pub = rospy.Publisher('obstacleavoid', Int16MultiArray, queue_size=10)
    rospy.init_node('obstacle', anonymous=True)
    rate = rospy.Rate(60)
    
    sensor = [1,2,3,4,5,6,7,8]
    output = [0,0,0,0,0,0,0,0]
    GPIO.setmode(GPIO.BOARD)
    for i in sensor:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    while not rospy.is_shutdown():
        for i in range(len(sensor)):
            output[i] = GPIO.input(sensor[i])
        publish = Int16MultiArray(data=output)
        rospy.loginfo(publish)
        pub.publish(publish)
        rate.sleep()
        
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
        
        

