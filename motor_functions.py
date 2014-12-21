import RPi.GPIO as GPIO
from time import sleep

def motor_left_set_speed(speed):
	GPIO.setmode(GPIO.BOARD)

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

	print "Turning motor on"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	left = GPIO.PWM(Motor1E,500)
	left.start(float(speed))

def motor_left_stop():
	print "stopping motor"

	left.stop()

	GPIO.cleanup()

motor_left_set_speed(100)

sleep(2)

motor_left_stop()

