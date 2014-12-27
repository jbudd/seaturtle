import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

SERVO_CONTROL = 18

GPIO.setup(SERVO_CONTROL, GPIO.OUT)

control = GPIO.PWM(SERVO_CONTROL,50)

control.start(7.5)

sleep(0.5)
raw_input()
control.ChangeDutyCycle(10.5)

sleep(0.5)
raw_input()
control.ChangeDutyCycle(4.5)

sleep(0.5)
raw_input()
control.ChangeDutyCycle(7.5)

sleep(0.5)

control.stop()

GPIO.cleanup()

