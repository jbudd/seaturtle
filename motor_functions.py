# import RPi.GPIO as GPIO
# import time

# time_stamp = time.time()


#pin definitions
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

def set_speed_right(speed):
	global motor_right_PWM
	speed = float(speed)
	if(speed > 0):
		#print("Starting motor")
		GPIO.output(RA,GPIO.HIGH)
		GPIO.output(RB,GPIO.LOW)
		motor_right_PWM.ChangeDutyCycle(speed)
	elif(speed < 0):
		GPIO.output(RA,GPIO.LOW)
		GPIO.output(RB,GPIO.HIGH)
		motor_right_PWM.ChangeDutyCycle(abs(speed))
	elif(speed == 0):
		global motor_right_PWM
		print "stopping motor"
		motor_gear_PWM.ChangeDutyCycle(0)

def set_speed_left(speed):
	global motor_left_PWM
	speed = float(speed)
	if(speed > 0):
		#print("Starting motor")
		GPIO.output(LA,GPIO.HIGH)
		GPIO.output(LB,GPIO.LOW)
		motor_left_PWM.ChangeDutyCycle(speed)
	elif(speed < 0):
		GPIO.output(LA,GPIO.LOW)
		GPIO.output(LB,GPIO.HIGH)
		motor_left_PWM.ChangeDutyCycle(abs(speed))
	elif(speed == 0):
		print "stopping motor"
		motor_gear_PWM.ChangeDutyCycle(0)

def set_speed_gear(speed):
	global motor_gear_PWM
	speed = float(speed)
	if(speed > 0):
		#print("Starting motor")
		GPIO.output(GA,GPIO.HIGH)
		GPIO.output(GB,GPIO.LOW)
		motor_gear_PWM.ChangeDutyCycle(speed)
	elif(speed < 0):
		GPIO.output(GA,GPIO.LOW)
		GPIO.output(GB,GPIO.HIGH)
		motor_gear_PWM.ChangeDutyCycle(abs(speed))
	elif(speed == 0):
		print "stopping motor"
		motor_gear_PWM.ChangeDutyCycle(0)

def move(speed):
	set_speed_right(speed)
	set_speed_left(speed)

def rotate_pods(degrees):
	count_degrees = int(abs(degrees)/18)
		#use interrupts to count number of encoder pulses
	count = 0
	while(count < count_degrees):
		set_speed_gear(65)
		GPIO.wait_for_edge(ENCODER,GPIO.FALLING)
		global time_stamp
		time_now = time.time()
		if(time_now - time_stamp) >= 0.13:
			print "increasing count count "
			count += 1
		time_stamp = time_now
	set_speed_gear(0)


	












