import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 31
Motor1B = 33		
Motor1E = 29

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(35,GPIO.IN)
motor = GPIO.PWM(Motor1E,500)
motor.start(0)


GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)

degrees = 72


count_degrees = int(abs(degrees)/18)
	#use interrupts to count number of encoder pulses
count = 0
while(count < count_degrees):
	motor.ChangeDutyCycle(60)
	GPIO.wait_for_edge(35,GPIO.RISING)
	count += 1

motor.stop()
GPIO.cleanup()


	


