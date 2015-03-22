import RPi.GPIO as GPIO
from motor_functions import *
import time


speed = raw_input("Please enter a speed:")
try:
	while True:
		move(speed)
except KeyboardInterrupt:
	move(0)
	GPIO.cleanup()
	print "motors stopped"
