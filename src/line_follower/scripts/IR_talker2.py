#!/usr/bin/env python

import rospy#, time
from std_msgs.msg import Int8
import RPi.GPIO as GPIO

sensor = 8

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)          # Sin warnings
GPIO.setup(sensor, GPIO.IN)      # Pin 8 (D0) como entrada de datos a la RPi

def IR_talker():
    pub=rospy.Publisher('IR', Int8, queue_size=10)   # Nombre del Topic
    rospy.init_node('IR_talker', anonymous=True)        # Nombre del nodo
    rate = rospy.Rate(10)                               # Para que el bloque funcione a la velocidad deseada 10hz
    while not rospy.is_shutdown():
        if GPIO.input(sensor)==1:           #0=no negro, 1=negro
            rospy.loginfo("black")
            pub.publish(GPIO.input(sensor))
        else:
            rospy.loginfo("no black")
            pub.publish(GPIO.input(sensor))
        rospy.sleep(1)                      #time.sleep

if __name__ == '__main__':
    try:
        IR_talker()   
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
