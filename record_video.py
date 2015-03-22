import picamera
import time
import sys

filename = 'video_'+ str(time.time())+'.h264'

record_time = int(sys.argv[1])

print "starting video"

try:
	with picamera.PiCamera() as camera:
	    camera.resolution = (640, 480)
	    camera.start_recording(filename)
	    camera.wait_recording(record_time)
	    camera.stop_recording()

	print 'done recording'
except KeyboardInterrupt:
	camera.stop_recording()
	print "done"	