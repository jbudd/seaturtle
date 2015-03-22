import RPi.GPIO as GPIO
import time, math

time_stamp = time.time()


#pin definitions
RB = 19
RA = 23
RE = 21
LB = 13
LA = 15
LE = 11
GA = 31
GB = 33
GE = 29
ENCODER = 35

#board definitons
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RA,GPIO.OUT)
GPIO.setup(RB,GPIO.OUT)
GPIO.setup(RE,GPIO.OUT)

GPIO.setup(LA,GPIO.OUT)
GPIO.setup(LB,GPIO.OUT)
GPIO.setup(LE,GPIO.OUT)

GPIO.setup(GA,GPIO.OUT)
GPIO.setup(GB,GPIO.OUT)
GPIO.setup(GE,GPIO.OUT)

#start motors

GPIO.output(RA,GPIO.HIGH)
GPIO.output(RB,GPIO.LOW)
GPIO.output(RE,GPIO.HIGH)


GPIO.output(GB,GPIO.HIGH)
GPIO.output(GA,GPIO.LOW)
GPIO.output(GE,GPIO.HIGH)

time.sleep(20)

GPIO.cleanup()

