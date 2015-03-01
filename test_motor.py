import RPi.GPIO as GPIO
from motor_functions import *
import time

# #pin definitions
# RA = 19
# RB = 23
# RE = 21
# LA = 13
# LB = 15
# LE = 11
# GA = 31
# GB = 33
# GE = 29
# ENCODER = 35

# #board definitons
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(RA,GPIO.OUT)
# GPIO.setup(RB,GPIO.OUT)
# GPIO.setup(RE,GPIO.OUT)

# GPIO.setup(LA,GPIO.OUT)
# GPIO.setup(LB,GPIO.OUT)
# GPIO.setup(LE,GPIO.OUT)

# GPIO.setup(GA,GPIO.OUT)
# GPIO.setup(GB,GPIO.OUT)
# GPIO.setup(GE,GPIO.OUT)

# GPIO.setup(ENCODER,GPIO.IN)

# #setup PWM channels
# motor_right_PWM = GPIO.PWM(RE,500)
# motor_right_PWM.start(0)

# motor_left_PWM = GPIO.PWM(LE,500)
# motor_left_PWM.start(0)

# motor_gear_PWM = GPIO.PWM(GE,500)
# motor_gear_PWM.start(0)
speed = raw_input("Please enter a speed:")
try:
	while True:
		move(speed)
except KeyboardInterrupt:
	move(0)
	GPIO.cleanup()
	print "motors stopped"
