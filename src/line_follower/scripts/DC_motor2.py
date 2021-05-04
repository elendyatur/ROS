import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

p=GPIO.PWM(en,1000)
p.start(25)



try:
	while True:
		print("run")
		if(temp1==1):
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			print("forward")
		else:
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			print("backward")
		sleep(5)

		print("stop")
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
		sleep(5)

		print("forward")
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		temp1=1
		sleep(5)

		print("backward")
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.HIGH)
		temp1=0
		sleep(5)

		print("low")
		p.ChangeDutyCycle(25)
		sleep(5)

		print("medium")
		p.ChangeDutyCycle(50)
		sleep(5)

		print("high")
		p.ChangeDutyCycle(75)
		sleep(5)

except KeyboardInterrupt:
	GPIO.cleanup()
