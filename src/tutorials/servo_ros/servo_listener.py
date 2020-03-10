#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO         # importar librerias de GPIO
import time                     # y tiempo

from std_msgs.msg import Float32

servoPIN = 17                   # GPIO17 (pin11) se llamara servoPIN
GPIO.setmode(GPIO.BCM)          # nombrar pines segun su nombre y no su numero
GPIO.setup(servoPIN, GPIO.OUT)  # configurar el pin11 (GPIO17) como salida

p = GPIO.PWM(servoPIN, 50)      # GPIO 17 for PWM with 50Hz
p.start(0)                      # Inicializacion

def callback(msg):
    rospy.loginfo("Roger %s", msg.data)	# msg.data: dato recibido del publisher
    p.ChangeDutyCycle(msg.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('servo_listener', anonymous=True)

    rospy.Subscriber('move_servo', Float32, callback)		# topic

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
    	listener()
    except rospy.RosInterruptException:
	p.stop()
	GPIO.cleanup()
	pass

