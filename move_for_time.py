import RPi.GPIO as GPIO
from motor_functions import *
import time , sys

# p_value = sys.argv[2]

filename = 'logs/move_straght_log' + str(time.time()) + '_' + 'PID_3_24'
run_time = int(sys.argv[1])

# time.sleep(15)

# start_time = time.time()

# try:
# 	while (time.time() - start_time) < run_time:
# 		move(85)
# 		global data_cache
# 		data_cache.append([
# 			lsm.read(),
# 			dxyz,
# 			sensor.read(),
# 			time.time()
# 			])
# 		time.sleep(dt)
# 	move(0)
# 	write_data(filename)
# 	GPIO.cleanup()
# except KeyboardInterrupt:
# 	move(0)
# 	write_data(filename)
# 	GPIO.cleanup()
try:
	move_straight_PID(run_time)

	move(0)
	GPIO.cleanup()
	# write_data(filename)

except KeyboardInterrupt:
	# write_data(filename)
	move(0)
	GPIO.cleanup()