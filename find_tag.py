import picamera
import subprocess
import sys, time
from motor_functions import *

#init

values = []
x = 0
y = 0
z = 0

run_time = 60
start_time = time.time()

camera = picamera.PiCamera()
camera.resolution = (640,480)

filename = 'logs/find_log' + str(time.time())

found_tag = False
image_counter = 0
image_threshold = 0

missed_tags = 0
miss_tolerance = 3

# def take_image():
# 	camera.capture('image3.jpeg', use_video_port=True)

# 		argument = ' -W '+ str(640) + ' -H ' + str(480) +' image3.jpeg'

# 		proc = subprocess.Popen('../apriltags/build/bin/apriltags_demo' + argument, 
# 			shell=True,
# 			stdout = subprocess.PIPE,
# 			stderr = subprocess.PIPE,
# 			stdin=subprocess.PIPE)

# 		so, se = proc.communicate()

# 		#act

# 		values = so.split(',')

# 		return values

try:
	while (time.time() - start_time) < run_time:
		print found_tag

		# #Sense/think
		camera.capture('image3.jpeg', use_video_port=True)

		argument = ' -W '+ str(640) + ' -H ' + str(480) +' image3.jpeg'

		proc = subprocess.Popen('../apriltags/build/bin/apriltags_demo' + argument, 
			shell=True,
			stdout = subprocess.PIPE,
			stderr = subprocess.PIPE,
			stdin=subprocess.PIPE)

		so, se = proc.communicate()

		#act

		values = so.split(',')



		if len(values) > 3:
			found_tag = True
			x = float(values[1][3:])
			y = float(values[2][3:])
			z = float(values[3][3:])
			print 'Found tag at'
			print x, y, z

			#adjust heading
			if y > 1:
				print "adjusting for +y"
				turn_degree(-2)
			elif y < -1:
				print "adjusting for -y"
				turn_degree(2)
			# do something about z here

			#if more than 1m away move towards it
			if x > 1:
				print "moving closer"
				move_straight(2)
		elif found_tag:
			missed_tags += 1
			print 'missed tag'
			if missed_tags == 1:
				turn_degree(-5)
			# else:
			# 	turn_degree(-5)
			if missed_tags > miss_tolerance:
				missed_tags = 0
				found_tag = False
		elif not found_tag:
			print "no tag detected"
			if image_counter > image_threshold:
				turn_degree(5)
				image_counter = 0
			else:
				image_counter +=1
			# time.sleep(1)

	print "done tracking"
	move(0)
	write_data(filename)

except KeyboardInterrupt:
	move(0)
	write_data(filename)
