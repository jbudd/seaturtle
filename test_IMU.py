import RPi.GPIO as GPIO
from Adafruit_LSM303 import Adafruit_LSM303
from L3GD20 import L3GD20
import time, math

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

# while 1==1:
# 	time.sleep(dt)
# 	dxyz = s.Get_CalOut_Value()
# 	x += dxyz[0]*dt;
# 	y += dxyz[1]*dt;
# 	z += dxyz[2]*dt;
# 	print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))


def get_orientation():
	data = lsm.read()
	heading = math.atan2(data[1][0]/1000,data[1][2]/1000)*180/3.1415
	if heading < 0:
		heading += 360
	return heading



print '[(Accelerometer X, Y, Z), (Magnetometer X, Y, Z, orientation)]'
while True:
    data = lsm.read()
    print data[1][1]
    dxyz = s.Get_CalOut_Value()
    x += dxyz[0]*dt
    y += dxyz[1]*dt
    z += dxyz[2]*dt
    print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))

    time.sleep(dt) # Output is fun to watch if this is commented out
# while True:
# 	print get_orientation()
# 	data = lsm.read()
# 	print data 
# 	time.sleep(1)


