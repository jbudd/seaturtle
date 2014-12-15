import RPi.GPIO as GPIO
from time import sleep
import sys
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
p = GPIO.PWM(Motor1E,500)
speed = sys.argv[1]
if not speed:
	p.start(50)
else:
	p.start(float(speed))

sleep(2)
p.stop()
GPIO.cleanup()

