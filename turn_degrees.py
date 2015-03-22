from Adafruit_LSM303 import Adafruit_LSM303
from L3GD20 import L3GD20
import time, math
from motor_functions import *
import sys

degree = float(sys.argv[1])

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

def turn_degree(degree):
	z = 0
	dt = 0.2
	while abs(degree) > abs(z):
		print z
		if degree > 0:
			turn_right(70)
		elif degree <= 0:
			turn_left(70)
		dxyz = s.Get_CalOut_Value()
		z += dxyz[2]*dt
		time.sleep(dt)

	move(0)


turn_degree(degree)


