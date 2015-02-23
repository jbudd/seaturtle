import RPi.GPIO as GPIO
from time import sleep

def motor_set_speed(motor,speed):
	GPIO.setmode(GPIO.BOARD)
	if(motor == "R"):
		Motor1A = 19
		Motor1B = 23
		Motor1E = 21
	elif(motor == "L"):
		Motor1A = 13
		Motor1B = 15
		Motor1E = 11
	elif(motor == "G"):
		Motor1A = 31
		Motor1B = 33
		Motor1E = 29
	else:
		print "Not a valid motor"
		return
	
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

	print "Turning motor on"
	if(speed > 0):
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		motor = GPIO.PWM(Motor1E,500)
		motor.start(float(speed))
	elif(speed < 0):
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		motor = GPIO.PWM(Motor1E,500)
		motor.start(float(speed))
	elif(speed == 0):
		print "stopping motor"

		left.stop()

		GPIO.cleanup()

def move_forward(speed):
	motor_set_speed("L",speed)
	motor_set_speed("R",speed)

def rotate_pods(degrees):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(35,GPIO.INPUT)

    #start the motor
	if(degrees > 0):
		motor_set_speed("G",60)
	else:
		motor_set_speed("G",-60)
	count_degrees = int(abs(degrees)/18)
	#use interrupts to count number of encoder pulses
	count = 0
	while(count < count_degrees):
		GPIO.wait_for_edge(35,GPIO.RISING)
		count += 1
	motor_set_speed("G",0)

	












