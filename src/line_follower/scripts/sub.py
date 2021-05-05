#!/usr/bin/env python
#
import rospy, time
from line_follower.msg import sensores
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

in1 = 24
in2 = 23
in3 = 17
in4 = 27

en1 = 25
en2 = 22
temp1=1

var_IR_1=1
var_IR_2=1

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


def callback(msg):
	global var_IR_1
	global var_IR_2
	global temp1
	if msg.US_1 == 0:
		rospy.loginfo(" ")
		var_IR_1=msg.IR_1
		var_IR_2=msg.IR_2
	elif (msg.US_1!=0 and msg.US_1<10):
		rospy.loginfo('Stop')
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.LOW)
		GPIO.output(in4,GPIO.LOW)
	else:
		if (var_IR_1==1 and var_IR_2==0):
			rospy.loginfo('Izquierda')
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
		elif (var_IR_2==1 and var_IR_1==0):
			rospy.loginfo('Derecha')
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)
		elif (var_IR_1==1 and var_IR_2==1):
			if temp1==1:
				rospy.loginfo('Bifurcacion_Izquierda')
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.HIGH)
				GPIO.output(in4,GPIO.LOW)
				temp1=0
			else:
				rospy.loginfo('Bifurcacion_Derecha')
				GPIO.output(in1,GPIO.HIGH)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.LOW)
				temp1=1
		else:
			rospy.loginfo('Recto')
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
	rospy.sleep(2)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('line_follower', sensores, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	var_IR_1=0
	var_IR_2=0
	try:
		listener()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
