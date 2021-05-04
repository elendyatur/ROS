#!/usr/bin/env python
#
import rospy, time
from line_follower.msg import dos_sensores_IR
import RPi.GPIO as GPIO

in1 = 24
in2 = 23
in3 = 17
in4 = 27

en1 = 25
en2 = 22
temp1=1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

p=GPIO.PWM(en1,1000)
p.start(75)
p1=GPIO.PWM(en2,1000)
p1.start(75)


def IR_callback(msg):
	if (msg.sensor_1==1 and msg.sensor_2==0):
		rospy.loginfo('Izquierda')
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
	elif (msg.sensor_2==1 and msg.sensor_1==0):
		rospy.loginfo('Derecha')
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.LOW)
		GPIO.output(in4,GPIO.LOW)
	elif (msg.sensor_1==1 and msg.sensor_2==1):
		rospy.loginfo('Stop')
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.LOW)
		GPIO.output(in4,GPIO.LOW)
	else:
		rospy.loginfo('Recto')
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
    
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
