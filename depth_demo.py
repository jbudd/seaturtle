from motor_functions import *
import time

filename = 'logs/depth_demo_log' + str(time.time())
#keep track of total degrees turned
degrees = 0
try:
	rotate_pods(90)
	degrees += 90

	print "moving"
	move_interval(5)

	move(0)
	print "minus 90"
	rotate_pods(-90)
	time.sleep(1)
	print "minus 90 again"
	rotate_pods(-90)

	print "moving again"
	move_interval(5)

	move(0)
	print "last 90"
	rotate_pods(90)

	move(0)

	write_data(filename)
except KeyboardInterrupt:
	write_data(filename)	




