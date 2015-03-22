from motor_functions import *

cache = []
filename = 'IMU_log' + str(time.time())

try:
	while True:
		cache.append(lsm.read())
		time.sleep(1)
except KeyboardInterrupt:
	print cache
	output = open(filename, 'w')
	for x in cache:
		output.write(str(x))
