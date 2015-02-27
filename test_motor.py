import RPi.GPIO as GPIO
from motor_functions import *
import time



try:
	while True:
		move(65)
except KeyboardInterrupt:
	move(0)
	print "motors stopped"
