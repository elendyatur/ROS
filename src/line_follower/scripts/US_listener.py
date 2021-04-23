#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def US_callback(msg):
	rospy.loginfo('Distance: %f', msg.data)

def US_listener():
	rospy.init_node('US_listener', anonymous=True)
	rospy.Subscriber('US', Float32, US_callback)

    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	try:
		US_listener()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass