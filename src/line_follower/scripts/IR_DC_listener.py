#!/usr/bin/env python
#
import rospy, time
from line_follower.msg import dos_sensores_IR
import RPi.GPIO as GPIO

def IR_callback(msg):
	if (msg.sensor_1==1 and msg.sensor_2==0):
		rospy.loginfo('Izquierda')
	elif (msg.sensor_2==1 and msg.sensor_1==0):
		rospy.loginfo('Derecha')
	elif (msg.sensor_1==1 and msg.sensor_2==1):
		rospy.loginfo('Stop')
	else:
		rospy.loginfo('Recto')
    
def IR_listener():
    rospy.init_node('IR_listener', anonymous=True)
    rospy.Subscriber('IR', dos_sensores_IR, IR_callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        IR_listener()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
