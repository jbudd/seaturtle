import RPi.GPIO as GPIO
import time, math, ms5803
from Adafruit_LSM303 import Adafruit_LSM303
from L3GD20 import L3GD20

time_stamp = time.time()

data_cache =[]

DEVICE = '/dev/i2c-1'
ADDRESS = 0x76

sensor = ms5803.Sensor(DEVICE,ADDRESS)

generic_filename = 'logs/test_log' + str(time.time())


# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("250dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)

# Print current configuration
s.Init()
s.Calibrate()

# Calculate angle
dt = 0.02
x = 0
y = 0
z = 0

lsm = Adafruit_LSM303()

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

GPIO.setup(ENCODER,GPIO.IN)

#setup PWM channels
motor_right_PWM = GPIO.PWM(RE,500)
motor_right_PWM.start(0)

motor_left_PWM = GPIO.PWM(LE,500)
motor_left_PWM.start(0)

motor_gear_PWM = GPIO.PWM(GE,500)
motor_gear_PWM.start(0)
	

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
		motor_right_PWM.ChangeDutyCycle(0)

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
		motor_left_PWM.ChangeDutyCycle(0)

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


def move_interval(interval):
	p = 0.5
	z = 0
	dt = 0.2

	start_time = time.time()

	while (time.time()-start_time) < interval:
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*dt
		print z
		set_speed_left(100)
		set_speed_right(100)
		data_cache.append([
			lsm.read(),
			dxyz,
			sensor.read(),
			time.time()
			])
		time.sleep(dt)

	move(0)

def turn_left(speed):
	speed = float(speed)
	set_speed_right(speed)
	set_speed_left(-speed)

def turn_right(speed):
	speed = float(speed)
	set_speed_right(-speed)
	set_speed_left(speed)	

def rotate_pods(degrees):
	degrees = float(degrees)
	speed = 0
	if(degrees > 0):
		speed = 65
	elif(degrees < 0):
		speed = -65
	else:
		print "not a degree"
	count_degrees = int(abs(degrees)/18)
		
	count = 0

	start_time = time.time()
	while(count < count_degrees and time.time()-start_time < 3):
		set_speed_gear(speed)
		GPIO.wait_for_edge(ENCODER,GPIO.FALLING)
		global time_stamp
		time_now = time.time()
		if(time_now - time_stamp) >= 0.13:
			count += 1
		time_stamp = time_now
	set_speed_gear(0)


def turn_degree(degree):
	z = 0
	dt = 0.2
	global data_cache
	while abs(degree) > abs(z):
		print z
		if degree < 0:
			turn_right(70)
		elif degree >= 0:
			turn_left(70)
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*dt
		data_cache.append([
			lsm.read(),
			dxyz,
			sensor.read(),
			time.time()
			])
		time.sleep(dt)
	print "done turning"

	move(0)


def turn_degree_bang(degree):
	z = 0
	dt = 0.2
	speed = 65
	threshold = 1
	count = 0
	global data_cache
	degree = int(degree)
	to_go = degree
	dxyz = s.Get_CalOut_Value()
	z += dxyz[2]*(dt)
	start_time = time.time()
	stopping = False
	while abs(z) < abs(degree):
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*(dt)

		
		print z
		if abs(z) < .74*abs(degree) and not stopping:
			if degree < 0:
				turn_right(speed)
			elif degree >= 0:
				turn_left(speed)
		else:
			stopping = True
			if count < 1:
				move(0)
				count += 1
			else:
				if degree < 0:
					turn_left(speed)
				elif degree >= 0:
					turn_right(speed)
		data_cache.append([
			lsm.read(),
			dxyz,
			sensor.read(),
			time.time()
			])
		time.sleep(dt)
	move(0)
	start_time = time.time()
	while time.time()-start_time < 2:
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*(dt)
		print "bonus"
		print z
		data_cache.append([
			lsm.read(),
			dxyz,
			sensor.read(),
			time.time()
			])
		time.sleep(dt)
	print "done"



def move_straight_P(interval):
	z = 0
	dt = 0.2
	p = 50
	global data_cache

	speed_right = 85
	speed_left = 100

	start_time = time.time()
	while (time.time() - start_time) < interval:
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*(dt)
		print z
		if z > 0:
			set_speed_right(max(speed_right - p*z ,65))
			set_speed_left(speed_left)
		elif z < 0:
			set_speed_right(min(speed_right - p*z, 100))
			set_speed_left(max(speed_left + p*z,65))
		else:
			set_speed_right(speed_right)
			set_speed_left(speed_left)
		data_cache.append([
			lsm.read(),
			dxyz,
			sensor.read(),
			time.time()
			])
		time.sleep(dt)
	move(0)


def write_data(filename):
	move(0)
	GPIO.cleanup()
	global data_cache
	output = open(filename, 'w')
	for x in data_cache:
		output.write(str(x))



def move_straight_PID(interval):
	z = 0
	dt = 0.2
	p = 50
	d = 10
	i = 10
	global data_cache
	z_values = [0]

	speed_right = 85
	speed_left = 100

	start_time = time.time()
	while (time.time() - start_time) < interval:
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*(dt)
		z_values.append(z)
		# print z_values[len(z_values)-2]
		deriv = (z - float(z_values[len(z_values)-2]))/dt
		intergrate = sum(z_values)
		print z
		if z > 0:
			speed_r = max(speed_right - (p*z + d*deriv + i*intergrate), 65)
			set_speed_right(min(speed_r, 100))
			set_speed_left(speed_left)
		elif z < 0:
			speed_r = max(speed_right + (p*z + d*deriv + i*intergrate), 65)
			set_speed_right(min(speed_r, 100))
			speed = min(speed_left - (p*z + d*deriv + i*intergrate),100)
			set_speed_left(max(speed,65))
		else:
			set_speed_right(speed_right)
			set_speed_left(speed_left)
		data_cache.append([
			lsm.read(),
			dxyz,
			sensor.read(),
			time.time()
			])
		time.sleep(dt)
	move(0)	












