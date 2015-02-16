import RPi.GPIO as GPIO
from time import sleep
import sys


GPIO.setmode(GPIO.BOARD)

Motor1A = 29 
Motor1B = 31
Motor1E = 33

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

speed = raw_input("Please enter a speed:")
print "Turning motor on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
p = GPIO.PWM(Motor1E,500)
p.start(float(speed))

raw_input("Press any key to stop the motor")

print "stopping motor"

p.stop()

GPIO.cleanup()

