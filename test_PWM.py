import RPi.GPIO as GPIO
from time import sleep

def tester(speed):
	GPIO.setmode(GPIO.BOARD)


	GPIO.setup(11,GPIO.OUT)

	motor=GPIO.PWM(11,500)

	motor.start(0)
	print "PWM 0"


	sleep(5)
	print "time for the if statement"
#	speed = 55
	if(speed > 0):
		print"time to cange to 50"
		motor.ChangeDutyCycle(float(speed))
#	sleep(5)
	elif(speed == 0):
		motor.stop()

#	sleep(5)

	motor.stop()

	GPIO.cleanup()
while(1):
	tester(50)


