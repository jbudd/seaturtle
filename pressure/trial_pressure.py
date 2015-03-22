import time
import ms5803

DEVICE = '/dev/i2c-1'
ADDRESS = 0x76

sensor = ms5803.Sensor(DEVICE,ADDRESS)

cache = []

filename = 'Pressure_log' + str(time.time())

start_time = time.time()
while (time.time() - start_time) < 60:
	print sensor.read()
	cache.append(sensor.read())
	time.sleep(0.5)

output = open(filename, 'w')
for x in cache:
	output.write(str(x))




