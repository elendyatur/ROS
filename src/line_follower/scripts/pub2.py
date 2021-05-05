#!/usr/bin/env python

import rospy, time
from line_follower.msg import sensores		# import libraries
import RPi.GPIO as GPIO

GPIO_TRIGGER = 5			# Set GPIO Pins
GPIO_ECHO = 6

GPIO.setwarnings(False)     # No warnings
GPIO.setmode(GPIO.BCM)      # Modo pinout BCM
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measure():
	GPIO.output(GPIO_TRIGGER, True)
	rospy.sleep(0.00001)				# Set Trigger after 0.01ms to LOW
	GPIO.output(GPIO_TRIGGER, False)
	StartTime = time.time()

	# save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
	# save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
        
	TimeElapsed = StopTime - StartTime		# time difference between start and arrival
	distance = (TimeElapsed * 34300) / 2	# multiply with the sonic speed (34300 cm/s)
											# and divide by 2, because there and back
	return distance

def talker2():
	pub = rospy.Publisher('line_follower', sensores, queue_size=10)
	rospy.init_node('US_talker', anonymous=True)
	rate = rospy.Rate(10)					# 10hz
	while not rospy.is_shutdown():
		distance = measure()
		rospy.loginfo(distance)
		msg_send=sensores()
		msg_send.US_1=distance
		pub.publish(msg_send)
		time.sleep(2)

if __name__ == '__main__':
	try:
		talker2()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
