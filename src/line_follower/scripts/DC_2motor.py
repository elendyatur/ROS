import RPi.GPIO as GPIO          
from time import sleep

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
p.start(25)
p1=GPIO.PWM(en2,1000)
p1.start(25)

try:
	while True:
		print("run")
		if(temp1==1):
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
			print("forward")
		else:
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
			print("backward")
		sleep(5)

		print("stop")
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.LOW)
		GPIO.output(in4,GPIO.LOW)
		sleep(5)

		print("forward")
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
		temp1=1
		sleep(5)

		print("backward")
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.HIGH)
		GPIO.output(in3,GPIO.LOW)
		GPIO.output(in4,GPIO.HIGH)
		temp1=0
		sleep(5)

		print("low")
		p.ChangeDutyCycle(25)
		p1.ChangeDutyCycle(25)
		sleep(5)

		print("medium")
		p.ChangeDutyCycle(50)
		p1.ChangeDutyCycle(50)
		sleep(5)

		print("high")
		p.ChangeDutyCycle(75)
		p1.ChangeDutyCycle(75)
		sleep(5)

except KeyboardInterrupt:
	GPIO.cleanup()
