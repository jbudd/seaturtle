import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

LED_right = 16
LED_left = 18

GPIO.setup(LED_right,GPIO.OUT)
GPIO.setup(LED_left,GPIO.OUT)

GPIO.output(LED_right, GPIO.HIGH)

sleep(3)

GPIO.output(LED_right,GPIO.LOW)
GPIO.cleanup()
