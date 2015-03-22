#import all modules
import RPi.GPIO as GPIO
import time
import sys
from motor_functions import *
from Adafruit_LSM303 import *
import ms5803
# from L3GD20 import L3GD20

#global time
time_stamp = time.time()

#pin definitions
RA = 19
RB = 23
RE = 21
LA = 13
LB = 15
LE = 11
GA = 31
GB = 33
GE = 29
ENCODER = 35
LED_R = 8
LED_G = 10
LED_B = 12
LED_RT = 16
LED_LFT = 18

#board definitons and init
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

GPIO.setup(LED_R,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_B,GPIO.OUT)
GPIO.setup(LED_RT,GPIO.OUT)
GPIO.setup(LED_LFT,GPIO.OUT)

#setup PWM channels
motor_right_PWM = GPIO.PWM(RE,500)
motor_right_PWM.start(0)

motor_left_PWM = GPIO.PWM(LE,500)
motor_left_PWM.start(0)

motor_gear_PWM = GPIO.PWM(GE,500)
motor_gear_PWM.start(0)

# #sensor set up
# pressure_sensor = ms5803.Sensor('/dev/i2c-1',0x76)

# # Communication object
# # gyro = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# # Preconfiguration
# gyro.Set_PowerMode("Normal")
# gyro.Set_FullScale_Value("250dps")
# gyro.Set_AxisX_Enabled(True)
# gyro.Set_AxisY_Enabled(True)
# gyro.Set_AxisZ_Enabled(True)

# # Print current configuration
# gyro.Init()
# gyro.Calibrate()

# # # Calculate angle
# # dt = 0.02
# # x = 0
# # y = 0
# # z = 0
# # while 1==1:
# # 	time.sleep(dt)
# # 	dxyz = s.Get_CalOut_Value()
# # 	x += dxyz[0]*dt;
# # 	y += dxyz[1]*dt;
# # 	z += dxyz[2]*dt;
# # 	print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))


