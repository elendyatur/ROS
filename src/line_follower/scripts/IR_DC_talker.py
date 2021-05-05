#!/usr/bin/env python

import rospy
from line_follower.msg import dos_sensores_IR
import RPi.GPIO as GPIO

sensor1 = 7
sensor2 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)           # Sin warnings
GPIO.setup(sensor1, GPIO.IN)      # Pin 7 (D0) como entrada de datos a la RPi
GPIO.setup(sensor2, GPIO.IN)      # Pin 8 (D0) como entrada de datos a la RPi

def ir1():
	if GPIO.input(sensor1)==1:           #0=no negro, 1=negro
		color1='negro'
		return color1
	else:
		color1='blanco'
		return color1

def ir2():
	if GPIO.input(sensor2)==1:           #0=no negro, 1=negro
		color2='negro'
		return color2
	else:
		color2='blanco'
		return color2

def IR_talker():
    pub=rospy.Publisher('IR', dos_sensores_IR, queue_size=10)   # Nombre del Topic
    rospy.init_node('IR_talker', anonymous=True)        # Nombre del nodo
    rate = rospy.Rate(10)                               # Para que el bloque funcione a la velocidad deseada 10hz
    while not rospy.is_shutdown():
		color1=ir1()
		rospy.loginfo('sensor 1: %s', color1)
		color2=ir2()
		rospy.loginfo('sensor 2: %s', color2)
		msg_send=dos_sensores_IR()
		msg_send.sensor_1=GPIO.input(sensor1)
		msg_send.sensor_2=GPIO.input(sensor2)
		pub.publish(msg_send)
		rospy.sleep(1)                      #time.sleep

if __name__ == '__main__':
    try:
        IR_talker()   
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
