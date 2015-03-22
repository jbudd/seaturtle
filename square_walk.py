from motor_functions import *
import time
import ms5803

# time.sleep(15)
filename = 'logs/square_log' + str(time.time())

try:
	for x in range(0,4):

		start_time = time.time()
		print "moving"
		move_straight(5)
		print "turning"	
		turn_degree(50)
	move(0)
	write_data()

except KeyboardInterrupt:
	move(0)
	write_data(filename)


