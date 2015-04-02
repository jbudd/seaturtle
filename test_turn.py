from motor_functions import *
import sys

degree = sys.argv[1]
filename = 'logs/turn_PID_log' + str(time.time()) + 'bang_74_with_extra_good'

try:
	turn_degree_bang(degree)
	move(0)


	write_data(filename)

except KeyboardInterrupt:
	write_data(filename)