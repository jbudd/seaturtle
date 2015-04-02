import picamera
import time
import sys

filename = 'low-res.h264'

record_time = 30

print "starting video"

try:
	with picamera.PiCamera() as camera:
	    camera.resolution = (400, 400)
	    camera.start_recording(filename)
	    camera.wait_recording(record_time)
	    camera.stop_recording()

	print 'done recording'
except KeyboardInterrupt:
	camera.stop_recording()
	print "done"	