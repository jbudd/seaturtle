import picamera
import subprocess
import sys, time


camera = picamera.PiCamera()

filename = 'picture_' +str(time.time()) + '.png'

time.sleep(3)

camera.capture(filename)





