from motor_functions import *
import sys

degree = sys.argv[1]
filename = 'logs/turn_PID_log' + str(time.time())

try:
	turn_degree_PID(degree)


	write_data(filename)

except KeyboardInterrupt:
	write_data(filename)