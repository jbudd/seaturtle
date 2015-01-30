import time
import ms5803

DEVICE = '/dev/i2c-1'
ADDRESS = 0x76

sensor = ms5803.Sensor(DEVICE,ADDRESS)

while True:
	print sensor.read()
	time.sleep(0.5)
