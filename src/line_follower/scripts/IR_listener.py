#!/usr/bin/env python
#
import rospy, time
from std_msgs.msg import Int8
import RPi.GPIO as GPIO

def IR_callback(msg):
    if msg.data==0:
        rospy.loginfo('I heard black %s', msg.data)
    else:
        rospy.loginfo('I heard no black %s', msg.data)
    
def IR_listener():
    rospy.init_node('IR_listener', anonymous=True)
    rospy.Subscriber('IR', Int8, IR_callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        IR_listener()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass        
