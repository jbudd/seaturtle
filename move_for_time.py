import RPi.GPIO as GPIO
from motor_functions import *
import time , sys

# p_value = sys.argv[2]

filename = 'logs/move_straght_log' + str(time.time()) + '_' + 'new'
run_time = int(sys.argv[1])

# time.sleep(15)

# start_time = time.time()

# try:
# 	while (time.time() - start_time) < run_time:
# 		move(85)
# 	move(0)
# 	GPIO.cleanup()
# except KeyboardInterrupt:
# 	move(0)
# 	GPIO.cleanup()
try:
	move_straight(run_time)

	move(0)
	GPIO.cleanup()
	write_data(filename)

except KeyboardInterrupt:
	write_data(filename)
	move(0)
	GPIO.cleanup()